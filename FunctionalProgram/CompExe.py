# Comprehension Exercise 

some_list = ['a','b','c','b','d','m','n','n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

comp_list = ['a','b','c','b','d','m','n','n']

dup = list(set([num for num in comp_list if comp_list.count(num) > 1]))

print(dup)