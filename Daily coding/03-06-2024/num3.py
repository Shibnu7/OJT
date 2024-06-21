import numpy as np

orginal_array = np.array([1,2,3,4,5,6])
print("orginal array : ", orginal_array)

view_array = orginal_array.view()
print("view of the orginal array is : ", view_array)

view_array[2]= 30
print("modified view of the array :",view_array)
print("orginal array after modifying the view : ",orginal_array)

copy_array = orginal_array.copy()
print("copy array :", copy_array)

copy_array[0]=10
print("modified copy array :", copy_array)
print("orginal array after modifying the copy array : ",orginal_array)