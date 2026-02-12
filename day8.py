#set + tuples

t = (1, 2, 3, 2, 4, 2)

print("first element: ", t[0])
print("last element", t[-1])
print("length of t: " , len(t))

count =0
for i in t:
    if i == 2:
        count = count+1
print("occurence of 2: ", count)

print("unique elements: ", set(t))