#1. Create a null vector of size 10 but the fifth value which is 1.
import numpy as np
null_vector = np.zeros(10)
null_vector[4] = 1

#2. Create a vector with values ranging from 10 to 49
import numpy as np
# Create a vector with values ranging from 10 to 49
vector = np.arange(10, 50)

#3. Create a 3x3 matrix with values ranging from 0 to 8

import numpy as np
# Create a 3x3 matrix with values ranging from 0 to 8
matrix = np.arange(9).reshape(3, 3)

#4.  Find indices of non-zero elements from [1,2,0,0,4,0]

import numpy as np

# Create the array
arr = np.array([1, 2, 0, 0, 4, 0])
# Find indices of non-zero elements
indices = np.nonzero(arr)
# Print the indices
print(indices)

#5. Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np

# Create a 10x10 array with random values between 0 and 1
array = np.random.rand(10, 10)
# Find the minimum and maximum values in the array
min_value = np.min(array)
max_value = np.max(array)
# Print the results
print("Minimum value:", min_value)
print("Maximum value:", max_value)

#6. Create a random vector of size 30 and find the mean value.

import numpy as np
# Create a random vector of size 30
vector = np.random.rand(30)
# Find the mean value of the vector
mean_value = np.mean(vector)
# Print the mean value
print("Mean value:", mean_value)




