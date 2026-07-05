from getpass import getpass

attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = getpass("Enter password: ")

    if username == "admin" and password == "admin123":
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        attempts += 1

if attempts == 3:
    print("Account Locked")