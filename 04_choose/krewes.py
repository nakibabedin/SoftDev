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
    *why does ameer suck at coding?
    *how do we ensure that the code will completely randomly chose a devo?
OPS Summary:
    1. gather all keys from dictionary in a list, keys
    2. pick a random index using length of list
    3. retrieve key from list
    4. generate a random element from list associated with key
    5. return random devo
'''

import random as rng

krewes = {1:['A', 'B', 'C'], 2:['D', 'E', 'F']}
def find_devo(krewes):
    keys = list(krewes.keys())
    index = rng.randint(0, len(keys)-1)
    key = keys[index]
    rando_value = rng.randint(0, len(krewes[key])-1)
    return krewes[key][rando_value]

print(find_devo(krewes))
    
    
