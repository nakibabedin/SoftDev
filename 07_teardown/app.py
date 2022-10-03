'''
Charles's Angels::Aleksandra Shifrina, Nakib Abedin, Ameer Alnasser
SoftDev pd08
K04 -- RNG + Dictionaries
2022-09-22
time spent: 0.5hrs
'''


from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?



@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(name) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:

QCC:
0.  Line 12 utilized a similar syntax as the java constructor
1.  the forward slash is utilized when we navigate directories
2.  the output will be printed inside of the directory with the app, with the #3 name from the constructor
4.  It will not appear anywhere because we never run the hello_world() function
5.  java also has object-oriented programming, as seen on line 21 wih the call of a method from app  
...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
