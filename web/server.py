from flask import Flask, render_template, request
from flask_socketio import SocketIO
import json
import threading
import atexit

import sys
import os
sys.path.append(os.path.abspath('../src'))

from teams.network import NetworkTeam

app = Flask(__name__)
app.secret_key = "fifa-42"
socketio = SocketIO(app)

num_players = 0
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
        name1: {
            'pos': [p.val for players in state['team1']['players']]
        },
        name2: {
            'pos': [p.val for players in state['team2']['players']]
        }
    }
    emit('next', {'state': network_state})

def game_next():
    game.next()
    send_network_state(game.get_state())

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/game", methods=['POST'])
def show_game():
    global teams, game, inter
    name = request.form.get('name')
    if name:
        if num_players == 0:
            team1 = NetworkTeam(formation='balanced-1', color=(0, 32, 255))
            name1 = name
            print(f'Added team1 with name {name1}')
            return render_template('game.html', name=name)
        elif len(teams) == 1:
            team2 = NetworkTeam(formation='balanced-1', color=(0, 32, 255))
            name2 = name
            print(f'Added team2 with name {name2}')

            game = Game(team1, team2, sound=False, difficulty=0, cam='full')
            print(f'Starting game')
            inter = setInterval(game_next, 1)

            return render_template('game.html', name=name)
        else:
            return render_template('error.html', message="Already have 2 players in the game")
    else:
        return render_template('error.html', message="Could not process name")

@socketio.on("move")
def move_player(data):
    name = data['name']
    if name.lower() == name1:
        team1.register_keystroke(data['key'])
    elif name.lower() == name2:
        team2.register_keystroke(data['key'])
    else:
        raise Exception(f'name `{name}` not recognized, choose from `{name1}` or `{name2}`')

if __name__ == "__main__":
    #atexit.register(inter.cancel)
    app.run(debug=True)
