#identity check
a = [1,2,3]
b = a             #same memory
c = [1,2,3]       #new list, new memory

print("\n 1: ")
print(a == b)
print(a is b)
print(a == c)
print(a is c)

x = 256
y = 256
p = 257
q = 257
print("\n 2: ")
print(x is y)
print(p is q)

lst1 = [1, 2]
lst2 = lst1

lst2.append(3)
print("\n 3: ")
print(lst1)
print(lst2)

