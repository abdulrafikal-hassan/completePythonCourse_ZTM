# global keyword

a = 10
def conf(b):
    print(b)
    a = 90

conf(3000)

total = 0
def count():
    global total
    total += 1
    return total 

count()
count()
print(count())
# better way dooing the above 

all = 1
def count(all):
    all += 1
    return all

print(count(count(count(all))))

# Non Local  also know as Parent Local

def outer():
    x ="local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("innere: ", x)

    inner()
    print("outer: ",x)

outer()