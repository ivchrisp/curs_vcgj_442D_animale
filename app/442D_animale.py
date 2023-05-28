from flask import Flask
import lib.biblioteca_animale

app = Flask(__name__)

print ('442D_animale')

@app.route("/iepure", methods = ['GET'])
def obtine_iepure():
    ret = "<h1>Iepure:<h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_animale.culoare_iepure()
    ret += "<br>"
    
    ret += "<b>Hrana: </b>"
    ret += lib.biblioteca_animale.hrana_iepure()
    ret += "<br>"
    
    ret += "<b>Invelis corp: </b>"
    ret += lib.biblioteca_animale.invelis_iepure()
    ret += "<br>"
    
    return ret
    
@app.route("/iepure/culoare", methods = ['GET'])
def obtine_culoare_iepure():
    ret = ""
    ret += lib.biblioteca_animale.culoare_iepure()
    return ret
    
@app.route("/iepure/hrana", methods = ['GET'])
def obtine_hrana_iepure():
    ret = ""
    ret += lib.biblioteca_animale.hrana_iepure()
    return ret
    
@app.route("/iepure/invelis", methods = ['GET'])
def obtine_invelis_iepure():
    ret = ""
    ret += lib.biblioteca_animale.invelis_iepure()
    return ret

app.run(host = "127.0.0.1", port = 5001)
