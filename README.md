
# Fifa-42 - Reborn!
A modern port of a beloved game written by me along with a couple of friends.  
The aim is to make the original game (written in ANSI C) more accessible.  
The ideal outcome would be a python game with an AI that can learn from the opposing player's moves along with an online game that supports single-player as well multi-player

## Milestones
- [ ] Create an executable game file (.exe /.rpm/.deb packages) - Release v1.0
  - [x] Set up game environment and Human Agents
  - [x] Calculate stats (possession, shot/pass accuracy)
  - [x] Implement Pause menu
  - [x] Create menu
  - [x] Add sound
  - [ ] Package the game as an executable
- [ ] Convert to a static online game - Release - v2.0
  - [ ] Port to JavaScript
  - [ ] Set up local multiplayer (static - requires only frontend)
  - [ ] Enable online multiplayer (requires a backend)
- [ ] Set up true single player
  - [ ] Set up the original AI team (included in v1)
  - [ ] Come up with an improved (hard-coded) AI team
  - [ ] Train a realistic AI team using Reinforcement Learning (super hard)

## Controls
  Key                  | Action                     |
  -------------------- | -------------------------- |
  Arrow keys           | Move the (selected) player |
  Q,W,E,A,Z,X,C        | Shoot the ball             |
  ESC                  | Bring up Pause menu        |
  BACKSPACE            | Collapse Pause menu        |


## Setup
### Structure
```terminal
.
├── driver.py # Driver to test the game
├── game.py # Class that controls the entire game
├── ball.py # Football that can be passed around
├── teams.py # Teams consisting of a set of agents
├── agents.py # Agents that can play the game
├── settings.py # Global settings and paths
├── const.py # Important game constants
├── stats.py # In-game statistics (possession, goals scored, pass/shot accuracy)
└── point.py # class that handles 2-D co-ordinate manipulation
```

### Installing locally
* The game requires Python3+  

* Install dependancies using:  
```terminal
pip3 install -r requirements.txt
```

* Run the game using:  
```terminal
python3 driver.py
```

## License
This project is licensed under the [MIT](https://opensource.org/licenses/MIT) License
