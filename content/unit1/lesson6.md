+++
title = "Input and Output"
date =  2018-02-26T21:18:01-05:00
weight = 10
pre = "<b>Lesson 6. </b>"
+++

---

## Lesson Information

In the previous lesson, the students learned how to *output* a message
to the shell and the SenseHAT LED Matrix. This is an example of
controlling the output of a program. Later the students will also learn
how to output to another machine. In this lesson, we will build on this
knowledge and continue to learn the structure of a program: Input -
Process - Output, beginning by studying what inputs are and how to use
inputs.

{{% sidebar "Highlights" %}}

##### Computational Thinking Skills

* **Abstraction**: Input and Output
* **Automation**: Processing input and producing output

##### Standard Alignments

* Todo

##### Cross-discipline Applications

* The same concept of input and output can be applied to mathematics too.

##### Duration

* 1 hour

{{% /sidebar %}}

#### The purpose of the lesson is to:

1. Formulate the concept of output (between shell and SenseHAT)
2. Use pre-defined variables in programs as input
3. Reinforce the idea of input using the `input()` function
4. Introduce process chart as a graphical visualization of programs

#### Driving Questions:

* What are input and output in a program?
* What is the structure of a program?
* What is a process chart and how do we use it?

#### Computer Science Concepts:

> input, output, programming flow

#### Materials Needed:

> Raspberry Pi 3 with SenseHAT

### Target Skills:

1. SWBAT differentiate outputs to shell and to SenseHAT
2. SWBAT use pre-defined variables as input in their programs
3. SWBAT understand process charts
4. SWBAT use the `input()` function to customize their input.

---

## Instructional Plan and Structure

> It should be obvious that most, if not all, programs are devoted to
> gathering data from outside, processing it, and providing results back
> to the outside world. That is, input and output are key.
>
> *Real World Haskell*, Bryan O'Sullivan, Don Steward, & John Goerzen.

### Overview of the lesson (10 minutes)

In the previous lesson, we wrote a program like this::

    from sense_hat import SenseHat
    sense = SenseHat()

    sense.show_message("Hello Python", scroll_speed = 0.05, 
                       text_colour = [255, 0, 0], back_colour = [0, 0, 255])

Begin the class by reviewing these questions. The students may discuss
these questions in groups first and then share these questions with the
rest of the class.

1. What/where is this program outputting the message to?
2. Can we output the message to other places/devices? How can we do so?
3. Can you imagine where else we might output this message to?

This image below could help you answer the above questions:

![image](https://cdn-images-1.medium.com/max/1400/1*-OQi5hp-uoL_KdIydr4hew.gif)

### What is a program? (10 minutes)

The above image demonstrates what a program consists of. We can think of
programs as the mysterious machine shown in the image. It takes some
input, do some processing, and produces some output. In the case of the
program we have written, we know that we output the message to the
shell/SenseHAT. More formally, a program looks like this:

{{< mermaid align="center" >}}
graph LR;
    A(Input) -->B{Processing}
    B --> C(Output)
{{< /mermaid >}}

Then, what is our input in this program? Ask the students to discuss in
groups and guess.

The inputs are basically the parameter values that we pass to the
`sense.show_message()` and `print()` functions. If this is not clear
enough, we can actually restructure our program this way so that this
structure is clearer.

```python
# Initiation:
from sense_hat import SenseHat
sense = SenseHat()

# Input:
msg = "Hello Python!"
speed = 0.05
red = [255, 0, 0]
blue = [0, 0, 255]

# Process

# Output
sense.show_message(msg, scroll_speed = speed, 
                   text_colour = red, back_colour = blue)
```

{{% notice note %}}

The pound/hashtag sign `#` starts a comment. You can write your notes in
the code this way and Python will ignore it. Other languages may use
double slash `//` to do so. Here we use comments to divide our code into
initialization-input-process-output sections. Comments will be greyed
out in **Thonny Python**, which also means that these comments will be
ignored.

{{% /notice %}}

{{% notice tip %}}

We only need to initialize the program once. We usually import libraries
at the beginning of our code.

{{% /notice %}}

{{% notice note %}}

Notice that the `# Process` block. Are there no processing step in our
program?

{{% /notice %}}

What did we just do in this program?

Well we just defined a few variables at the beginning of program and
then passed them to the `sense.show_message()` function as parameters.
Take a look at the Variable panel in your **Thonny Python**:

TODO: add a Thonny Python screenshot.

When Python reads Line 14, it will automatically look up all these
variables and substitute them with their values. So the code will
eventually become something we are familiar with:

    sense.show_message("Hello Python", scroll_speed = 0.05, 
                    text_colour = [255, 0, 0], back_colour = [0, 0, 255])

{{% notice tip %}}

It is better to demonstrate the process of substituting values with
variables to the students.

{{% /notice %}}

We don't need to write all programs this way but since we are learning
to code, it is a good idea for us to stick to this structure for a while
so we understand what is going on.

### Restructure your program (15 minutes)

In the previous class we wrote code to have Python output 3 messages to
SenseHAT/shell. Rewrite the program using the input-process-output
structure provided above and still have Python output three messages.

{{% notice tip %}}

You might want to have different variables as inputs, such as `msg1`,
`msg2`, `msg3`, etc.

{{% /notice %}}

### The `input()` function (15 minutes)

So far we have only pre-defined messages for SenseHAT to print. Can we
get this input dynamically from the user using our program? In other
words, can we prompt the user to *input* a message that we can then
output to SenseHAT/shell?

The `input()` function can help us do that:

```python
>>> input("What is your name?\n")
What is your name?
Captain America
'Captain America'
```

What do you think the function does?

The `input()` function takes a string. It will display this string in
the shell as a prompt, and the user can type in something there. Then
the `input` function will take whatever the user typed in the shell and
*return* it. What is the type of the returned value?

{{% notice note %}}

The `\n` is a `newline` character, so that you can answer the question
on a new line.

{{% /notice %}}

We can also save the returned value of this function to a variable so we
can use it later:

```python
>>> name = input("What is your name?\n")
What is your name?
Captain America
>>> name
'Captain America'
>>> "my name is " + name
'my name is Captain America'
```

Of course, we can output result to SenseHAT:

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

**Challenge:**

* Ask two different questions and output those results to SenseHAT. Make the outputs look different by using different colors and speed.

---

## Review and Assessment

1. What are input and output?
2. How do we use the `input()` function?
3. What is the common structure of a computer program?
