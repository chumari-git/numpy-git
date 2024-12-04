import numpy as np


array = np.array([1,4,23,6,4,3,73,7,43,15])
array_2 = np.array([5,4,36,2,867,844,384,12,37,95])
print(array)

sumple = array + 5
dotprod = np.dot(array,array_2)

print(sumple)
print(dotprod)

mean = np.mean(array)
print(mean)
std = np.std(array_2)
print(std)
var = np.var(array_2)
print(var)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
element_sum = arr1 + arr2
element_mul = arr1 * arr2
print("1", element_sum, element_mul)

x = np.array([0, 1, 2, 3])
y = np.array([1, 3, 7, 13])
poly_coeff = np.polyfit(x, y, 2)
print("2",poly_coeff)

a = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(a, b)
print(x,"lin")









