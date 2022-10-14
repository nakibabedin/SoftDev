# Team Brown: Nakib Abedin, Eric Sohel, Shafiul Haque
# SoftDev pd08
# K10: Just Plug It In
# 2022-10-13
# time spent: 0.2hrs

from flask import Flask, render_template #Q0: What will happen if you remove render_template from this line? (log your prediction before you pull the trigger...)
# the app route for my foist template wouldn't load
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template") #Q1: Can all of your teammates confidently predict the URL to use to load this page?
#http://127.0.0.1:5000/my_foist_template
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll) #Q2: What is the significance of each argument? Simplest, most concise answer best.
    # the first argument is the template that the app route returns
    # second argument sets the page title as the name
    # the third arguments sets the collection is a list of numbers that are printed out as

if __name__ == "__main__":
    app.debug = True
    app.run()
