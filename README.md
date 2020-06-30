# Fifa-42 - Reborn!
A modern port of a beloved game written by me along with a couple of friends.  
The aim is to bring the original game (written in ANSI C) online.
I also intend to convert this into a full blown online game along with a realistic AI.

## Milestones
- [ ] Create a python port (using PyGame)
  - [x] Set up game environment and Human Agents
  - [ ] Set up the original AI team
  - [x] Calculate stats (possession, shot/pass accuracy)
  - [ ] Implement Pause menu
- [ ] Convert to a static online game
  - [ ] Port to JavaScript
  - [ ] Set up local multiplayer (static - requires only frontend)
  - [ ] Enable online multiplayer (requires a backend)
- [ ] Train a realistic AI team using Reinforcement Learning (super hard)

## Setup
### Structure
```terminal
.
├── agents.py # Agents that can play the game
├── teams.py # Teams consisting of a set of agents
├── ball.py # Football that can be passed around
├── game.py # Class that conotrols the entire game
├── driver.py # Driver to test the game
├── point.py # class that handles 2-D co-ordinate manipulation
└── utils.py # Contains global settings and constants
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
