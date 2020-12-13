<a name="point"></a>
# point

<a name="point.P"></a>
## P Objects

```python
class P()
```

Implementation of a 2-D point

<a name="point.P.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(x, y=None)
```

Initialize an point

**Examples**:

```
pt1 = P(3,4)
pt2 = P((3,4))
pt3 = P([3,4])
pt4 = P(pt3)
```

<a name="point.P.val"></a>
#### val

```python
 | @property
 | val()
```

Return the value of the point as a tuple rounded to the nearest integer point

<a name="point.P.mag"></a>
#### mag

```python
 | @property
 | mag()
```

Return the magnitude of the point (it's distance from zero)

