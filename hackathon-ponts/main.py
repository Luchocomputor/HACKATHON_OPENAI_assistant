from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from src.utils.ask_question_to_pdf import (
    ask_question_to_pdf,
    gpt3_completion,
    open_file,
    read_pdf,
    split_text,
)

# BONJOUR
app = Flask(__name__)


@app.route("/")
def hello(name=None):
    return render_template("index.html")


@app.route("/prompt", methods=["POST"])
def prompt():
    error = None
    if request.method == "POST":
        msg = request.form["prompt"]
        # Appel de la fonction pour poser la question au PDF
        answer = ask_question_to_pdf(msg)
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return {"answer": answer}
