from flask import Flask, render_template, Response, request, send_from_directory,jsonify,send_file
import PokeApi
import Ui
import cv2
from time import sleep
from os import geteuid

app = Flask(__name__)
path = "".join(x+"/" for x in __file__.split("/")[:-1])
isSudo = geteuid() == 0

def GetPath(name):
    return path+"/"+name

# Default path of the website
@app.route('/')
def index():
    return render_template('index.html') 

@app.route("/pokemon.ttf")
def font():
    return send_file(path+"/pokemon.ttf", as_attachment=True) 


# Takes the generated PokedexWindow image and encoding its png then renders it and sends it back to the clients
def gen(): 
    while True:
        sleep(.5)
        if PokeApi.imgpix.any():
            _,jpg =  cv2.imencode(".png",cv2.imread(GetPath("PokedexWindow.png")))
            frame = jpg.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')
                
@app.route('/pokemon')
def pokemon():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

# If the user Puts a number it will go to PokeApi to get the info and update things
@app.route("/Number/<number>")
def Number(number):
    if PokeApi.GetPokemonInfo(number):
        Ui.UpdateUI()
        return jsonify(result="Valid")
    return jsonify(result="NotValid")


# Changes the color of the pokemon
@app.route("/R/<c>")
def R(c):
    if c.isdigit() and int(c) > -1 and int(c) < 4:
        PokeApi.Color[0] = int(c)
        PokeApi.CreateImage()
        Ui.UpdateUI()
        return jsonify(result="Correct")
    return jsonify("Not correct")

@app.route("/G/<c>")
def G(c):
    if c.isdigit() and int(c) > -1 and int(c) < 4:
        PokeApi.Color[1] = int(c)
        PokeApi.CreateImage()
        Ui.UpdateUI()
        return jsonify(result="Correct")
    return jsonify("Not correct")

@app.route("/B/<c>")
def B(c):
    if c.isdigit() and int(c) > -1 and int(c) < 4:
        PokeApi.Color[2] = int(c)
        PokeApi.CreateImage()
        Ui.UpdateUI()
        return jsonify(result="Correct")
    return jsonify("Not correct")

# If the code is being ran at the highest level it is port 80 else 5000
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=isSudo and "80" or "5000")