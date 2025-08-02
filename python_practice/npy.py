import numpy as np

# lis = [98, 89, 88, 90]
# print(lis)

# arr = np.array([98, 89, 88, 90])
# print(arr)

## 2D array

# arr = np.array([[1,2,3], [4,5,6]])
# print(arr)

## Creating array with default values

# arr = np.full((2,3), 7)   #Will create a 2 by 3 array with default value 7.  #np.zeroes() #np.ones()
# print(arr)

##Creating sequences of no.s in array

# arr = np.arange(10,1,-2)
# print(arr)

##Creating Identity Matrices

# arr = np.eye(4)
# print(arr)

##Attributes and calculations

# arr = np.array([[1,2,3],[5,6,7]])

# print(arr.shape)    #rows,columns
# print(arr.size)     #no of elements in array
# print(arr.ndim)     #no of dimensions
# print(arr.dtype)    
# farr = arr.astype(float)   #type casting
# print(farr.dtype)
# print(arr[0][0])
# print(arr[[0, 1], [0, 2]])

# print(arr + 2)
# print(arr.min(), arr.max(), arr.sum())
## boolean masking
# print(arr[arr > 1])

##Reshaping

# arr = np.array([1,2,3,4,5,6])
# print(arr.reshape(2,3))       #It creates a view of original array  1D -> 2D -> 3D

##Ravel and flatten

# arr = np.array([[1,2,3], [4,5,6]])
# print(arr.ravel())
# print(arr.flatten())   #Both coverts 2D,3D -> 1D   .ravel() -> View  .flatten() -> copy

## Manupilations

#1D insert
# arr = np.array([1,2,3,4,5])
# new_arr = np.insert(arr, 1, 20, axis=0)
# print(new_arr)

#2D insert
# arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
# new_arr = np.insert(arr, 1, [10, 20, 30], axis=1)     #axis= 0 is row, 1  is columns
# print(new_arr)