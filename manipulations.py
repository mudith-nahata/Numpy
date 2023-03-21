#manipulations.py
"AUTHOR--->MUDITH NAHATA"
import numpy as np
array=random.randint(10,30(2,3))
#where 10 and 30 are the range of the values and 2 and 3 describes rows and columns of the array
print("{} {}".format(array,array.shape))
#transpose of array
arr=np.transpose(array)
print("{}".format(arr))
print("{}".format(arr.shape))
#again transpose
trans2=arr.T #transpose the matrix
print("{}".format(trans2))
print("{}".format(trans2.shape))

