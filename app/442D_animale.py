from flask import Flask
import lib.biblioteca_animale
app=Flask(__name__)
print('442D_animale')

'''
 ------------------------------------
    #2 Popescu Andrei 442D- castor
 ------------------------------------
'''

@app.route("/castor", methods=['GET'])
def obtine_castor():
    ret = "<h1>castor:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_animale.culoare_castor()
    ret += "<br>"

    ret += "<b>hrana: </b>"
    ret += lib.biblioteca_animale.hrana_castor()
    ret += "<br>"

    ret += "<b>invelisul_corpului: </b>"
    ret += lib.biblioteca_animale.invelisul_corpului_castor()
    ret += "<br>"

    print("DBG: apel obtine_castor")
    return ret

@app.route("/castor/culoare", methods=['GET'])
def obtine_culoare_castor():
    ret = ""
    ret += lib.biblioteca_animale.culoare_castor()
    return ret

@app.route("/castor/hrana", methods=['GET'])
def obtine_hrana_castor():
    ret = ""
    ret += lib.biblioteca_animale.hrana_castor()
    return ret

@app.route("/castor/invelisul_corpului", methods=['GET'])
def obtine_invelisul_corpului_castor():
    ret = ""
    ret += lib.biblioteca_animale.invelisul_corpului_castor()
    return ret

app.run(host = "127.0.0.1", port = 5002)
