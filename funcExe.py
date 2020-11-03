# Returning the highest even from a list using a function

def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0 :
            evens.append(item)
    return max(evens)

print(highest_even([10,12,4,2,3,5,9,40]))

def highest_odd(li):
    odds = []
    for item in li:
        if item % 2 != 0:
            odds.append(item)
    return max(odds)

print(highest_odd([10,12,4,2,3,5,9,40]))