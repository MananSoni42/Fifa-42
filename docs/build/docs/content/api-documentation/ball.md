<a name="ball"></a>
# ball

<a name="ball.Ball"></a>
## Ball Objects

```python
class Ball()
```

Implement the football used in the game

<a name="ball.Ball.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(pos, sound=True)
```

Initialize the Football

**Attributes**:

- `pos` _Point_ - the initial position of the ball

<a name="ball.Ball.draw"></a>
#### draw

```python
 | draw(win, debug=False)
```

Draw the football

**Attributes**:

- `win` _pygame.display_ - Window on which to draw
- `debug` _bool_ - If enabled, show the square used to approximate the ball
  as well as a red border whenever the ball is not free

<a name="ball.Ball.reset"></a>
#### reset

```python
 | reset(pos)
```

Reset the ball

**Attributes**:

- `pos` _Point_ - the initial position of the ball

<a name="ball.Ball.goal_check"></a>
#### goal\_check

```python
 | goal_check(stats)
```

Check if a goal is scored

**Attributes**:

- `stats` _Stats_ - Keep track of game statistics for the pause menu

<a name="ball.Ball.update_stats"></a>
#### update\_stats

```python
 | update_stats(stats, player=None, goal=None, side=None)
```

Sync ball statistics with the global variables

**Attributes**:

- `player` _Agent_ - Player that received the ball
- `goal` _bool_ - True if a goal is scored
- `side` _int_ - id of the team which conceded the goal
  
  Activates when a player receives the ball or during a goal attempt
  
  - Possession: +1 if same team pass is recorded
  - Pass: +1 to 'succ' if same team pass is recorded
  +1 to 'fail' if diff team pass is recorded
  - Shot: +1 to 'succ' if a goal is scored
  +1 to 'fail' if goal is not scored (out of bounds) / keeper stops the ball
  Does not apply if player shoots towards his own goal

<a name="ball.Ball.ball_player_collision"></a>
#### ball\_player\_collision

```python
 | ball_player_collision(team, stats)
```

Check if the ball has been captured by a player

**Attributes**:

- `team` _Team_ - The team for which to check
- `stats` _Stats_ - Keep track of game statistics for the pause menu

<a name="ball.Ball.check_capture"></a>
#### check\_capture

```python
 | check_capture(team1, team2, stats)
```

If the ball is not free, move the ball along with the player rather than on it's own

**Attributes**:

- `team1` _Team_ - Team facing right
- `team2` _Team_ - Team facing left
- `stats` _Stats_ - Keep track of game statistics for the pause menu

<a name="ball.Ball.update"></a>
#### update

```python
 | update(team1, team2, action1, action2, stats)
```

Update the ball's (in-game) state according to specified action

**Attributes**:

- `team1` _Team_ - Team facing right
- `team2` _Team_ - Team facing left
- `action1` _list_ - Actions of team 1
- `action2` _list_ - Actions of team 2
- `stats` _Stats_ - Keep track of game statistics for the pause menu
  
  Calls ```check_capture()``` and ```goal_check()```

