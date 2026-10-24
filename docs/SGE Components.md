# SGE Components

In SGE, there are `Scenes`, which may contain `Objects` and a `Camera`.

This manual contains information about how to use these components.

The current structure of SGE's components is structured like this:
> `Scene`
> > `Camera`
>
> > `Object`

## Scene

A `Scene` is the main component of Sigma Engine.
It contains a list of `objects` and a single `camera`.

The Developer is meant to use Scene's functions to overwrite them however they want, with the purpose of making a game or tool.

**Example**:

```py
# Import SGE libraries to use them
from sge.scene import Scene

class ExampleScene(Scene):
 # Your Code Goes Here
```

### Scene.Load(self)

Called on scene load.

It's meant for initiating objects, assets, etc, for them to be used later on.

**Example**:

```py
class ExampleScene(Scene):
 # Called on Scene Load.
 def Load(self):
  # Create a new Rectangle
  rect = Object(0)
  # Change its position
  rect.x, rect.y = 50, 50
  # Change its size
  rect.width, rect.height = 75, 75
  # Change its color
  rect.innerColor = C_BLUE
  # Add this new Object to the Scene's object list
  self.Add(rect)

  return super().Load()
```

### Scene.Update(self, dt: float) -> (newScene: str = None)

Called every frame, **before** drawing the screen.

It's meant for checking for user input, moving objects, and for changing scenes.

**`super()` Params**:

- `newScene`: if it isn't `None`, SigmaEngine will SKIP DRAWING, then load the file with that name and load the corresponding Scene.

**Overwriten Params**:

- `dt`: the delta time in seconds, which is the time that has passed between this and the last call of Update().

**Example**:

```py
class ExampleScene(Scene):
 def Update(self):
  # Check user input

  # Then for some reason, change scenes.
  return super().Update("ExampleScene2")
```

### Scene.AfterUpdate(self)

Called every frame, after the screen is drawn.

It's meant for advanced... Uhm... Devs... who want to do... advanced things.

**Example**:

```py
class ExampleScene(Scene):
 def AfterUpdate(self):
  # Your Code Goes Here
  return super().AfterUpdate()
```

### Scene.Add(self, obj)

Adds `obj` to the list of objects of this scene.

**Example**:

```py
class ExampleScene(Scene):
 def Load(self):
  # Create a new Rectangle
  rect = Object(0)
  # Change its position
  rect.x, rect.y = 50, 50
  # Change its size
  rect.width, rect.height = 75, 75
  # Change its color
  rect.innerColor = C_BLUE
  # Add this new Object to the Scene's object list
  self.Add(rect)

  return super().Load()
```

### Scene.Draw(self)

## Camera

## Object

An `object` is a sub component of a `Scene`. It extends the `Pointer` class. It is a graphical component which will be presented to the screen if it's in the `camera`'s field of view.

### Object.`init`(self, shape: int)

### Object.shape

`shape` defines how the object is drawn on the screen.
It can ONLY have THESE SPECIFIC VALUES, DEPENDING OF wHAT SHAPE IT wANTS TO BE:

- `0`: circle
- `1`: rectangle
- `2`: polygon

`shape` NEEDS TO BE EXACTLY ONE OF THOSE VALUES.
