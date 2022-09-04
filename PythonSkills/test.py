words = ['hi', 'wow']
my_dict = {'hi': 'hoo', 'wow': 'wooo'}
numbers = [-x for x in range(5)]
nested_lists = [[x for x in range(5)] for y in range(5)]

even_numbers = [x for x in numbers if x % 2 == 0]
print('even_numbers: ', even_numbers)

capitalized = [x.capitalize() for x in words]
print('capitalized: ', capitalized)

capitalized_d = {x[0].capitalize(): x[1] for x in my_dict.items()}
print('capitalized_d: ', capitalized_d)

abs_sum = sum([abs(x) for x in numbers])
print('abs_sum: ', abs_sum)

set_letters_used = {letter for letter in "hello"}
# set_letters_used = [letter for letter in "hello"]
print('set_letters_used: ', set_letters_used)

switch_key_value = {x[1]: x[0] for x in my_dict.items()}
print('switch_key_value: ', switch_key_value)

squared = [x**2 for x in range(10)]
print('squared: ', squared)

divisible_3_5 = [x for x in range(20) if x % 3 == 0 if x % 5 == 0]
print('divisible_3_5: ', divisible_3_5)

flattened_list = [x for y in nested_lists for x in y]
print('flattened_list: ', flattened_list)

tuples = [(x, y) for x in range(3) for y in range(3)]
print('tuples: ', tuples)
