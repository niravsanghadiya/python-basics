
# array.array is standard library
# Features:
# 1 - Stores only one data type
# 2 - More memory efficient than list for large dataset
# 3 - Not flexible as lists
import array

int_array = array.array('i',[1,2,3,4]) # i means integer


for i in range(len(int_array)):
    print(f'Integer Index : {i} Value: {int_array[i]}')

float_array = array.array('f',[1,3,5,6])  # f means float


for f in range(len(float_array)):
    print(f'Float array Index : {f}  Value: {float_array[f]}')


# Basic Operations

# 1. Access
print(int_array[2]) # print element having index 2
print('\n')

# 2. Append
int_array.append(5)
float_array.append(8.0)

# 3. Insert at position
int_array.insert(2,9)
for x in range(len(int_array)):
    print(int_array[x])
print('\n')

# 4. Remove an element
int_array.remove(3) # remove an element at index 3
int_array.pop() # remove last element
int_array.reverse() # reverse an array

for x in range(len(int_array)):
    print(int_array[x])
print('\n')

# 5. Index of element
print(f'Index of element {int_array.index(9)}')


# Copying array

# Shallow copy
copy_array = int_array
print('Shallow Copy array')
for i in range(len(copy_array)):
    print(copy_array[i])
print('\n')

# Deep Copy
import copy
deep_copy_array = copy.deepcopy(int_array)
print('Deep Copy array')
for i in range(len(deep_copy_array)):
    print(deep_copy_array[i])
