'''Text analyzer'''

text = input("Enter name: ")
frequency = {} #empty dictionary

for char in text:
    if char != " ":
        if char in frequency:
            frequency[char] +=1
        else:
            frequency[char] =1
print(" character frequency :")
for char, count in frequency.items():
    print(char," = ",count)