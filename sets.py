#Last Tutorial in the Python I folder 
#Sets are collection of unique objects and has no duplicate

my_set = {1,2,3,4,5}
print(my_set)
my_set.add(100)
my_set.add(2)## wont duplicate 2 in the set
print(my_set)

my_list =(6,7,8,9,0)
print(set(my_list))

print(2 in my_set)
print(len(my_set))
## print(my_set[3]) indexing wont work
new_set = my_set.copy()
print(new_set)

your_set = {4,5,6,7,8,9,10}

#.difference(),.discard(),.isdisjoint(),.union(),.issuperset()
#.issubset(),.intersection(), .difference_update()

print(my_set.difference(your_set))
print(my_set.discard(4))
print(my_set)
print(my_set.difference_update(your_set))
print(my_set)
print(my_set.intersection(your_set)) #my_set & your_set
print(my_set.isdisjoint(your_set))
print(my_set.issubset(your_set))
print(my_set.union(your_set)) # my_set | your_set
print(my_set.issuperset(your_set))