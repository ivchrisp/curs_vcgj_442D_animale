from flask import Flask
import lib.biblioteca_animale
app=Flask(__name__)
print ('442D_animale')

# BARAN LUIZA - SINSILA

@app.route("/sinsila", methods=['GET'])
def obtine_sinsila():
    ret = "<h1>sinsila:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_animale.culoare_sinsila()
    ret += "<br>"

    ret += "<b>hrana: </b>"
    ret += lib.biblioteca_animale.hrana_sinsila()
    ret += "<br>"

    ret += "<b>invelisul_corpului: </b>"
    ret += lib.biblioteca_animale.invelisul_corpului_sinsila()
    ret += "<br>"

    print("DBG: apel obtine_sinsila")
    return ret

@app.route("/sinsila/culoare", methods=['GET'])
def obtine_culoare_sinsila():
    ret = ""
    ret += lib.biblioteca_animale.culoare_sinsila()
    return ret

@app.route("/sinsila/hrana", methods=['GET'])
def obtine_hrana_sinsila():
    ret = ""
    ret += lib.biblioteca_animale.hrana_sinsila()
    return ret

@app.route("/sinsila/invelisul_corpului", methods=['GET'])
def obtine_invelisul_corpului_sinsila():
    ret = ""
    ret += lib.biblioteca_animale.invelisul_corpului_sinsila()
    return ret

app.run(host = "127.0.0.1", port = 5002)
