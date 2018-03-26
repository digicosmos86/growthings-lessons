+++
title = "Building Abstractions with Functions"
date =  2018-03-25T19:07:24-04:00
weight = 7
pre = "<b>Lesson 3. </b>"
+++

---

## Lesson Information

In the previous lesson the students learned how to automate repetitive tasks using both "forever loops" `while True:` and "for-loops" `for i in ...:`. In this lesson, they will learn how to use **functions**, in connection with these loops and everything else we have learned so far, to construct more complex programs. Functions are the building blocks of more complex computer programs and therefore are a key concept in this curriculum.  We will approach functions in two steps. We will start building the concept of functions in their simplest form: a "named block" of code. We will gradually expand on this concept and introduce the concepts of **parameterization** (function **input**) and **return values** (function **output**).  In this lesson we will only focus on understanding functions as "code blocks."

{{% sidebar "Highlights" %}}

##### Computational Thinking Skills

* **Abstraction**: Building abstraction with functions
* **Automation**: Functions as a means of automation
* **Analysis**: Why do functions make code more efficient?

##### Standard Alignments

TODO

##### Cross-discipline Applications

* The concept of functions taught in this lesson is everywhere in everyday life

##### Duration

1 hour

{{% /sidebar %}}

#### The purpose of the lesson is to:

1. Gain basic understanding of the concept of functions
2. Understanding functions from their real life equivalents
3. Write functions as "code blocks" - a set of commands
4. Differentiate between **defining** a function and **calling** a function

#### Driving Questions:

* What are functions?
* Why do we use functions?
* How can we write functions ourselves?
* How can we use functions most efficiently?

#### Computer Science Concepts:

> functions, blocks, function definitions, function calls

#### Materials Needed:

> Raspberry Pi + SenseHAT

#### Target Skills:

1. SWBAT build abstractions with functions
2. SWBAT write simple functions with no input or output
3. SWBAT articulate why we need functions

---

## Instructional Plan and Structure

### Overview of the lesson (10 minutes)

Lead into the class with this question "How do we write essays?" With words, of course! However, although essays are composed of individual words, we first need to organize them into sentences. You might even argue we use words to compose phrases first. We also use paragraphs to logically organize sentences related to each other.

Writing computer programs are just like writing an essay. We write individual lines of code, but when we write code, we break the code apart into "blocks." For example, this is the code we wrote in Unit 1:

```python
# Initiation:
from sense_hat import SenseHat
sense = SenseHat()

# Input:
name = input("What is your name?\n")
speed = 0.05
red = [255, 0, 0]
blue = [0, 0, 255]

# Process
msg = "Hello Python!" + name

# Output
sense.show_message(msg, scroll_speed = speed, 
                   text_colour = red, back_colour = blue)
```

Notice that we thought the two lines under `# Initialization` and the four lines under `# Input` are more closely related to each other than other lines of code, so we naturally put them together into "blocks," just like paragraphs in an essay. This way we keep our code organized and readable, even though we don't have to do this (if we randomly add blank lines within these "blocks," the code will still run, but we don't want to do that (why not?).

Sometimes we have to tell the computer some code are in the same block, especially when we are using loops. This way, we tell the computer "we want to loop these lines of code, but leave the other lines alone." We use **indentations** to explicitly let the computer know what we want to do.

```python
while True:
    sense.show_message("Hello World!")


for i in range(8):
    sense.set_pixel(i, i, r)
    time.sleep(1)
```

Today we will learn a new structure that's closely related to these blocks. Before we reveal what this structure is, let's play a game.

### Unplugged Activity (5 minutes)

On a piece of paper, write down these instructions:

1. go to the teacher's desk
2. take a piece of paper
3. go to the back of the classroom
4. find the trash bin
5. put this piece of paper in the trash bin

Now, ask a student to follow these instructions one-by-one, and then ask the rest of the class to describe __in a phrase__ what that student just did.

Do the same activity again. This time, use this instruction:

* Walk around the classroom for one loop

Ask the rest of the class what was written on the instruction.

### "Named blocks" (10 minutes)

The activity we just did shows us that some things that we do can be further divided into a set of smaller things that are connected. For example, "doing grocery shopping" involves getting in the car, driving to the grocery store, grabbing groceries from the shelves, paying for them, and taking them home. However, we do not usually talk about these individual activities. Instead, we refer to them altogether as "doing grocery shopping."

{% note %}
Can you name other activities like this?
{% /note %}

In coding, we do the same thing. We can give a block of code a name, and next time we want to use them, we can simply call this block. In other words, we can **define** a name for this block of code. For example:

```python
# Preparation step omitted

for i in range(8):
    sense.set_pixel(i, 4, r)
    time.sleep(0.5)
```

This block of code literally draws a horizontal line on at the fifth row of the LED matrix. So why don't we call it `draw_5th_row`?

{% warning %}
We cannot use spaces in the name, so we use underscores `_` instead of spaces. Also by convention we don't capitalize in these names. All letters are lower case.
{% /warning %}

The code will look like this:

```python
def draw_5th_row():
    for i in range(8):
        sense.set_pixel(i, 4, r)
        time.sleep(0.5)
```

First, because we are defining a name for this block of code, so we use the keyword `def`, meaning "define". Also, we need to indent (tab) the entire block, which means the code that is already indented need to be indented further. Also, don't forget the colon `:`!

Now we run the code, nothing happens. Why?

That's because we have only defined this "named block." In order to use it, we need to call it. How do we make a call? With hands around mouth! (perform the action for the students) That looks like a pair of parentheses `()`, doesn't it!

```
draw_5th_row()
```

You can try calling this block multiple times. Don't forget to clear the LED matrix between calls.

Oh, and, we just wrote our first **function**!!!

### Free coding time (30 minutes)

* Write a function that draws a vertical line (on any column). You can pick and name you want.
* Write a function called `draw_diagonal()` that draws a diagonal line on your LED matrix.
* **(Challenge)** write a function that draws a circle on your LED matrix. (Hint: you can use 4 for-loops to do this, or 4 functions)

---

## Review and Assessment (5 minutes)

1. What is a "named block?"
2. How do you write a "named block?"
3. What are the advantages of functions (so far)?