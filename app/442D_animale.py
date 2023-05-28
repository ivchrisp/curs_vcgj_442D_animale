from flask import Flask
import lib.biblioteca_animale
app=Flask(__name__)
print('442D_animale')

'''
 ------------------------------------
    Gruianu Valentina - frenchbulldog
 ------------------------------------
'''

@app.route("/frenchbulldog", methods=['GET'])
def obtine_frenchbulldog():
    ret = "<h1>frenchbulldog:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_animale.culoare_frenchbulldog()
    ret += "<br>"

    ret += "<b>hrana: </b>"
    ret += lib.biblioteca_animale.hrana_frenchbulldog()
    ret += "<br>"

    ret += "<b>invelisul_corpului: </b>"
    ret += lib.biblioteca_animale.invelisul_corpului_frenchbulldog()
    ret += "<br>"

    print("DBG: apel obtine_frenchbulldog")
    return ret

@app.route("/frenchbulldog/culoare", methods=['GET'])
def obtine_culoare_frenchbulldog():
    ret = ""
    ret += lib.biblioteca_animale.culoare_frenchbulldog()
    return ret

@app.route("/frenchbulldog/hrana", methods=['GET'])
def obtine_hrana_frenchbulldog():
    ret = ""
    ret += lib.biblioteca_animale.hrana_frenchbulldog()
    return ret

@app.route("/frenchbulldog/invelisul_corpului", methods=['GET'])
def obtine_invelisul_corpului_frenchbulldog():
    ret = ""
    ret += lib.biblioteca_animale.invelisul_corpului_frenchbulldog()
    return ret

app.run(host = "127.0.0.1", port = 5002)

