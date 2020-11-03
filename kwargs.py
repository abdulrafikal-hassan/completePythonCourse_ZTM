# *args  **kwargs

def super_func(*args):
    print(args)
    return sum(args)

print(super_func(1,2,3,4,5))

def super(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super(1,2,3,4,5, num=9, num1= 10))

#Rule: params, *args, default parameters, **kwargs
# eg. def func(param,*args,defaultParams,**kwargs)