from flask import Flask, render_template, request
from flask_socketio import SocketIO
import json
import atexit
import time

import sys
import os
sys.path.append(os.path.abspath('../src'))

from teams.network import NetworkTeam
from game import Game
from settings import *

app = Flask(__name__)
app.secret_key = "fifa-42"
socketio = SocketIO(app)

name1, team1 = None, None
name2, team2 = None, None
inter = None

def send_network_state(state):
    network_state = {
        'W': W, 'H': H,
        'name1': name1, 'name2': name2,
        'ball': state["ball"].pos.val,
        'team1': {
            'pos': [p.pos.val for p in state['team1']['players']]
        },
        'team2': {
            'pos': [p.pos.val for p in state['team2']['players']]
        }
    }
    with app.test_request_context():
        socketio.emit('next', {'state': network_state}, broadcast=True)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/game", methods=['POST'])
def show_game():
    global game, inter, team1, team2, name1, name2
    name = request.form.get('name')
    if name:
        if not team1:
            team1 = NetworkTeam(formation='balanced-1', color=(0, 32, 255))
            name1 = name
            print(f'Added team1 with name {name1}')
            return render_template('game.html', name=name, next=False)
        elif not team2:
            team2 = NetworkTeam(formation='defensive-3', color=(0, 32, 255))
            name2 = name
            print(f'Added team2 with name {name2}')

            print(f'Starting game')
            game = Game(team1, team2, sound=False, difficulty=0, cam='full')

            return render_template('game.html', name=name, next=True)
        else:
            return render_template('error.html', message="Already have 2 players in the game")
    else:
        return render_template('error.html', message="Could not process name")

@socketio.on("move")
def move_player(data):
    name = data['name']
    key = data['key']
    if name.lower() == name1:
        print(f'{name} pressed {key}')
        team1.register_keystroke(key)
    elif name.lower() == name2:
        team2.register_keystroke(key)
        print(f'{name} pressed {key}')
    else:
        raise Exception(f'name `{name}` not recognized, choose from `{name1}` or `{name2}`')

@socketio.on("get_next")
def game_next(data):
    if game:
        game.next()
        send_network_state(game.get_state())

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    #atexit.register(inter.cancel)
    socketio.run(app, debug=True)
