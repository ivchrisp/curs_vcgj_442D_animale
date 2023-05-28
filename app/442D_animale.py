from flask import Flask
import lib.biblioteca_animale
app=Flask(__name__)
print('442D_animale')

'''
 ------------------------------------
    #4 CONSTANTINESCU CATALIN - capra
 ------------------------------------
'''

@app.route("/capra", methods=['GET'])
def obtine_capra():
    ret = "<h1>capra:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_animale.culoare_capra()
    ret += "<br>"

    ret += "<b>hrana: </b>"
    ret += lib.biblioteca_animale.hrana_capra()
    ret += "<br>"

    ret += "<b>invelisul_corpului: </b>"
    ret += lib.biblioteca_animale.invelisul_corpului_capra()
    ret += "<br>"

    print("DBG: apel obtine_capra")
    return ret

@app.route("/capra/culoare", methods=['GET'])
def obtine_culoare_capra():
    ret = ""
    ret += lib.biblioteca_animale.culoare_capra()
    return ret

@app.route("/capra/hrana", methods=['GET'])
def obtine_hrana_capra():
    ret = ""
    ret += lib.biblioteca_animale.hrana_capra()
    return ret

@app.route("/capra/invelisul_corpului", methods=['GET'])
def obtine_invelisul_corpului_capra():
    ret = ""
    ret += lib.biblioteca_animale.invelisul_corpului_capra()
    return ret

app.run(host = "127.0.0.1", port = 5002)

