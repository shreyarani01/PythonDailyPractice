#email and password checker

email = input("Enter your email: ")

if '@' not in email:
    print("Email is incorrect")

elif email == "soya@gmail.com":
    num_of_attempts = 0

    while num_of_attempts < 3:
        password = input("Enter your password: ")

        if password == "4852":
            print("Welcome ")
            break
        else:
            num_of_attempts += 1
            print("Wrong password")

    if num_of_attempts == 3:
        print("Account Locked due to multiple incorrect trials :(")

else:
    print("Invalid credentials")
