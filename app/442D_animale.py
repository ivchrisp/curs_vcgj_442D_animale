from flask import Flask
import lib.biblioteca_animale
app=Flask(__name__)
print('442D_animale')

@app.route("/puma", methods=['GET'])
def obtine_puma():
    ret = "<h1>puma:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_animale.culoare_puma()
    ret += "<br>"

    ret += "<b>hrana: </b>"
    ret += lib.biblioteca_animale.hrana_puma()
    ret += "<br>"

    ret += "<b>invelisul_corpului: </b>"
    ret += lib.biblioteca_animale.invelisul_corpului_puma()
    ret += "<br>"

    print("DBG: apel obtine_puma")
    return ret

@app.route("/puma/culoare", methods=['GET'])
def obtine_culoare_puma():
    ret = ""
    ret += lib.biblioteca_animale.culoare_puma()
    return ret

@app.route("/puma/hrana", methods=['GET'])
def obtine_hrana_puma():
    ret = ""
    ret += lib.biblioteca_animale.hrana_puma()
    return ret

@app.route("/puma/invelisul_corpului", methods=['GET'])
def obtine_invelisul_corpului_puma():
    ret = ""
    ret += lib.biblioteca_animale.invelisul_corpului_puma()
    return ret

app.run(host = "127.0.0.1", port = 5002)


