# JS

0:21:19 Declare String Variables

## Variables and Types

### [Question](http://www.javascripter.net/faq/deleteavariable.htm): Can I delete a JavaScript variable?

Answer: Not always – it depends.

You cannot delete a variable if you declared it (with var x;) at the time of first use.

However, if your variable x first appeared in the script without a declaration, then you can use the delete operator (delete x;) and your variable will be deleted, very similar to deleting an element of an array or deleting a property of an object.

Surprisingly, if you have not declared your variable with the var keyword at the time of first use, then delete will work

### Question: How do I delete an array element in JavaScript?

Answer: Two different ways to delete an element myArray[n] from myArray are:

delete myArray[n] (faster, but leaves a gap at index n)
myArray.splice(n,1) (slower, but does not leave a gap in the array)

```js

// Variables and Types

// initialization
my_var = "Global"
var my_string = "Hello!"
const my_float = 7.0
let my_int = 7
let my_array = [1, 2, 3]
let my_dict = {}
// let my_set = set()
// let my_bytes = bytes(message, 'utf-8')
let my_bool = false
// let my_tuple = (1, 2)


// type
typeof my_var

// delete a variable
delete my_var

// print representation of a variable
console.log(my_var)

//  assign vales to be nothing, a NoneType
my_var = null
my_var = undefined

// assign vales form tuple
let a=1, b=2
```

## Arrays

### sort

By default, the sort() function sorts values as strings. However, if numbers are sorted as strings, "25" is bigger than "100", because "2" is bigger than "1". You can fix this by providing a compare function.

**Compare function**:

```js
const my_array = [40, 100, 1, 5, 25, 10];
my_array.sort(function(a, b){return b - a});
```

The compare function compares all the values in the array, two values at a time (a, b).
When comparing 40 and 100, the sort() method calls the compare function(40, 100).
The function calculates 40 - 100 (a - b), and since the result is negative (-60),  the sort function will sort 40 as a value lower than 100.

### (filter())[https://www.freecodecamp.org/news/how-to-count-objects-in-an-array/]

The filter method does just that – it iterates through each element in the array and filters out all elements that don't meet the condition(s) you provide. It then returns a new array with all the elements that returned true based on your condition(s).

### reduce()

The reduce() method executes a reducer function for array element.

The reduce() method returns a single value: the function's accumulated result.

The reduce() method does not execute the function for empty array elements.

The reduce() method does not change the original array.

### JSON.stringify()

turns whatever into a string

```js
// arrays
var my_array = [1, 2, 3]

//  add to array
my_array.push(4)
my_array.shift(0)

// accessing array variables
my_array[0]
my_array[my_array.length-1]

//  delete form a array, by index
delete my_array[0]
delete my_array[-1]

// delete form a array, by value
const array = [2, 5, 9];
const index = array.indexOf(5);
if (index > -1) { // only splice array when item is found
  array.splice(index, 1); // 2nd parameter means remove one item only
}

// sort array
const my_unsorted_array = [40, 100, 1, 5, 25, 10];
my_unsorted_array.sort(function(a, b){return b - a});

// reverse array
my_unsorted_array.reverse()

// count value, 0s, in a array
let counter = 0;
for (let i = 0; i < my_array.length; i++) {
  if (my_array[i] == '0') counter++;
}

counter = 0;
for (const obj of my_array) {
  if (obj == '0') counter++;
}

var count = my_array.filter(function(item){
  if (item == 0) {
    return true;
  } else {
    return false;
  }
}).length;

count = my_array.filter(item => item == 0).length

count = my_array.reduce((counter, obj) => {
  if (obj == '0') counter += 1
  return counter;
}, 0);

count = my_array.reduce((counter, obj) => obj == '0' ? counter += 1 : counter, 0);

// length of a array
my_array.length

// randomize the order of items in a array
my_array.sort(() => Math.random() - 0.5);
```

---

## Basic Operators

```js
// assigning
a = b || c // if b is null will take c

// Arithmetic Operators
c = a + b
c = a - b
c = a * b
c = a / b
c += a //c=c+a
c++ //c=c+1

// Comparison Operators, all True
c = 1 == 1
c = 1 === 1
c = 1 !== '1'
c = 1 != 2
c = 1 < 2
c = 1 <= 2
c = 1 < 2 < 3

// power by, Exponentiation
c = a ** b

// integer division, no float points
int_div = Math.floor(a/b)
int_div = Math.trunc(a/b)

// division reminder, modulus operator
remainder = a % b

// concatenation
String_c = String_a + String_b
array_c = array_a.concat(array_b)
array_c = [...array_a,...array_b];

// part of string
part = my_string.slice(start,end)
part = my_array.slice(start,end)

// skip in a array, A double colon ::x means to skip by x
even_members = my_array.filter(item => array.indexOf(item) % 2 == 0);

// Logical Operators, all True
true && true
true || false
! false

// Bitwise Operators, all 1 
c = 1 & 1
c = 1 | 0
c = 1 ^ 0
c = ~ -2
c = 2 >> 1
c = 1 << 0

// if you could not to understand Bitwise Operators, review how to convert from decimal to binary

// Membership Operators, all True
c = My_member in My_object
c = !(Not_member in My_object)

```

## String Formatting

## Basic String Operations

## Conditions

switch/break/default

## Loops

## Functions

## Classes and Objects

## Dictionaries/Objects

The data stored in the form of key-value pairs is called an Object or a Dictionary. Objects and dictionaries are similar; the difference lies in semantics. In JavaScript, dictionaries are called objects, whereas, in languages like Python or C#, they are called dictionaries.

Object could be used rather than switch statement, with the condition value as a keys

```js

var my_obj={}

// accessing it
a = my_dic.my_prop
a = my_dic["my_prop_with_space"]

// deleting it
delete my_dic.my_prop

// check if has a property, return boolean
my_obj.hasOwnProperty(my_prop)



```

## Modules and Packages

## Randoms
