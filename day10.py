#Student marks manager

students = {}
n = int(input("How many students? "))

for i in range(n):
    name, marks = input("Enter name and marks: ").split()
    students[name] = int(marks)

print(students)
