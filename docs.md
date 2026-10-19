# SigmaEngine API

## Scene

A `Scene` is the main component of Sigma Engine.
It contains a list of `objects` and a `camera`.

## Object

An `object` is a sub component of a `Scene`. It extends the `Pointer` class. It is a graphical component which will be presented to the screen if it's in the `camera`'s field of view.

### Object.shape

`shape` defines how the object is drawn on the screen.
It can ONLY have THESE SPECIFIC VALUES, DEPENDING OF wHAT SHAPE IT wANTS TO BE:

- `0`: circle
- `1`: rectangle
- `2`: polygon

`shape` NEEDS TO BE EXACTLY ONE OF THOSE VALUES.
