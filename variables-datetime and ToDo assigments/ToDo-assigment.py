
# print float value into integer
float_variable = 3.14159
int_value = int(float_variable)   # here I am used int()function to print float value into integer
print(int_value)



def __init__(self,modelname, year):
      print()       
'''When we use double underscor then its create a special method  called dunder method,
   The __init__ method, in particular, is a special method used as the constructor for 
   a class. It is automatically called when an object of the class is created '''

# dictionary

my_dict = {}
key = "colors"

              # Check if the key is already in the dictionary
if key in my_dict:
    my_dict[key].add("red")  # Add a value to the set
    my_dict[key].add("blue")
else:
    my_dict[key] = {"red", "blue"}  # Create a new set for the key

print(my_dict)

# Here we give multiple values to one key using set




my_info = {
    'name': 'John cina',
    'age': 30,
    'name': 'Rock'  # This will overwrite the value of the 'name' key
}
print(my_info) 
''' In the dictionary we cannot have duplicate keys. Each key must be unique within the 
   dictionary. If we try to add a new key with the same name as an existing key, it will
   simply overwrite the existing key's value.'''

my_info = {
    'person1': {
        'name': 'Ankikt',
        'age': 21,
        'city': 'Bhor'
    },                          # Here we can use nested dictionary inone dictionary
    'person2': {
        'name': 'Akshay',
        'age': 25,
        'city': 'une'
    }
}
print(my_dict['person1']['name'])  # Accessing a nested value (John)
print(my_dict['person2']['city'])  # Accessing another nested value (Los Angeles)



   
   #what is array?
'''--> If we have to store more than one item or value at the same time then we use array
      We can declare an array like x[100], storing 100 data in x. It is a container that
      can hold a fixed number of items'''
import array

# Creating an array of integers
int_array = array.array('i', [1, 2, 3, 4, 5])

# Accessing elements
print(int_array[0])  # Prints the first element (1)

# Adding elements
int_array.append(6)

# Removing elements
int_array.remove(3)

# Getting the length of the array
length = len(int_array)


#finally block
'''The finally block is used to define code that should be executed regardless of whether
   an exception is raised or not. This block is commonly used for cleanup operations like 
   closing files, releasing resources, or logging.'''

try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Code to handle the specific exception
    print("A ZeroDivisionError occurred.")
finally:
    # Code that should always be executed
    print("This will always be executed, whether there was an exception or not.")
