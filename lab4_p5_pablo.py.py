import re
p= input("Enter your password")
x = True
while x:
    if (len(p)<7):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[!@#$%^&*]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("The password is secure.")
        x=False
        break

if x:
    print("Password is not secure, please try again.")
