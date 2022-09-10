
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


// arrays
// var my_array = [1, 2, 3]

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


// Arithmetic Operators
c = a + b
c = a - b
c = a * b
c = a / b

// Comparison Operators, all True
c = 1 == 1
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



// objects

my_obj ={}

my_obj.hasOwnProperty(my_prop)

JSON.stringify
