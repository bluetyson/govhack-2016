from flask import Flask, render_template, jsonify

from hansard.parsing import HansardParser

app = Flask(__name__)


HANSARD_DATA = "sample.xml"

@app.route("/markovstuff")
def get_markov():
    markov_stuff = HansardParser().parse(HANSARD_DATA)
    json_dict = []
    for i in markov_stuff:
        tmp = {}
        tmp["type"] = "talk"
        tmp["content"] = i.content
        tmp["politician_id"] = -1
        json_dict.append(tmp)

    return jsonify(json_dict)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
