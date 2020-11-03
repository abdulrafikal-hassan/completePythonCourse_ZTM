# Scope - what variables do I have access to ?

a = 1

def confussion():
    a = 5
    return a 

print(confussion())
print(a)

#Rules for scopes
# 1 - Start with local scope 
# 2 - Parent local scope
# 3 - Global Scope
# 4 - Built in Python funcntions