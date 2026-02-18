#lambda function
a = lambda x,y: x+y
print("ans: " , a(4,5))

b = lambda x: "Odd" if x%2 == 1  else "even"
print("ans2: " , b(9))

c = lambda x: x[0] == 'a'
print("ans3 ", c("apple"))