# Fifa-42 - Reborn!
A modern port of a beloved game me and a couple of friends wrote.  
I also intend to convert this into a full blown online game along with a realistic AI.

## Milestones
- [ ] Create a basic python port (using PyGame for now)
- [ ] Set up basic (original) AI team
- [ ] Convert to a static online game
- [ ] Train AI using Reinforcement Learning (super hard)

## Setup
### Structure
```terminal
.
├── agents.py # Agents that can play the game (A new agent only needs a move method)
├── ball.py # Football that can be passed around
├── game.py # Class that conotrols the entire game
├── driver.py # Driver to test the game
└── utils.py # Contains global settings, constants, functions and classes
```

## License
This project is licensed under the [MIT](https://opensource.org/licenses/MIT) License
