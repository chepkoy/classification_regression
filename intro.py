# Basics of numpy
import numpy as np


# Creating a numpy array
int_array = np.array([2,3,4,5])
float_array = np.array([1.2,3.5,5.1])

print(int_array)
print(float_array)

# Returning the datatype

print(int_array.dtype)
print(float_array.dtype)

# Special array creations zeros array and ones array

zero = np.zeros([2,4])

print(zero)

ones = np.ones([3,3])
print(ones)

# Creating an array containing a series of numbers with the range function

number_range =np.arange(1,10,1)
print(number_range)

# Addition

even_numbers = np.array([2,4,6,8,10])
odd_numbers = np.array([1,3,5,7,9])
add_two_arrays = even_numbers + odd_numbers
print(add_two_arrays)

# Subtraction

sub_two_arrays = even_numbers - odd_numbers
print(sub_two_arrays)

# Multiplication

product = even_numbers * odd_numbers
print(product)

# Matrix multiplication
matrix_1 = np.array([[1,1],[2,3]])
matrix_2 = np.array([[2,0],[1,6]])
matrix_multiplication = matrix_1.dot(matrix_2)
print(matrix_multiplication)


# unary operations

summ = even_numbers.sum()
meann =even_numbers.mean()
maxx = even_numbers.max()

print(summ)
print(meann)
print(maxx)
