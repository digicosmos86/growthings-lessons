+++
title = "Image on the LED Matrix"
date =  2018-02-26T22:39:05-05:00
weight = 5
pre = "<b>Lesson 1. </b>"
+++

---

## Lesson Information

In this lesson the students will learn to decompose a problem by breaking down an animation.  Then they will design and code an animation on the LED matrix by using a `pixel_list`, the while-loop, and the `sleep` function from the `time` package.

{{% sidebar "Highlights" %}}

##### Computational Thinking Skills

* **Abstraction**: Decomposition
* **Automation**: "forever" loops

##### Standard Alignments

* Todo

##### Cross-discipline Applications

* N/A

##### Duration

2 hours

{{% /sidebar %}}

#### The purpose of the lesson is to:

1. Learn to decompose a problem by learning about animations
2. Draw single frames with a list of colors
3. Create animations by inserting a pause between frames
4. Create a loop with while-loops

#### Driving Questions:

* What are animations composed of?
* How to build animations?
* How to draw single frames on the LED matrix?
* How to control the speed of the animation?

#### Computer Science Concepts:

> while-loops, lists, variables

#### Materials Needed:

> Raspberry Pi 3 + SenseHAT; {{% button href="https://github.com/digicosmos86/MicroInventor_Hugo/raw/master/content/unit2/lesson1.files/worksheet.pdf" icon="fa fa-download" %}}Worksheet{{% /button %}}

#### Target Skills:

1. SWBAT articulate what an animation is composed of
2. SWBAT draw single frames on the LED matrix with a list of pixels
3. SWBAT control frame speeds with `time.sleep()` function

---

## Instructional Plan and Structure

In this unit the students will encounter their first microproject that is connected to their final project.  Explain to the students what they need to do:

* An animation on the SenseHAT LED matrix with at least 3 frames.
* loops and custom functions will have to be used (we will teach how to use them).
* students will have to control individual pixels (although it's OK to use `sense.set_pixels()` function as well).
* explain what the animation is about.

### Overview of the lesson (5 minutes)

In this lesson we focus on making animations frame-by-frame using the `sense.set_pixels()` function.  But first, let's talk about how animation works.  What do you think animations are made of (we are talking about 2D animations here as 3D animations used in movies are different)?  We can go to the popular website [GIPHY](https://giphy.com).  This is where a lot of the gif animations on facebook and Snapchat come from.  Another website with many gifs is [9GAG](https://9gag.com).

### Decompose an animation (20 minutes)

Talk in pairs about what these gif animations are composed of.  You can also select any gif you like and post the gif to [this website](https://ezgif.com/split). This website can split an animated gif into individual frames. You can also make the gif go faster or slower using the speed tool on the tool bar.

Answer the following questions:

* How many **frames** are there in your animation?
* What are the ways of making the animation go faster and slower?

Now we know that animations are composed of individual pictures, called frames. If the frames transition between each other really fast, we think that it is moving.  Maybe you have seen flip book animations like this:

{{< youtube CSj0lajQBrM >}}

So this is the structure of an animation:

{{< mermaid align="center" >}}
graph LR;

    B1(Frame1)-->|Interval|B2(Frame2)
    B2-->|Interval|B3(Frame3)
    
{{< /mermaid >}}

### Building Frames (1 hour)

Now let's build individual frames. Before we do anything, it is a good idea to **clear** whatever that's on the LED matrix.  Python provides us the `sense.clear()` function for us to do that.  Remember to put it at the beginning of your code.

Let's take a look at this code:

```python
from sense_hat import SenseHat

sense = SenseHat()

sense.clear()

X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

sense.set_pixels(question_mark)
```

Let's run the code.  What happened?  What do you think this code does? What do you think the `X`s and `O`s are?  What is the type of `question_mark`? How many elements are there in `question_mark`?

{{% notice note %}}
So the `X`s and `O`s are actually variable names!
{{% /notice %}}

So here is actually what happened: we defined two colors: `red` and `white`. However, we named them to `X`s and `O`s.  Then we constructed a `list` called `question_mark`, with \\(8 \times 8=64\\) elements. Each of these elements maps to a pixel on the LED matrix.  If it is an `O`, the pixel will be `white`, and if it's an `X`, the corresponding pixel will be `red`! After all these, we pass this `question_mark` to `sense.set_pixels()` function, and voila! The question mark is shown on the LED matrix!

{{% notice warning %}}
Pay attention to the plural in `sense.set_pixels()`. In the next few lessons, we will encounter the `sense.set_pixel()` function, which looks very similar.
{{% /notice %}}

We can design our own patterns.  You can work on {{% button href="https://github.com/digicosmos86/MicroInventor_Hugo/raw/master/content/unit2/lesson1.files/worksheet.pdf" icon="fa fa-download" %}}this worksheet{{% /button %}}. Draw your own patterns on the grid, define your own color variables, and then modify the `question_mark` variable (you can call it whatever you like). Just remember to pass it to `sense.set_pixels()` function.

Feel free to design 2-3 frames and show them on your SenseHAT.

### Make your animation! (15 minutes)

Now that we have a few frames, let's put them together and make animations! You might have already tried something like this:

```python
from sense_hat import SenseHat

sense = SenseHat()

sense.clear()

X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White
W = [0, 255, 0] # Green

question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

sense.set_pixels(question_mark)

plus = [
O, O, O, O, O, O, O, O,
O, O, O, W, W, O, O, O,
O, O, O, W, W, O, O, O,
O, W, W, W, W, W, W, O,
O, W, W, W, W, W, W, O,
O, O, O, W, W, O, O, O,
O, O, O, W, W, O, O, O,
O, O, O, O, O, O, O, O,
]

sense.set_pixels(plus)
```

Does it work?  What do you think is going on here?

We don't see the question mark at all because this program runs fast.  Plus shows up way before we can see the question mark. We will need to add an interval - have the program pause for a short period of time, and then move on to show the next frame.  We have the function `time.sleep()` to help us do that. Before we use this function, we need to **import** the time package at the beginning of the code, like this: `import time`.  Then we can insert `time.sleep(1)` into our code.

{{% notice warning %}}
Where do we insert `time.sleep()`
{{% /notice %}}

We will have to insert `time.sleep()` right after each frame is shown, so that it becomes an interval. Now work on your code and make sure that you can see all of your frames.  Change the number in `time.sleep(1)` and see what happens.

### Boomerang! with `while` (15 minutes)

The last problem with our animation is that shows a couple of frames and then done.  Is there anything we can do to make our animations like the cool Boomerang effect on Instagram?

Yes, the answer is the `while` loop. Before defining `question_mark`, add this line to your code: `while True:`.

{{% notice warning %}}
Don't forget the colon `:` at the end.
{{% /notice %}}

The next step is very important. You need to indent the rest of your code.  This tells Python that the indented code is being looped. Now your code should look like this:

{{% expand "Expand to see the code" %}}

```python
from sense_hat import SenseHat
import time

sense = SenseHat()

sense.clear()

X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White
W = [0, 255, 0] # Green

while True:
    question_mark = [
    O, O, O, X, X, O, O, O,
    O, O, X, O, O, X, O, O,
    O, O, O, O, O, X, O, O,
    O, O, O, O, X, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, X, O, O, O, O
    ]

    time.sleep(0.5)

    sense.set_pixels(question_mark)

    plus = [
    O, O, O, O, O, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]

    sense.set_pixels(plus)

    time.sleep(0.5)
```

{{% /expand %}}

If you forget to indent your code, python will complain and you will see an error like this:

```python
IndentationError: expected an indented block
```

Then you need to check your code and make sure that it is properly indented.

Now try to write your own while loop and make your own looped animations!

{{% notice tip %}}
If you want to stop your animation, use Thonny Python's stop execution button (the big red stop sign) or `Ctrl+Z`.
{{% /notice %}}

**Challenge**

* What are the input and output of this animation program?
* Restructure this program using the structure mentioned in the last unit.

---

## Review and Assessment

1. What is a while-loop?
2. What are animations consist of?
3. What do indentations do?