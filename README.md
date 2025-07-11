# TTPALETTE
### A library for coloring texts in the terminal

This library works with [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code)

### 256 Color table

The photo is from [here](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797)<br>
![256 Color table](https://user-images.githubusercontent.com/995050/47952855-ecb12480-df75-11e8-89d4-ac26c50e80b9.png)


## Install

```
pip install ttpalette
```


## Examples

#### Use a specific color

```python
from ttpalette import ttpalette

ttpalette.BackColor().custom(14)
ttpalette.Color().custom(14)
```

#### Use a solid color

```python
from ttpalette import ttpalette

ttpalette.Color.RED()
ttpalette.BackColor.RED()
```

#### Fixed colors available

```
BLACK
RED
GREEN
YELLOW
BLUE
MAGENTA
CYAN
WHITE

RESET

```

#### Back to normal

```python
from ttpalette import ttpalette


ttpalette.Color.RESET
ttpalette.BackColor.RESET
```
