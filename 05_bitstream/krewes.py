# NADH -- Nakib Abedin, Daniel He
# SoftDev pd08
# K05 -- working with a txt file
# 2022-09-29
# time spent: 

# DISCO:
#   0) you can open and store the contents of a txt file in python using the open method
#   1) the open method returns a file object which can be read using the .read() method
# QCC:
#   0) if dic[s[0]] is none in line 22, would it just return none or will it add something to none
# OPS SUMMARY:
# Populate:
#   0) Open the file and store its contents in a variable
#   1) Use the .split method in order to seperate all of the devos across each period
#   2) Use the .split method again to store the information about each devo in a list 
#   3) Return the populated dictionary
import random

def populate():
    file = open("krewes.txt", "r")
    data = file.read().split("@@@") #the list version of file object
    dic = {} #dictionary to be populated
    for e in data: # loops through a list of lists
        s = e.split("$$$") # splits information so that it becomes seperate elements in a list
        #check, only proceed if dict size >0
        if s[0] in dic: # checks if the key already exists
            dic[s[0]] = dic[s[0]] + [s[1],s[2]]
        else:
            dic[s[0]] = [s[1],s[2]]
    return dic # return populated dictionary
    
def randomName(dic):
    # randomly generates a devo
    periods = list(dic) # list of all the keys
    period = random.choice(periods) # randomly selects a period
    devo = dic[period][0] # the bv first element in the list is the devo
    ducky = dic[period][1] # the second element is the ducky
    return(devo + " from period " + str(period) + " whose ducky is " + ducky)

dictionary = populate()
print(randomName(dictionary))

