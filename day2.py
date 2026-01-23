'''Number analyzer'''

numbers = []
n = int(input("Enter number you wanna insert: "))
for i in range(n):
    n = int(input("Enter the numbers " + str(i+1) + ":"))
    numbers.append(n)

print("numbers in it: ", numbers)
print("sum of numbers: ", sum(numbers))
print("maximum of numbers: ", max(numbers))
print("sorted list: ", sorted(numbers))