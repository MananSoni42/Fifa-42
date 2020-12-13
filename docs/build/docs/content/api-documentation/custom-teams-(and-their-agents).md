<a name="original_ai"></a>
# original\_ai

<a name="original_ai.OriginalAIAgent"></a>
## OriginalAIAgent Objects

```python
class OriginalAIAgent(Agent)
```

Harcoded AI agents that play like the original AI (designed in 2013)
Takes an additional difficulty arguement

<a name="original_ai.OriginalAIAgent.draw"></a>
#### draw

```python
 | draw(win, team_id, debug=False)
```

Draw an AI agent

Also displays circles with ```AI_FAR_RADIUS``` and ```AI_NEAR_RADIUS``` when debug is True

<a name="original_ai.OriginalAIAgent.dist_to_line"></a>
#### dist\_to\_line

```python
 | dist_to_line(line, pt)
```

perpendicular of a pt from the given line

**Attributes**:

- `line` _tuple_ - A straight line representing x*line[0] + y*line[1] + line[2] = 0
- `pt` _Point_ - a 2D point

<a name="original_ai.OriginalAIAgent.ai_move_with_ball"></a>
#### ai\_move\_with\_ball

```python
 | ai_move_with_ball(enemy_players, goal_x)
```

How AI players move when they have the ball

**Attributes**:

- `enemy_players` _list_ - A list of the positions (coordinates) of the enemy players
- `goal_x` _int_ - The x-coordinate of the enemy's goal post
  
  Returns an ACT
  
  **Working**:
  
  - If this player has the ball
  - Calculate vectors towards the goal and away from nearby players of the opposite team
  - Add up all these vectors and move in that direction (probabilistically)
  - enemy_players: positions of all of the enemy team

<a name="original_ai.OriginalAIAgent.ai_move_without_ball"></a>
#### ai\_move\_without\_ball

```python
 | ai_move_without_ball(ball)
```

How AI players move when they do not have the ball

**Attributes**:

- `ball` _Point_ - position of the ball
  
  Returns an ACT
  
  **Working**:
  
  - If the ball is within its ```AI_FAR_RADIUS```, move towards the ball (probabilistically)
  - Otherwise, do ```NOTHING```

<a name="original_ai.OriginalAIAgent.ai_pass"></a>
#### ai\_pass

```python
 | ai_pass(team_players, enemy_team_players)
```

How AI players pass the ball

**Attributes**:

- `team_players` _list_ - A list of the positions (coordinates) of the team players
- `enemy_team_players` _list_ - A list of the positions (coordinates) of the enemy team players
  
  Returns an ACT
  
  **Working**:
  
  - Pass the ball such that the perpendicular distance to the pass line is less than ```AI_MIN_PASS_DIST```
  - Pass is valid if no enemy is nearer than a team player in that direction
- `Note` - The origin is at top-left instead of the standard bottom-left so we map y to H-y

<a name="original_ai.OriginalAIAgent.ai_shoot"></a>
#### ai\_shoot

```python
 | ai_shoot(gk, goal_x)
```

How AI players shoot the ball

**Attributes**:

- `gk` _Agent_ - The enemy's goalkeeper agent
- `goal_x` _int_ - the x-coordinate of the enemy's
  
  Returns an ACT
  
  **Working**:
  
  - Only shoots if within ```AI_SHOOT_RADIUS``` of  the enemy goal
  - Shoots to maximize distance between keeper and shot while keeping the shot within goal boundaries
- `Note` - The origin is at top-left instead of the standard bottom-left so we map y to H-y

<a name="original_ai.OriginalAIAgent.gk_move"></a>
#### gk\_move

```python
 | gk_move(goal_x, ball)
```

How the AI goalkeeper moves

**Attributes**:

- `goal_x` _int_ - the x-coordinate of the enemy's
- `ball` _Ball_ - The football object
  
  Returns an ACT
  
  **Working**:
  
  - Moves towards the ball (tracks the y coordinate)
  - Does not go outside the goals boundary

<a name="original_ai.OriginalAIAgent.gk_pass"></a>
#### gk\_pass

```python
 | gk_pass(enemy_players, goal_x)
```

How the AI goalkeeper passes

**Attributes**:

- `enemy_players` _list_ - A list of the positions (coordinates) of the enemy players
- `goal_x` _int_ - The x-coordinate of the team's goal post
  
  Returns an ACT
  
  **Working**:
  
  - Pass such that enemy players in AI_SHOOT_RADIUS do not get the ball

<a name="original_ai.OriginalAIAgent.move"></a>
#### move

```python
 | move(state_prev, state, reward, selected)
```

Umbrella function that is used to move the player. Overrides the Agent's ```move()``` method

Returns an ACT

**Working**:

- if the selected player is the goal keeper and it has the ball: call ```ai_gk_pass()```
- else if the selected player is the goal keeper and it does not have the ball: call ```ai_gk_move()```
- else If the selected player is within ```AI_SHOOT_RADIUS``` of the enemy's goal post and it has the ball: call ```ai_shoot()```
- else If the selected player has the ball: call ```ai_pass()``` or ```ai_move()``` based on the ```PASS_PROB```
- else call ```ai_move_without_ball()``` or ```ai_move_with_ball()```

<a name="original_ai.OriginalAITeam"></a>
## OriginalAITeam Objects

```python
class OriginalAITeam(Team)
```

The AI team used in the original (C++) version

<a name="original_ai.OriginalAITeam.select_player"></a>
#### select\_player

```python
 | select_player(ball)
```

Select a player based on the balls position

**Working**:

- If ball is near the D-area, keeper gets automatic control
- Otherwise the player nearest to the ball has control (ties are broken randomly)

<a name="original_ai.OriginalAITeam.formation_dir"></a>
#### formation\_dir

```python
 | formation_dir(id)
```

Send player (with the given ID) to his designated place in the formation

**Working**:

- If player is in-line (horizontally or vertically), move directly towards original point (U/L/D/R)
- Otherwise choose 2 directions that take you closer to the original point and choose one of them randomly (UL/UR/DL/DR)

<a name="original_ai.OriginalAITeam.move"></a>
#### move

```python
 | move(state_prev, state, reward)
```

Move each player in the team. Call this method to move the team

<a name="human"></a>
# human

<a name="human.HumanAgent"></a>
## HumanAgent Objects

```python
class HumanAgent(Agent)
```

Agents controlled by humans

<a name="human.HumanAgent.draw"></a>
#### draw

```python
 | draw(win, team_id, selected=False, debug=False)
```

Draw the human agent. Also draws a red circle on top of the selected player

<a name="human.HumanAgent.move"></a>
#### move

```python
 | move(state_prev, state, reward)
```

Move the human agent based on the keyboard

<a name="human.HumanTeam"></a>
## HumanTeam Objects

```python
class HumanTeam(Team)
```

A team of human players

<a name="human.HumanTeam.update"></a>
#### update

```python
 | update(action, ball)
```

Select a player (based on the Ball's state) and update the team's state based on the received actions and the ball's position

<a name="human.HumanTeam.draw"></a>
#### draw

```python
 | draw(win, debug)
```

Draw the human team

<a name="human.HumanTeam.select_player"></a>
#### select\_player

```python
 | select_player(ball)
```

Select the player that is controlled by the keyboard

**Working**:

- If ball is near the D-area, keeper gets automatic control
- Otherwise the player nearest to the ball has control (ties are broken randomly)

<a name="human.HumanTeam.formation_dir"></a>
#### formation\_dir

```python
 | formation_dir(id)
```

Send player (with the given ID) to his designated place in the formation

**Working**:

- If player is in-line (horizontally or vertically), move directly towards original point (U/L/D/R)
- Otherwise choose 2 directions that take you closer to the original point and choose one of them randomly (UL/UR/DL/DR)

<a name="human.HumanTeam.move"></a>
#### move

```python
 | move(state_prev, state, reward)
```

Move a human team

**Working**:

- Player nearest to the ball moves through keyboard
- All other players return to their original positions (if maintain_formation is set)

<a name="random"></a>
# random

<a name="random.RandomAgent"></a>
## RandomAgent Objects

```python
class RandomAgent(Agent)
```

Agents that move randomly

<a name="random.RandomAgent.move"></a>
#### move

```python
 | move(state_prev, state, reward)
```

Move the agent randomly

<a name="random.RandomTeam"></a>
## RandomTeam Objects

```python
class RandomTeam(Team)
```

A team of random agents

<a name="random.RandomTeam.move"></a>
#### move

```python
 | move(state_prev, state, reward)
```

Move each player randomly

