from flask import Flask, request
from ie_titanic_utils.str_utils import extract_title

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name")
    if name:
        return f"Hey there {name}!"
    else:
        return "Hey!"

@app.route("/extract_title")
def do_extract_title():
    name = request.args.get("name")
    separator = request.args.get("separator",".")
    if name:
        title = extract_title(name,separator=separator)
        return {"title":title, "original_name": name}
    else:
        return {"error": "No name given"},400


