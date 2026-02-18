#sum check using highest order function

def sum(funct, L):
    result = 0
    for i in L:
        if funct(i):
            result = result+i
    return result

L=[11,14,21,23,56,78,45,29,28]

x = lambda x: x%2 == 0 
y = lambda y: y%2 != 0
z = lambda z: z%3 == 0

print(sum(x,L))
print(sum(y,L))
print(sum(z,L))