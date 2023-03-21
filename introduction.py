#numpy.py
"AUTHOR:------>"Mudith Nahata"
import numpy as np
#List Vs Numpy Timetaken
#from time module importing Process Time

from time import process_time

#checking wether time taken by the list
python_list=[i for i in range(10000)]
start_time=process_time()
python_list=[i+5 for i in range(10000)]
end_time=process_time()
#to check time taken by the both list
time_taken=end_time-start_time
print(time_taken)
#now creating a numpy array
np_array=np.array([i for in range(10000)])
start_time=np_array.process_time()
np_array+=5
end_time=process_time()
print(end_time-process_time)
