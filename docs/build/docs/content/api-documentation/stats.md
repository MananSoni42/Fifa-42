<a name="stats"></a>
# stats

<a name="stats.Stats"></a>
## Stats Objects

```python
class Stats(object)
```

Keep track of game statistics

<a name="stats.Stats.__init__"></a>
#### \_\_init\_\_

```python
 | __init__()
```

Initializes the possession, pass accuracy and shot accuracy

<a name="stats.Stats.get_possession"></a>
#### get\_possession

```python
 | get_possession()
```

Return a tuple containing the current possesion (between 0 and 1) for each team

It is rounded to 2 decimal places and their sum is guaranteed to be 1

<a name="stats.Stats.get_pass_acc"></a>
#### get\_pass\_acc

```python
 | get_pass_acc()
```

Return a tuple containing the current pass accuracy (between 0 and 1) for each team

It is rounded to 2 decimal places

<a name="stats.Stats.get_shot_acc"></a>
#### get\_shot\_acc

```python
 | get_shot_acc()
```

Return a tuple containing the current shot accuracy (between 0 and 1) for each team

It is rounded to 2 decimal places

