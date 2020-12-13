<a name="agent"></a>
# agent

<a name="agent.Agent"></a>
## Agent Objects

```python
class Agent(ABC)
```

Abstract class that controls agents in the football game

Implement the move method to instantiate a valid agent

<a name="agent.Agent.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(id, team_id, pos, dir='L')
```

Initialize a player

**Attributes**:

- `id` _int_ - Player's unique ID
- `team_id` _int_ - ID of the team the player plays for
- `pos` _Point_ - The player's initial position
- `dir` _string_ - The player's current direction (which way it faces). Either 'R' or 'L'

<a name="agent.Agent.draw"></a>
#### draw

```python
 | draw(win, team_id, debug=False)
```

Draw the player as an animated sprite

**Attributes**:

- `win` _pygame.display_ - Window on which to draw
- `team_id` _int_ - Required to get the correct sprite
- `debug` _bool_ - Show additional info including the player's ID and the square used to approximaate the player

<a name="agent.Agent.update"></a>
#### update

```python
 | update(action, players)
```

Update player's (in-game) state based on his action

<a name="agent.Agent.move"></a>
#### move

```python
 | @abstractmethod
 | move(state_prev, state, reward)
```

Implement this method for a valid agent

**Attributes**:

- `state_prev` _dict_ - The lsat to last game state
- `state` _dict_ - The last game state
- `reward` _list_ - Reward returned from this state (Not implemented)
  
  Should return a valid action

