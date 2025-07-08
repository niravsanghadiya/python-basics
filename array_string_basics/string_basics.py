
# Creating String

s1 = "test string"
s2 = "sample text"
s3 = """ multi line 
text"""
print(f'multi line string : {s3}')
print(s1,s2,s3)

# Basic string methods

str_local = "Hello World"
print(str_local.lower()) # lower string
print(str_local.upper()) # upper case string
print(str_local.replace('l','_')) # replace l with _     output: He__o Wor_d
print(str_local.split())  # ['Hello', 'World']
print(str_local.startswith('H')) # True for H else False for other characters
print(str_local.endswith('e')) # False

# Concatenation and Repetition

s2 = "east"
s3 = "west"

print(s2 + " " + s3) # Concatenation - east west
print(s2*2) # Repetition easteast

# f-string formatted
name = "this is test"
age = 23
print(f'name : {name} and age : {age}')

# format() method
print('name {} and age is {}'.format(name,age))

# Joining string
words = ['hello', 'world']
print(' '.join(words))

letters = ['a','b','c']
print('-'.join(letters))

# Splitting - Split into array of string
split_text = "python is awesome"
print(split_text.split(' ')) # ['python', 'is', 'awesome']

# String interning
str2 = "hello"
str3 = "hello"
print(str2 is str3) # True, because of string interning

# str is short notation of string. It is an immutable sequence of Unicode characters
print(type(str2))  #<class 'str'>
a = str("hello")
b = str("hello")
print(a is b)

int_string = str(123)
print(int_string) # convert int to string '123'
bool_string = (str(True)) # convert boolean to string 'True'
print(type(bool_string)) # <class 'str'>

# we can convert almost any object into its string representation

num = str(12)
print(type(num)) # <class 'str'>

# Get type of object
num_int = 6
print(type(num_int)) # <class 'int'>

# Indexing and Slicing
custom_text = "python"
print(custom_text[0]) # print 1st character which is p
print(custom_text[-1]) # print last character which is n

print(custom_text[1:4]) # yth
print(custom_text[:]) # python
print(custom_text[::-1]) # reverse the string - nohtyp



