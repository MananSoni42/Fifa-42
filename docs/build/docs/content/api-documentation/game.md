<a name="game"></a>
# game

<a name="game.Game"></a>
## Game Objects

```python
class Game()
```

Class that controls the entire game

<a name="game.Game.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(team1, team2, sound=True, difficulty=0.6)
```

Initializes the game

**Attributes**:

- `team1` _Team_ - Right-facing team
- `team2` _Team_ - Left-facing team

<a name="game.Game.check_interruptions"></a>
#### check\_interruptions

```python
 | check_interruptions()
```

Check for special keyboard buttons

Sets internal flags to pause, quit the game or run it in debug mode

<a name="game.Game.same_team_collision"></a>
#### same\_team\_collision

```python
 | same_team_collision(team, free)
```

Check if current player collides with any other players of the same team

<a name="game.Game.diff_team_collision"></a>
#### diff\_team\_collision

```python
 | diff_team_collision(team1, team2, free)
```

Check if current player collides with any other players of the opposite team

<a name="game.Game.collision"></a>
#### collision

```python
 | collision(team1, team2, ball)
```

Handle collisions between all in-game players.

<a name="game.Game.text_draw"></a>
#### text\_draw

```python
 | text_draw(win, text, rect, align='center')
```

Utility to draw text

**Attributes**:

- `win` _pygame.display_ - window for rendering
  text (pygame.font (rendered)): The text object
- `rect` _tuple_ - Rectangle specified as (x, y, width, height)
- `align` _string_ - text alignment can be one of 'left', 'right', 'center' (defaults to 'center')

<a name="game.Game.goal_draw"></a>
#### goal\_draw

```python
 | goal_draw(win)
```

Display the current score (goals for each side)

<a name="game.Game.field_draw"></a>
#### field\_draw

```python
 | field_draw(win, hints)
```

Draw the football pitch

**Attributes**:

- `win` _pygame.display_ - window for rendering
- `hints` _bool_ - If (movement-based) hints are to be shown

<a name="game.Game.draw"></a>
#### draw

```python
 | draw(win, hints=True)
```

Draw the entire game

Calls ```field_draw()``` along with the ```draw()``` methods for each team and the ball

<a name="game.Game.pause_draw"></a>
#### pause\_draw

```python
 | pause_draw(win)
```

Draw the pause

Displays statistics for possession, pass accuracy and shot accuracy

<a name="game.Game.get_state"></a>
#### get\_state

```python
 | get_state()
```

Create a state object that summarized the entire game

```
state = {
    'team1': {
        'players' # list of the team player's coordinates
        'goal_x' # The x-coordinate of their goal post
    },
    'team2': {
        'players' # list of the team player's coordinates
        'goal_x' # The x-coordinate of their goal post
    },
    'ball' # Position of the ball
}
```

<a name="game.Game.next"></a>
#### next

```python
 | next()
```

Move the game forward by 1 frame

Passes state objects to the teams and pass their actions to ```move_next()```

<a name="game.Game.move_next"></a>
#### move\_next

```python
 | move_next(a1, a2)
```

Update the players' and ball's internal state based on the teams' actions

**Attributes**:

- `a1` _list_ - list of actions (1 for each player) in team 1
- `a2` _list_ - list of actions (1 for each player) in team 2
  
  Each action must be a key in the ```ACT``` dictionary found in ```const.py```

