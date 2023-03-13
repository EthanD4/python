"""
Ethan Doherty 00312960
mini project 2
this is user creation program
"""
import random
from datetime import datetime

def AccountCreation():
    FN = input("Enter your first name: ")
    LN = input("Enter your last name: ")
    savedUsername = createUser(FN, LN)
    userPassword = input("Enter a password: ")
    while (True):
        validPass = passwordCheck(userPassword)
        reEnter = input("Re-enter your password: ")
        if (validPass == reEnter):
            break
        else:
            userPassword = input("Passwords didn't match!\nEnter a password: ")
        
    encryptedPass = encryptPassword(validPass)
    f = open("users.txt", 'a')
    f.write(savedUsername + "::" + encryptedPass + '\n')
    f.close()

    f = open("log.txt", 'a')
    f.write(savedUsername + " :: " + str(datetime.now()) + " :: " + "NEW\n")
    f.close()

    print("Account created successfully!")
    
    
    

def createUser(FN, LN):
    firstletterFN = FN[0]
    username = firstletterFN + LN + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
    print("Your username is " + username)
    return username

def passwordCheck(userPassword):
    special_chars = ['!', '@', '$', ':', '?']

    while (True):
        if len(userPassword) < 7:
            print("Bad password, too short (must be longer than 7 characters)")
            userPassword = input("Enter a password: ")
        else:
            for char in special_chars:
                if userPassword.find(char) > -1:
                    print("Bad password,  no special chars allowed (!@$:?)")
                    userPassword = input("Enter a password: ")
                else:
                    return userPassword
    


def encryptPassword(password):
    special_chars_dict = {'i': '!', 'a': '@', 'S': '$', 'J': '?'} 
    ePassword = ''
    ePassword += password[-1]
    ePassword +=  password[1:-1]
    ePassword += password[0]

    for i in range(len(ePassword)):
        if ePassword[i] in special_chars_dict.keys():
            ePassword = ePassword[:i] + special_chars_dict[ePassword[i]] + ePassword[i+1:]

    return(ePassword)



def LogIn():
    username = input("Enter your username: ")
    f = open("users.txt", 'r')
    users = f.read().splitlines()
    userExists = False
    
    for u in users:
        if u.split("::")[0] == username:
            fileUser = u.split("::")[0]
            filePass = u.split("::")[1]
            userExists = True
            break
    f.close()
    
    if userExists == False:
        print("This user does not exist!")
        AccountCreation()
    else:
        password = input("Enter your password: ")
        while (True):
            reEnter = input("Re-enter your password: ")
            if (password == reEnter):
                break
            else:
                password = input("Passwords didn't match!\nEnter a password: ")

        ePass = encryptPassword(password)
        f = open("log.txt", 'a')
        if filePass == ePass:
            print(f"You have logged in {username}!\n")
            f.write(username + " :: " + str(datetime.now()) + " :: " + "OK\n")
        else:
            print("Incorrect password, goodbye!")
            f.write(username + " :: " + str(datetime.now()) + " :: " + "BAD PASS\n")
        f.close()
    


if __name__ == "__main__":
    choice = input("are you 'logging in' or 'creating an account?'. Type your choice here: ")
    if choice == "creating an account":
        AccountCreation()
    if choice == "logging in":
        LogIn()

#https://docs.python.org/3/library/datetime.html
