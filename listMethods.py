basket = ['a','b','c','d','e','f','g','h','k']

print(basket.sort()) #no return bcos we're not printing it 
basket = ['z','x','a','b','c','d','e','f','g','h','k']
basket.sort()
print(basket)# prints a sorted list 

#using builtinn func sorted 
print(sorted(basket)) # prints a new copy but do not change original

# sorted is a shorthand for assigning and printing a new formatted value
basket = ['z','x','a','b','c','d','e','f','g','h','k']
new_basket = basket[:] # basket.copy = basket[:]
new_basket.sort()
print(new_basket)
print(basket)
#to reverse a list 
basket.reverse()
print(basket) # it doesnt sort but switches the indexes
