import requests
import flask
# url = "https://pythonavanzado.techtalents.cloud/halloween"
# response = requests.get(url + "/data") #, params=dta)
# search = response.text
# a = search.find("h") + search.find("A") + search.find("n") + search.find("o") + search.find("W")    
# a+= search.find("L") + search.find("l") + search.find("e") + search.find("E")
# A = "h" in "https://pythonavanzado.techtalents.cloud/halloween"
# dta = {
    # "name" : "That guy",
    # "position" : a
# }
# requests.get(url, params=dta)
# if response.status_code == 200:
    # print(response.text)
app = flask.Flask(__name__)
@app.route("/VAR/<name>")
def VAR(name):
    if name == "Javi":
        return "email me at info@google.com"
    else:
        return flask.redirect("/")
@app.route("/")
def index():
    # name = requests.args.get("name", "World")
    return "Homepage"
app.run(host="0.0.0.0", port = 65535, debug=True)