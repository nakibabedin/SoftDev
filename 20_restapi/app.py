'''
u2be -- Nakib Abedin, Joseph Jeon
SoftDev
K20 -- Restful APIs
2022-11-21
time spent: 0.7 hrs
'''
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def page():
    x = requests.get("https://api.nasa.gov/planetary/apod?api_key=HXuFz4bCkyUrTLbNRiAEf8C88GNXoCYUvLWHK9LK")
    print(x)
    return render_template('main.html', url="https://apod.nasa.gov/apod/image/2211/Butterfly_HubbleOstling_960.jpg")

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()