from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
import json
import threading
import atexit
import time, threading

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

class setInterval :
    def __init__(self,interval,action) :
        self.interval=interval
        self.action=action
        self.stopEvent=threading.Event()
        thread=threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self) :
        nextTime=time.time()+self.interval
        while not self.stopEvent.wait(nextTime-time.time()) :
            nextTime+=self.interval
            self.action()

    def cancel(self) :
        self.stopEvent.set()

def send_network_state(state):
    network_state = {
        'W': W, 'H': H, 'ball': state["ball"].pos.val,
        'team1': {
            'pos': [p.pos.val for p in state['team1']['players']]
        },
        'team2': {
            'pos': [p.pos.val for p in state['team2']['players']]
        }
    }
    with app.test_request_context():
        emit('next', {'state': network_state}, broadcast=True)

def game_next():
    game.next()
    send_network_state(game.get_state())

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
            return render_template('game.html', name=name)
        elif not team2:
            team2 = NetworkTeam(formation='balanced-1', color=(0, 32, 255))
            name2 = name
            print(f'Added team2 with name {name2}')

            game = Game(team1, team2, sound=False, difficulty=0, cam='full')
            print(f'Starting game')
            inter = setInterval(1, game_next)

            return render_template('game.html', name=name)
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

if __name__ == "__main__":
    #atexit.register(inter.cancel)
    socketio.run(app, debug=True)
