from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story
app = Flask(__name__)
app.config['SECRET_KEY'] = "key"

debug = DebugToolbarExtension(app)


@app.route("/")
def show_prompt():
    return render_template("prompt-form.html", prompts=story.prompts)


@app.route("/madlib")
def show_madlib():
    madlib = story.generate(request.args)
    return render_template("show_madlib.html", madlib=madlib)
