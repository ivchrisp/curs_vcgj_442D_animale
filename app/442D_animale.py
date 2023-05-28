from flask import Flask
import lib.biblioteca_animale
app=Flask(__name__)


@app.route("/lenes", methods=['GET'])
def obtine_lenes():
    ret = "<h1>lenes:</h1>"
    ret += "<b>Culoare: </b>"
    ret += lib.biblioteca_animale.culoare_lenes()
    ret += "<br>"

    ret += "<b>Hrana: </b>"
    ret += lib.biblioteca_animale.hrana_lenes()
    ret += "<br>"

    ret += "<b>Invelisul corpului: </b>"
    ret += lib.biblioteca_animale.invelisul_corpului_lenes()
    ret += "<br>"

    return ret

@app.route("/lenes/culoare", methods=['GET'])
def obtine_culoare_lenes():
    ret = ""
    ret += lib.biblioteca_animale.culoare_lenes()
    return ret

@app.route("/lenes/hrana", methods=['GET'])
def obtine_hrana_lenes():
    ret = ""
    ret += lib.biblioteca_animale.hrana_lenes()
    return ret

@app.route("/lenes/invelisul_corpului", methods=['GET'])
def obtine_invelisul_corpului_lenes():
    ret = ""
    ret += lib.biblioteca_animale.invelisul_corpului_lenes()
    return ret

app.run(host="127.0.0.1", port=5002)
