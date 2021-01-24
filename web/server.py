from flask import Flask, render_template, request

import sys
import os
sys.path.append(os.path.abspath('../src'))

from teams.network import NetworkTeam

app = Flask(__name__)

num_players = 0
teams = [None, None]

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/game", methods=['POST'])
def game():
    global num_players, teams
    name = request.form.get('name')
    if name:
        if num_players >= 2:
            return render_template('error.html', message="Already have 2 players in the game")
        else:
            teams[num_players] = NetworkTeam(formation='balanced-1', color=(0, 32, 255))
            num_players += 1
            return render_template('game.html')
    else:
        return render_template('error.html', message="Could not process name")

if __name__ == "__main__":
    app.run(debug=True)
