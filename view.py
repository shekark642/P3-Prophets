from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, url_for, __init__




import os
#yurrrrrr
#yolo
# create a Flask instance
app = Flask(__name__)

# connects default URL of server to a python function
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/leaderboards')
def leaderboards():
    return render_template("leaderboards.html")

@app.route('/blackjack')
def blackjack():
    return render_template("blackjack.html")

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True)

