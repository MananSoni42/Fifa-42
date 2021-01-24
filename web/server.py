from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

player_queue = []

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/game", methods=['POST'])
def game():
    return render_template('game.html')

if __name__ == "__main__":
    app.run(debug=True)
