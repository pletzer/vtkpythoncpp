import vtk

# Read the vtk file
reader = vtk.vtkPolyDataReader()
reader.SetFileName('polyex.vtk')
reader.Update()

# pdata is a vtkPolyData instance
pdata = reader.GetOutput()

# Get the address of the underlying c++ object as 
# a string and convert the hex into an integer. 
# Note: must filter out 'Addr=', hence [5,:]
addr = int(pdata.GetAddressAsString('vtkPolyData')[5:], 16)

# Open the shared library. You might need to set 
# LD_LIBRARY_PATH (on Linux/Solaris) or DYLD_LIBRARY_PATH
# (on Mac OS X) if you get "dlopen(foo.so, 6): Library not loaded" 
# error.
import ctypes
lib = ctypes.cdll.LoadLibrary('foo.so')

# Call the C++ 'foo' procedure, will print out the number of 
# points. Note that the address must be converted to c_long
# on Mac OS X platform at least. 
lib.foo(ctypes.c_long(addr))



