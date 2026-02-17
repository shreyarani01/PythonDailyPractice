#multiplication using recursion
def mul(a,b):
    #base condn:
    if b == 1:
        return a
    else:
        return a + mul(a,b-1)
print(mul(3,4))