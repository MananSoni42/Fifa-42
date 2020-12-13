<a name="team"></a>
# team

<a name="team.Team"></a>
## Team Objects

```python
class Team(ABC)
```

Abstract class that controls a team of agents.

Implement the move and set_players methods to instantiate

<a name="team.Team.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(color=(0, 0, 0), formation='default')
```

Initialize the teams (not completely, some paramters are set using the ```init()``` method)

**Attributes**:

- `color` _tuple_ - The RGB value of the team
- `formation` _string_ - The team's formation of the team. Must be a key of ```FORM``` from ```const.py```

<a name="team.Team.init"></a>
#### init

```python
 | init(id, dir, diff)
```

Set the teams id, direction and difficulty (only for AI teams)
Also recolor the sprites based on the team's chosen color

**Attributes**:

- `id` _int_ - The team's id (must be either 1 or 2)
- `dir` _str_ - The team's direction (must be either 'L' or 'R')
  
  Calls ```set_players()``` and ```set_color()```

<a name="team.Team.set_color"></a>
#### set\_color

```python
 | set_color()
```

Recolor the sprites using this team's color

<a name="team.Team.set_formation"></a>
#### set\_formation

```python
 | set_formation(formation)
```

Set the teams formation

<a name="team.Team.formation_toggle"></a>
#### formation\_toggle

```python
 | formation_toggle()
```

Toggle whether the team maintains its formation

<a name="team.Team.draw"></a>
#### draw

```python
 | draw(win, debug=False)
```

Draw the team

Basically calls each players' ```draw()``` method

<a name="team.Team.update"></a>
#### update

```python
 | update(action, ball)
```

Update the team's state

Basically calls each players' ```update()``` method

<a name="team.Team.set_players"></a>
#### set\_players

```python
 | @abstractmethod
 | set_players(ids=list(range(NUM_TEAM)))
```

Implement this method to instantiate a valid team.

Add players (of relevant class) to the team

**Attributes**:

- `ids` _list_ - IDs of players to include in the team (defaults to all the players)
  
  **Requirements:**
  
  * Players are added to a list called players
  * Their ids match their respective index in the array

<a name="team.Team.move"></a>
#### move

```python
 | @abstractmethod
 | move(state_prev, state, reward)
```

Implement this method for a valid team

**Attributes**:

- `state_prev` _dict_ - The lsat to last game state
- `state` _dict_ - The last game state
- `reward` _list_ - Reward returned from this state (Not implemented)
  
  Should return a list of valid actions (in the same order as each of the players)

