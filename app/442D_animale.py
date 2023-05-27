from flask import Flask

app = Flask(__name__)

print ('442D_animale')

@app.route("/", methods = ['GET'])
def index():
    ret = "<h1></h1>Informatii despre animale 442D</h1>
    return ret
    
@app route("/iepure", methods = ['GET'])
def get_iepure():
    ret = "<h1>Iepure<h1>"
    ret += "Culoare: "
    ret += lib.biblioteca_animale.culoare_iepure()
    ret += "<br>"
    
    ret += "Hrana: "
    ret += lib.biblioteca_animale.hrana_iepure()
    ret += "<br>"
    
    ret += "Invelis corp: "
    ret += lib.biblioteca_animale.invelis_iepure()
    ret += "<br>"
    
    return ret
    
@app.route("/iepure/culoare", methods = ['GET'])
def ia_culoare_iepure():
    ret = ""
    ret += lib.biblioteca_animale.culoare_iepure()
    
    return ret
    
@app.route("/iepure/hrana", methods = ['GET'])
def ia_hrana_iepure():
    ret = ""
    ret += lib.biblioteca_animale.hrana_iepure()
    
    return ret
    
@app.route("/iepure/invelis", methods = ['GET'])
def ia_culoare_iepure():
    ret = ""
    ret += lib.biblioteca_animale.invelis_iepure()
    
    return ret

