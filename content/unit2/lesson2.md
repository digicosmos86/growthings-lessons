+++
title = "Looping with Pixels"
date =  2018-02-27T09:59:08-05:00
weight = 6
pre = "<b>Lesson 2. </b>"
+++

---

## Lesson Information

In this lesson we build complexity through for-loops.  The students will learn how to discover patterns in code and use loops to simplify their code, both very important concepts in computational thinking.  They will also learn how to build up complexity by combining loops. The ultimate goal is to understand how we can construct layers of abstraction to solve problems.

{{% sidebar "Highlights" %}}

##### Computational Thinking Skills

* **Abstraction**: Discovering Patterns
* **Automation**: Automating routines with loops
* **Analysis**: Using the debug tool to peek inside the loop and understand for-loops

##### Standard Alignments

* Todo

##### Cross-discipline Applications

* N/A

##### Duration

2 hours

{{% /sidebar %}}

#### The purpose of the lesson is to:

1. Learn the concept of for-loops
2. Review the concept of lists and iterating through lists
3. Build complexity through loops in loops

#### Driving Questions:

* Why do we need for-loops when we have while-loops?
* Why do we need `list`s?
* How does list iteration work?
* What are individual frames composed of?

#### Computer Science Concepts:

> for-loops, list iteration, range

#### Materials Needed:

> Raspberry Pi 3 with SenseHAT; {{% button href="https://github.com/digicosmos86/MicroInventor_Hugo/raw/master/content/unit2/lesson2.files/worksheet.pdf" icon="fa fa-download" %}}Worksheet{{% /button %}} with [draw_line_silly.py]({{< ref "#draw_line_silly" >}}) below.

#### Target Skills:

1. Understand what loops are for flow control
2. Fine-control how many times loops will be executed
3. Construct lists and access its elements
4. Identify patterns in code and rewrite with loops

---

## Instructional Plan and Structure

### Overview and Motivation (10 minutes)

Begin the class by stating that we are going to use finer controls of the individual pixels to do cool things such as building cool animations on the SenseHAT LED matrix.  Then demonstrate what the following code can do.

```python
# draw_line.py
from sense_hat import SenseHat
sense = SenseHat()

import time

r = [255, 0, 0]
sense.clear()

for i in range(8):
    sense.set_pixel(i, i, r)
    time.sleep(1)
```

```python
# rainbow.py
from sense_hat import SenseHat
sense = SenseHat()

import time

r = [255, 0, 0]
o = [255, 127, 0]
y = [255, 255, 0]
g = [0, 255, 0]
b = [0, 0, 255]
i = [75, 0, 130]
v = [139, 0, 255]
w = [255, 255, 255]

list_of_colors = [r, o, y, g, b, i, v, w]

sense.clear()

for i in range(8):
    for j in range(8):
        sense.set_pixel(i, j, list_of_colors[i])
    time.sleep(0.5)
```

### What are frames composed of? (15 minutes)

In the last lesson we got to know that an animation is composed of individual frames. However, what are frames composed of?

Take a look at the following pictures:

![pixelation_wikipedia](https://upload.wikimedia.org/wikipedia/commons/e/e3/Dithering_example_undithered.png)

Individual frames (static images) are composed of individual pixels, like this Iron Man picture: 

![Iron Man](https://cdn.shopify.com/s/files/1/0843/3925/files/ironman_pixelart_grid_large.png?v=1475115142) 

Each pixel has its own RGB values, just like what we did in drawing the frames in the last lesson with `sense.set_pixels()` with `pixel_list`s.

Now, feel free to use the Raspberry Pi image viewer to open the images you downloaded (they should be in the `Downloads` folder). Feel free to zoom in as much as you can until you see individual pixels.

How, then, do we control individual pixels?

### Getting Familiar with the Grid (20 minutes)

Explain to the students that all the cool things like drawing an animated rainbow are based on setting individual pixels.  Ask the them what function should be used to set individual pixels, if the function for drawing an entire frame is called `sense.set_pixels()`. (`sense.set_pixel(x, y, color)`)

{{% notice note %}}
`x`, `y` are x, y coordinates starting with 0. See the image below.  Also, set `color` here directly e.g. `sense.set_pixel(1, 2, [255,255,0])`.  It is __wrong__ to write `color = [255, 0, 0]`.
{{% /notice %}}

![RPi Pixel](https://s3.eu-west-2.amazonaws.com/learning-resources-production/projects/rpi-sensehat-led-coordinates/74c1964b50cd187a24d1ba6365c46006161f539b/en/images/coordinates.png)

**Task**: Use this {{% button href="https://github.com/digicosmos86/MicroInventor_Hugo/raw/master/content/unit2/lesson2.files/worksheet.pdf" icon="fa fa-download" %}}worksheet{{% /button %}} to design a picture that you would like to display on the LED matrix.  Then use `sense.set_pixel()` method to "draw" the picture on the LED matrix.

```python
sense.set_pixels(pixel_list)
```

If you want to, you can define another picture just like this, but change a few pixels, then you can create a SenseHAT animation!  You can set a time interval between each picture to control how fast the animation is.  Then, you can use a `while-loop` to display the animation forever.  See the code below:

### Finding Patterns in Code (70 minutes)

For some regular patterns of code, such as a diagonal line, there are even simpler ways to control the LED matrix.  This is what we are going to do next.

#### Diagonal Line - Silly Code

Now ask the students what they would normally write to do what `draw_line.py` does (Set the pixel 8 times.  See below)<a name = "draw_line_silly"></a>.

```python
# draw_line_silly.py
# uncomment the code after all pixels show up at the same time
from sense_hat import SenseHat
sense = SenseHat()

# import time

r = [255, 0, 0]
sense.clear()

sense.set_pixel(0,0,r)
# time.sleep(1)
sense.set_pixel(1,1,r)
# time.sleep(1)
sense.set_pixel(2,2,r)
# time.sleep(1)
sense.set_pixel(3,3,r)
# time.sleep(1)
sense.set_pixel(4,4,r)
# time.sleep(1)
sense.set_pixel(5,5,r)
# time.sleep(1)
sense.set_pixel(6,6,r)
# time.sleep(1)
sense.set_pixel(7,7,r)
# time.sleep(1)
```

Demonstrate that this works but ask the students why this is silly.

* Have to copy and paste a lot (Copy and pasting is never a good idea)
* If you want to change colors, you will have to change it 8 times.
* If you want to change time interval, you also have to change it 8 times
* What if you have a huge LED matrix, like what we see in real life?

Now give each pair of student a printed copy of `draw_line_silly.py` and ask the students to find patterns - what changes, what remains the same.

#### Patterns and Improvement

So now we've discovered four things:

1. This code snippet was repeated (looped 8 times).
2. Each time, only the coordinates changes
3. The `x`, `y` coordinates are the same each time when this code snippet was executed.
4. The coordinate goes from 0 to 7 each time.

```python
sense.set_pixel(_, _, r)
time.sleep(1)
```

What we wish to do:

1. Execute this code snippet exactly 8 times.
1. Have a number in the place of the underscore symbol.
1. This number goes from 0 to 7.

We can use a `for-loop` in Python to do that.

```python
for i in [0, 1, 2, 3, 4, 5, 6, 7]:
    sense.set_pixel(i, i, r)
    time.sleep(1)
```

**Explanation**: First we construct a `list`.  What Python does is that it iterates through the list.  The variable `i` is called a _counter_.  Each time the code executes, `i` is assigned to the next value in the list.  E.g. the first time the code executes, Python looks at the first element of the list, and assign `i = 0`. So what is executed is:

```python
sense.set_pixel(0, 0, r)
time.sleep(1)
```

**Question:** How many times was the code executed?

Ask the student why this is efficient:

1. No need to copy and paste.  The code is fast to write and easy to understand.
1. Can easily change the color and time interval.
1. Can change the code slightly and do different things.  For example:

```python
for i in [0, 1, 2, 3, 4, 5, 6, 7]: # Colon is very important, and so is indentation
    sense.set_pixel(i, 4, r)
    time.sleep(1)
```

```python
for i in [0, 1, 2, 3, 4, 5, 6, 7]:
    sense.set_pixel(5, i, r)
    time.sleep(1)
```

Ask the students to use their {{% button href="https://github.com/digicosmos86/MicroInventor_Hugo/raw/master/content/unit2/lesson2.files/worksheet.pdf" icon="fa fa-download" %}}worksheet{{% /button %}} to figure out why the code does what it does.

There is *one more thing* that the code does not do yet.  You have to manually write the list.  What if we have an 100x100 matrix?  In Python, you can write `range(start, end, step)` instead:

```python

for i in range(0, 8, 1):
    sense.set_pixel(5, i, r)
    time.sleep(1)
```

Or, if the list increments with step 1, you can omit the `1` and write:

```python
for i in range(0, 8):
    sense.set_pixel(5, i, r)
    time.sleep(1)
```

Or, if the list starts with `0`, you can omit the `0` and write:

```python
for i in range(8):
    sense.set_pixel(5, i, r)
    time.sleep(1)
```

**Free play Time:**  Feel free to change the start, end, step, coordinates, colors and figure out what happens.

Some Guiding Questions:

* How to set one line? One column?
* Can each pixel have a different color?

{{% notice tip %}}
The key is to change where i is and the set `x`, `y` values.
{{% /notice %}}

```python
# line_rainbow.py
from sense_hat import SenseHat
sense = SenseHat()

import time

r = [255, 0, 0]
o = [255, 127, 0]
y = [255, 255, 0]
g = [0, 255, 0]
b = [0, 0, 255]
i = [75, 0, 130]
v = [139, 0, 255]
w = [255, 255, 255]

colors = [r, o, y, g, b, i, v, w]

sense.clear()

for i in range(8):
    sense.set_pixel(i, 0, colors[i])
    time.sleep(0.5)
```

* [Optional] How to make an X?

{{% expand "Expand to see the code" %}}

```python
from sense_hat import SenseHat
import time

sense = SenseHat()
r = [255, 0, 0]

for i in range(8):
    sense.set_pixel(i, i, r)
    time.sleep(1)

for j in range(8):
    sense.set_pixel(7-j, j, r)
    time.sleep(1)
```

{{% /expand %}}

### Move up in Complexity - Rainbow Pattern

Now that we know how to draw lines and columns with loops, we can move on to draw the rainbow pattern.

Ask the students how they would do this given what they know. Again, we can try looking at some silly code.

```python
# rainbow_silly.py
from sense_hat import SenseHat
sense = SenseHat()

import time

r = [255, 0, 0]
o = [255, 127, 0]
y = [255, 255, 0]
g = [0, 255, 0]
b = [0, 0, 255]
i = [75, 0, 130]
v = [139, 0, 255]
w = [255, 255, 255]

#list_of_colors = [r, o, y, g, b, i, v, w]

sense.clear()

for i in range(8):
    sense.set_pixel(i, 0, r)
time.sleep(0.5) # Indentation vs no Indentaiton?

for i in range(8):
    sense.set_pixel(i, 1, o)
time.sleep(0.5) # Indentation vs no Indentaiton?

for i in range(8):
    sense.set_pixel(i, 2, y)
time.sleep(0.5) # Indentation vs no Indentaiton?

for i in range(8):
    sense.set_pixel(i, 3, g)
time.sleep(0.5) # Indentation vs no Indentaiton?

for i in range(8):
    sense.set_pixel(i, 4, b)
time.sleep(0.5) # Indentation vs no Indentaiton?

for i in range(8):
    sense.set_pixel(i, 5, i)
time.sleep(0.5) # Indentation vs no Indentaiton?

for i in range(8):
    sense.set_pixel(i, 6, p)
time.sleep(0.5) # Indentation vs no Indentaiton?

for i in range(8):
    sense.set_pixel(i, 7, w)
time.sleep(0.5) # Indentation vs no Indentaiton?
```

Again, what changed, what is the same?  What changed?

We can embed a loop in another loop like this:

{{% expand "Expand to see the code" %}}

```python
for j in range(8):
    for i in range(8):
        sense.set_pixel(i, j, colors[i])
        # time.sleep(0.1) # Can we add another interval here?
    time.sleep(0.5) # Think about Indentation Level
```

{{% /expand %}}

---

## Review and Assessment

1. How many times was `sense.set_pixel()` executed?
2. Switch `i` and `j`.  What is going to happen?
3. What happens if we switch the indentation of `time.sleep()`?

Explain that we are not going to do too much loops in loops.  What we need to understand is how to break down a big problem in smaller ones.  This problem seems to be very complicated, but it's nothing more than building upon what we already know.