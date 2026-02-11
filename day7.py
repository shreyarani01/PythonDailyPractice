# email username checker

email = input("Enter you e-mail: ")
username = []

for ch in email:
    if ch == '@':
        break
    username.append(ch)
if '@' not in email:
    print("Invalid email!")
elif len(username) == 0:
   print("Invalid username")
else:
    print("Username is: ","".join(username))