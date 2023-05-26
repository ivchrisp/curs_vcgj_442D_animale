from flask import Flask

import lib.biblioteca_animale

app = Flask(__name__)

print('442D_animale')

@app.route("/" , methods=['GET'])
def index():
    ret = "<h1></h1>Informatii despre animale 442D</h1>"
    return ret

@app.route("/caine/", methods=['GET'])
def get_caine():
    ret = "<h1>Caine<h1>"
    ret += "Culoare: "
    ret += lib.biblioteca_animale.culoare_caine()
    ret += "<br>"
    
    ret += "Hrana: "
    ret += lib.biblioteca_animale.hrana_caine()
    ret += "<br>"
    
    ret += "Invelis corp: "
    ret += lib.biblioteca_animale.invelis_caine()
    ret += "<br>"
    
    return ret
    
@app.route("/caine/culoare", methods=['GET'])
def ia_culoare_caine():
    ret = ""
    ret += lib.biblioteca_animale.culoare_caine()
    
    return ret
    
@app.route("/caine/hrana", methods=['GET'])
def ia_hrana_caine():
    ret = ""
    ret += lib.biblioteca_animale.hrana_caine()
    
    return ret
    
@app.route("/caine/invelis", methods=['GET'])
def ia_invelis_caine():
    ret = ""
    ret += lib.biblioteca_animale.invelis_caine()
    
    return ret
    
@app.route("/pantera/", methods=['GET'])
def get_pantera():
    ret = "<h1>Pantera<h1>"
    ret += "Culoare: "
    ret += lib.biblioteca_animale.culoare_pantera()
    ret += "<br>"
    
    ret += "Hrana: "
    ret += lib.biblioteca_animale.hrana_pantera()
    ret += "<br>"
    
    ret += "Invelis corp: "
    ret += lib.biblioteca_animale.invelis_pantera()
    ret += "<br>"
    
    return ret
    
@app.route("/pantera/culoare", methods=['GET'])
def ia_culoare_pantera():
    ret = ""
    ret += lib.biblioteca_animale.culoare_pantera()
    
    return ret
    
@app.route("/pantera/hrana", methods=['GET'])
def ia_hrana_pantera():
    ret = ""
    ret += lib.biblioteca_animale.hrana_pantera()
    
    return ret
    
@app.route("/pantera/invelis", methods=['GET'])
def ia_invelis_pantera():
    ret = ""
    ret += lib.biblioteca_animale.invelis_pantera()
    
    return ret
    
    
app.run(host = "127.0.0.1", port = 5001)
