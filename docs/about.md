This game was originally started as a final project for our final programming class (in 2013). The game was originally written in ANSI C (the only programming language we knew), only worked in a console and took us a whopping 8 months to write!  
Looking back, the game was a perfect example of how to NOT write code - We used NO documentation or comments, the variables were single letters and the entire codebase was a single file.
> // When I wrote the code, only god and I knew how it worked, now only god knows

We decided to rewrite the entire game in Python with an aim of making the original game more accessible. It has since turned into a full fledged project that will (hopefully) have:
* Good documentation making it easy for anyone to contribute
* An option to play online (with multiplayer support)
* A Reinforcement-Learning based computer team that adapts itself to defeat you.

## Progress
- [x] Create an executable game - release v1.0
- [ ] Add a web UI  - Release - release v2.0
    - [ ] Port python to JavaScript
    - [ ] Set up local single player (static - requires only frontend)
    - [ ] Add online multi player (requires a backend)
- [ ] Set up better computer agents
    - [x] Set up the original AI team
    - [ ] Come up with an improved (hard-coded) AI team
    - [ ] Train a realistic AI team using Reinforcement Learning - release v3.0
