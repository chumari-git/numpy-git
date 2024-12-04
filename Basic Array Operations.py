import numpy as np 

a = np.array([[1,3,4,5,7],[2,4,5,6,9]])
b = np.random.rand(2,5)
c = np.random.rand(5,3)

# print(a)
# print()
# print(np.mean(a))
# print(np.mean(a,axis=0))
# print(np.mean(a,axis=1))

print(c)

print("\nReshape")
print(a.reshape(5,2))

print("\nSlicing")
print(a[:,2:])

print("\nAddition")
print(a+b)

print("\nSubtraction")
print(a-b)

print("\nMultiplication")
print(a*b)

print("\nMatrice Multiplication")
print(np.matmul(b,c))


print(np.mean(a))
c = np.mean(a,axis=0)
r = np.mean(a,axis=1)
print()
print(r)
print()
data = np.array([1, 2, 3, 4, 5, 6])
mean_value = np.mean(data)
print(mean_value)  # Output: 3.5





