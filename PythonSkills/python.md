# python

## Variables and Types

```py
# initialization
my_string = "Hello!"
my_float = 7.0
my_int = 7
my_array = [1, 2, 3]
my_dict = {}
my_set = set()
my_bytes = bytes(message, 'utf-8')
my_bool = False
my_tuple = (1, 2)

# type
type(var)

# delete a variable
del var

# print representation of a variable
print(var)

# assign vales to be nothing, a NoneType
var=None

# assign vales form tuple
a, b = (1, 2)
```

## List

```py
# add to list
my_list.append(1)

# accessing list variables
my_list[0]
my_list[-1]

# delete form a list, by index
del my_list[0]
del my_list[-1]

# delete form a list, by value
if value in my_list:
    my_list.remove(value)

# sort list
my_list.sort()

# reverse list
my_list = my_list[::-1]
my_list = list(reversed(my_list))
my_list.reverse()

# count value in a list
my_list.count(value)

# length of a list
len(my_list)

# randomize the order of items in a list
from random import shuffle
shuffle(my_list)
```

## Basic operations, [recommended](https://www.w3schools.com/python/python_operators.asp)

```py
# Arithmetic Operators
c = a + b
c = a - by
c = a * b
c = a / b

# Comparison Operators, all True
c = 1 == 1
c = 1 != 2
c = 1 < 2
c = 1 <= 2
c = 1 < 2 < 3

# power by
c = a ** b

# integer division, no float points
int_div = a // b

# division reminder, modulus operator
int_div = a % b

# concatenation
String_c = String_a + String_b
List_c = List_a + List_b

# part of string
part = string[2:3]

# skip in a list, A double colon ::x means to skip by x
even_members = full_list[::2]

# Logical Operators, all True
True and True
True or False
not False

# Bitwise Operators, all 1 
c = 1 & 1
c = 1 | 0
c = 1 ^ 0
c = ~ -2
c = 2 >> 1
c = 1 << 0

# if you could not to understand Bitwise Operators, review how to convert from decimal to binary

# Identity Operators, for objects, all True
c = True is True
c = True is not False

# Membership Operators, all True
c = My_member in My_object
c = Not_member not in My_object

```

DailyReports

<https://stackoverflow.com/questions/45580350/prints2-12-what-does-this-line-do-in-the-below-program>

## Strings

```py
# initialization multi-line
my_string = "This is a\n" . "multiline string"

# concatenate a string
my_string = "Hello " + "World!"

# string length
len(my_string)

# string appears in another string
if "fun" in "this is fun":
    print("this is fun contains the word fun.")

# index of a substring
"this is fun".index("fun")

# string has only digits in it
if digit_string.isdigit():
    print("digit_string contains only digits.")

# string starts with another string
if "substring".startswith("sub"):
    print("substring starts with sub")

# join
print(",".join(["foo", "bar"]))

# split
print("foo,bar".split(","))

# print a number using a: format string
print("%d" % number)

# print a number using an: "f string"
number = 123
print(f"{number}")

# print a number using: the string format function
number = 123
print("{number}".format(number=number))


```

## functions

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number

a static method is bound to a class rather than the objects for that class.

An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class. A class which contains one or more abstract methods is called an abstract class. An abstract method is a method that has a declaration but does not have an implementation. While we are designing large functional units we use an abstract class. When we want to provide a common interface for different implementations of a component, we use an abstract class.

## List vs Array

List: A list in Python is a collection of items which can contain elements of multiple data types, which may be either numeric, character logical values, etc. It is an ordered collection supporting negative indexing. A list can be created using [] containing data values.
Contents of lists can be easily merged and copied using python’s inbuilt functions.

Array: An array is a vector containing homogeneous elements i.e. belonging to the same data type. Elements are allocated with contiguous memory locations allowing easy modification, that is, addition, deletion, accessing of elements. In Python, we have to use the array module to declare arrays. If the elements of an array belong to different data types, an exception “Incompatible data types” is thrown.

```py

# creating an array containing same 
# data type elements 
import array
  
sample_array = array.array('i', [1, 2, 3])  
  
# accessing elements of array
for i in sample_array:
     print(i)
```

## direction

```py
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

dict_3 = dict_2.copy()
dict_3.update(dict_1)

print(dict_3)i 
```

dict.setdefault will precisely "set a value in a dict only if the value is not already set".

dict. get(key[, default]). This method returns the value for key if key is in the dictionary, else returns default.

Using has_key() method returns true if a given key is available in the dictionary, otherwise, it returns a false. With the Inbuilt method has_key(), use the if statement to check if the key is present in the dictionary or not.

## models and packages

Because this is just how Python works - keywords such as class and def are not declarations. Instead, they are real live statements which are executed. If they were not executed your module would be empty. [here](https://stackoverflow.com/questions/6523791/why-is-python-running-my-module-when-i-import-it-and-how-do-i-stop-it)

```py
# stuff to run always here such as class/def
def main():
    pass

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()
```

model vs package vs _\_init__.py ,[here](https://stackoverflow.com/questions/36515197/python-import-module-from-a-package)

## List comprehension

output = [result for member in iterable if condition]

```py

# list
capitalized = [x.capitalize() for x in words]

# dictionary keys
capitalized_d = {x[0].capitalize() : x[1] for x in d.items()}

# nested if-statements
d = [x for x in range(20) if x % 3 == 0 if x % 5 == 0]
```

## set

[Set Objects](https://docs.python.org/3/c-api/set.html),
[Set Structure](https://docs.python.org/3/tutorial/datastructures.html),
[ALL 👌](https://python-reference.readthedocs.io/en/latest/docs/sets/)
