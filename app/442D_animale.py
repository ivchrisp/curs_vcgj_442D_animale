from flask import Flask
import lib.biblioteca_animale

app = Flask(__name__)

print ('442D_animale')

@app.route("/pisica", methods = ['GET'])
def obtine_pisica():
    ret = "<h1>Pisica:<h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_animale.culoare_pisica()
    ret += "<br>"

    ret += "<b>Hrana: </b>"
    ret += lib.biblioteca_animale.hrana_pisica()
    ret += "<br>"

    ret += "<b>Invelis corp: </b>"
    ret += lib.biblioteca_animale.invelis_pisica()
    ret += "<br>"

    return ret

@app.route("/pisica/culoare", methods = ['GET'])
def obtine_culoare_pisica():
    ret = ""
    ret += lib.biblioteca_animale.culoare_pisica()
    return ret

@app.route("/pisica/hrana", methods = ['GET'])
def obtine_hrana_pisica():
    ret = ""
    ret += lib.biblioteca_animale.hrana_pisica()
    return ret

@app.route("/pisica/invelis", methods = ['GET'])
def obtine_invelis_pisica():
    ret = ""
    ret += lib.biblioteca_animale.invelis_pisica()
    return ret

app.run(host = "127.0.0.1", port = 5001)
