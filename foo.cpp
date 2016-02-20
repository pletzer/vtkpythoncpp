/**
 * Example of a procedure that operates on a vtkPolyData instance
 * 
 * To create a shared library I typed:
 * VTK 5.10
 * g++ --shared -I $VTK_INCLUDE_DIR foo.cpp -L $VTK_LIBRARY_DIR -l vtkCommon -l vtkFiltering -o foo.so
 * VTK 6.3
 * g++ --shared -I $VTK_INCLUDE_DIR foo.cpp -L $VTK_LIBRARY_DIR -l vtkCommonDataModel-6.3 -l vtkCommonCore-6.3 -fPIC -o foo.so
 * VTK_INCLUDE_DIR and VTK_LIBRARY_DIR are the directories where the VTK include and library files 
 * are installed.
 */

#include <vtkPolyData.h>
#include <iostream>

extern "C"
void foo(vtkPolyData* pdata) {
    std::cout << "Number of points (C++): " << pdata->GetNumberOfPoints() << '\n';
}

