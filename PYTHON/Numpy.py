
import numpy as np

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) 

# convert to numpy arrays
NpList = np.array(List)
NpTup = np.array(tup)

# for each element in list multiple by 5
print(NpList * 5)
print(NpTup * 7)

# create a custom empty array of 4 by 4 
print(np.full([4, 4], 0, dtype=int))