#lists is a collection of items 
# lists is a forom of arrays in python language

l = [1,2,3,4,5,6]
l2 = ['a',2,4,'e']
l3 = ['books', 'shirts','food']

print(l3[2])
print(l[1::2])

#lists are mutable = can be changed 
#to copy a list 
new_list = l3[:]
new_list[0] = 'new item '
print(new_list)
print(l3[:])

#list methods 

basket = [1,2,3,4,5]

#the length
print(len(basket))

#adding
basket.append(10000)
print(basket)

basket.insert(4, 30000)

basket.extend([20])
print(basket)

#removing from the end of the list or using the index to remove a value
basket.pop() ## for pop() it returns the value
print(basket)

#looking or searching for items in lists 
print(3 in basket)


#clearing or emptying a list 
# basket.clear() // emptys the list
print(basket)

basket = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

print(basket.index('f'))

print('e' in basket)  # True
print(basket.count('c'))# its only 1 c in basket
