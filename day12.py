#even function

def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print("1:")
print(is_even(5))

print("2:")
for i in range (1,11):
    print( is_even(i))