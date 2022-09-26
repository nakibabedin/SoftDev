'''
Charles's Angels::Aleksandra Shifrina, Nakib Abedin, Ameer Alnasser
SoftDev pd08
K04 -- RNG + Dictionaries
2022-09-22
time spent: 0.5hrs
DISCO:
    *figured out that .keys() returns all keys of a dictionary  
    *figured out typecasting. ex: int(4.0)
    *figured out general solution for returning a random devo 
QCC:
    *will the final dictionary work with our code?
    *how do we ensure that the code will completely randomly chose a devo?
OPS Summary:
    1. gather all keys from dictionary in a list, keys
    2. pick a random index using length of list
    3. retrieve key from list
    4. generate a random element from list associated with key
    5. return random devo
'''

import random as rng
from re import I, M

#krewes = {1:['A', 'B', 'C'], 2:['D', 'E', 'F']}
krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"], 
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
         }


# def find_devo(krewes):
#     keys = list(krewes)
#     index = rng.randint(0, len(keys)-1)
#     key = keys[index]
#     rando_value = rng.randint(0, len(krewes[key])-1)
#     return "The devo you picked is " + krewes[key][rando_value] + " in period " + str(key)

def find_devo(krewes):
    keys = list(krewes)
    index = rng.randint(0, len(keys)-1)
    key = keys[index]
    rando_value = rng.randint(0, len(krewes[key])-1)
    return krewes[key][rando_value]

def find_devo_pd(krewes):
    print("Which period do you want a random devo from?")
    pd = int(input())
    if(pd != 2 and pd != 7 and pd != 8):
        print("GG.")
    rando_value = rng.randint(0, len(krewes[pd])-1)
    return "The devo you picked is " + krewes[pd][rando_value] + " from your chosen period " + str(pd)

def find_devo_hangman(krewes):
    devo = find_devo(krewes)
    name = list(devo)
    temp = []
    counter = 0
    while(True): 
        string = ""
        for i in range(len(name)):
                if name[i] not in temp:
                    string += "_ "
                else:
                    string += name[i] + " "
        print(string)
        print("Guess a letter")
        print(name)
        guess = input().upper()
        if guess not in name:
            counter += 1 
            print(" You dumb bro. Number of incorrect guesses: " + str(counter))
            print("Guesses remaining ")
        else: #if guess is correct
            temp.append(guess)
        if(string == devo ):
            break
    print("you have won the game")

# print("Which of the following methods do you want to run?")
# print("0: find a random devo from any period")
# print("1: find a random devo from a period of your choice")    
# program = int(input())
# if(program == 0):
#     print(find_devo(krewes))
#     input
# elif(program == 1):
#     print(find_devo_pd(krewes))

print(find_devo_hangman(krewes))
    



    
