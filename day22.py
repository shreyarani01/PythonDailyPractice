#Map

students = [
    {"name": "Jacob Martin",
    "father name" : "Ros Martin",
    "Address": "123 Hill Street"},

    {"name" : "Angela Stevens",
    "father name": "Robert Stevens",
    "Address": "3 Upper Street London"},
    
    {"name" : "Ricky Smart",
    "father name": "William Smart",
    "Address" : "Unknown"},
    ]

print(list(map(lambda student: student['name'],students)))

# Filter:
L = [1,2,3,4,5,6,7]
print(list(filter(lambda x: x>4 , L)))