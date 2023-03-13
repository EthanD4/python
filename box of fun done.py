"""
Ethan Doherty 00312960
box of fun
this is the box of fun with mad lib, fortune teller and a knock knock joke.
""" 

import math
import time
#import random as r
from random import randint #as rndI
#import from random as spinner


def Menu():
    print("Which game would you like to play? Fortune teller, Knock Knock Joke or Mad Lib")
    choice = str.casefold(input())
    if choice == "fortune teller":
        fortuneTeller()     
    elif choice == "knock knock joke" :
        Knock()
    elif choice == "mad lib" :
        MadLib()   
    else:
        print("open which?")
        Menu()
    
def fortuneTeller():
    print("Welcome to Fortune Teller. Please ask your question")
    ranNum = randint(1, 6)
    question = input()
    if ranNum == 1:
        print(question + "? yes")
    elif ranNum == 2:
        print(question + "? no")
    elif ranNum == 3:
        print(question + "? maybe")
    elif ranNum == 4:
        print(question + "? try again later")
    elif ranNum == 5:
        print(question + "? no chance")
    elif ranNum == 6:
        print(question + "? absolutley")
    time.sleep(3)
    print("would you like to play another game?")
    playAgain=str.casefold(input())
    if playAgain == "yes":
        Menu()
    else:
        print("goodbye")
    
def Knock():
    print("this is the Knock Knock Joke game... Knock Knock")
    response1 = str.casefold(input())
    if response1 == "who's there?" or "who is there?" "who's there" or "who is there":
        print("Beets")
        response2 = input()
    else:
        print("thats not how this works")     
    if response2 == "beets who" or "beets who?":
        print("beets me!")
    time.sleep(3)
    print("would you like to play another game?")
    playAgain=str.casefold(input())
    if playAgain == "yes":
        Menu()
    else:
        print("goodbye")
    
def MadLib():
    print("welcome to the mad lib game. First give me a noun")
    noun1 = input()
    print("Now a noun that is a place...")
    noun2 = input()
    print("Another noun...")
    noun3 = input()
    print("Another noun...")
    noun4 = input()
    print("last noun...")
    noun5 = input()
    print("Now give me a past tense verb")
    verb1 = input()
    print("one more verb...")
    verb2 = input()
    print("Now give me an adjective")
    adjective1 = input()
    print("Finaly, give me one more adjective")
    adjective2 = input()
    print("the " + adjective1 + " " + noun1 + " " + verb1 + " toward the " + noun2 + " with a pack of " + adjective2 + " " + noun3 + " when a " + noun4 + " " + verb2 + " over their " + noun5)
    time.sleep(3)
    print("would you like to play another game?")
    playAgain=str.casefold(input())
    if playAgain == "yes":
        Menu()
    else:
        print("goodbye")
def main():
    print("welcome to Ethan's Box of Fun!")
    input("Press Enter to continue")
    Menu()
main()

"""
sources
https://stackoverflow.com/questions/983354/how-do-i-wait-for-a-pressed-key
https://stackoverflow.com/questions/50192965/how-to-make-user-input-not-case-sensitive
https://realpython.com/python-sleep/
https://www.goodhousekeeping.com/life/parenting/g36198919/knock-knock-jokes-for-kids/?utm_source=google&utm_medium=cpc&utm_campaign=arb_ga_ghk_d_bm_prog_org_usx_g36198919&gclid=Cj0KCQjw1vSZBhDuARIsAKZlijQYsIW1RqYzjzch_F5ImSLLaznO6nGol43t2B3t3eIbWhoIBZhhXWMaAsbiEALw_wcB
http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
https://www.programiz.com/python-programming/type-conversion-and-casting
https://www.w3schools.com/python/python_while_loops.asp
"""