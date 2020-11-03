#Exercise: Check for duplicates in list
some_list = ['a','b','c','d','e','f','c','h','h','j','k']

double = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in double:
            double.append(value)

print(double)
