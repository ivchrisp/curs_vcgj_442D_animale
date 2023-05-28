from flask import Flask
import lib.biblioteca_animale
app=Flask(__name__)
print('442D_animale')

'''
 ------------------------------------
    #2 Danescu Mihai-Cosmin-442D - veverita
 ------------------------------------
'''

@app.route("/veverita", methods=['GET'])
def obtine_veverita():
    ret = "<h1>veverita:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_animale.culoare_veverita()
    ret += "<br>"

    ret += "<b>hrana: </b>"
    ret += lib.biblioteca_animale.hrana_veverita()
    ret += "<br>"

    ret += "<b>invelisul_corpului: </b>"
    ret += lib.biblioteca_animale.invelisul_corpului_veverita()
    ret += "<br>"

    print("DBG: apel obtine_veverita")
    return ret

@app.route("/veverita/culoare", methods=['GET'])
def obtine_culoare_veverita():
    ret = ""
    ret += lib.biblioteca_animale.culoare_veverita()
    return ret

@app.route("/veverita/hrana", methods=['GET'])
def obtine_hrana_veverita():
    ret = ""
    ret += lib.biblioteca_animale.hrana_veverita()
    return ret

@app.route("/veverita/invelisul_corpului", methods=['GET'])
def obtine_invelisul_corpului_veverita():
    ret = ""
    ret += lib.biblioteca_animale.invelisul_corpului_veverita()
    return ret

app.run(host = "127.0.0.1", port = 5002)
