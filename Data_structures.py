# quick reminder for data structures
# list
a = [1,2,3,4,5,6,7,8,9] 

# dictionary
# no duplicate keys
b = {'key0' : 1, 'key1': 2, 'key3' : 3}  

# tuple
# immutable
c = ('number1', 'number2', 'number3')  

# set
# --unordered
# -- no duplicates
d = {1,2,3,4,5}  

# acessing each data structure through print statement
# I will go for the second item in each data type

print(f'List item 2: {a[1]}\n')

print('Dictionary key 2: ', b['key1'], '\n')

print(f'Tuple item 2: {c[1]}\n')

# quick look at is and not evaluating statements

inty = 3
print(type(inty) is int) # will return True or False if depending on object type

# Or we can use it in a function using isinstance which is better for general object programming

def type_check(value):
    if isinstance(value, int):
        print(f"{value} is an integer")
    else:
        value_type = type(value)
        print(f'{value} is not an integer it is actually a {value_type}')
type_check(10)