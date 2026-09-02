from array import *
arr1 = array('i',[23,34,66,55,44,12,23])
# arr2 = array(arr1.typecode, arr1.tolist()) --> uses more memory
arr2 = array(arr1.typecode, (n for n in arr1)) #memory efficient
print(arr2)
arr1[2] = 100
arr1.append(78)
print(arr1)

# for n in arr1:
#     print(n)