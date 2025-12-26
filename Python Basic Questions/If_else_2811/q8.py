# Q8 Write a program that checks if a username and password entered by the user match the pre-set values
# username = "admin" and password = "1234". If both match, print "Login Successful", otherwise print
# "Login Failed".


username = "admin"
password = "1234"

user_name = input("Enter username: ")
user_password = input("Enter password: ")

if user_name == username and user_password == password:
    print("Login Successful")
else:
    print("Login Failed")
