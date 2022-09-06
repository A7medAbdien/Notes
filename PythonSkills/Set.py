import random
from copy import copy
my_set = set([1, 2, 3])
my_set.add("f")
my_set.update({4})
# print(my_set)

# my_set2 = set(my_set)
# my_set2 = copy(my_set)
my_set2 = my_set.copy()
# my_set2 = my_set[:]  # set is not a subscriptable object
# print(my_set2)

# element_index = random.randint(0, len(my_set) - 1)
# my_set.remove(element_index)

# my_set2.difference_update({"f"})
# print(my_set)
print(my_set2)
# print(len(my_set))
# print(my_set.issuperset(my_set2))
# print(my_set2.issubset(my_set))

# my_list = [x for x in range(3)]
# my_list += [x for x in range(3)]
# print(my_list)
# my_unique_list = list(set(my_list))
# print(my_unique_list)
