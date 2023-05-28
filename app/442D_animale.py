from flask import Flask
import lib.biblioteca_animale
app=Flask(__name__)
print('442D_animale')
'''
------------------------------------
 BAJENARU_ALEXANDRU 422D - leu
------------------------------------
'''
@app.route("/leu", methods=['GET']) # Defines a route for GET requests to "/leu"
def obtine_hamster(): # Defines a function that will be called when the route is accessed
 ret = "<h1>leu:</h1>"
 ret += "<b>Culoare: </b>"
 ret += lib.biblioteca_animale.culoare_leu() # Calls a function from the biblioteca_animale library
 ret += "<br>"
 ret += "<b>hrana: </b>"
 ret += lib.biblioteca_animale.hrana_leu() # Calls a function from the biblioteca_animale library
 ret += "<br>"
 ret += "<b>invelisul_corpului: </b>"
 ret += lib.biblioteca_animale.invelisul_corpului_leu() # Calls a function from the biblioteca_animale library
 ret += "<br>"
 print("DBG: apel obtine_leu") # Prints a debug message
 return ret # Returns the built HTML string
@app.route("/leu/culoare", methods=['GET']) # Defines a route for GET requests to "/leu/culoare"
def obtine_culoare_leu(): # Defines a function that will be called when the route is accessed
 ret = ""
 ret += lib.biblioteca_animale.culoare_leu() # Calls a function from the biblioteca_animale library
 return ret # Returns the result of the function
# The following two functions are similar to the one above, but for different routes
@app.route("/leu/hrana", methods=['GET'])
def obtine_hrana_leu():
 ret = ""
 ret += lib.biblioteca_animale.hrana_leu()
 return ret
@app.route("/leu/invelisul_corpului", methods=['GET'])
def obtine_invelisul_corpului_leu():
 ret = ""
 ret += lib.biblioteca_animale.invelisul_corpului_leu()
 return ret
app.run(host = "127.0.0.1", port = 5002)
