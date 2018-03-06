+++
title = "Data Types"
date =  2018-02-26T21:35:52-05:00
weight = 11
pre = "<b>Lesson 7. </b>"
+++

---

## Lesson Information

In previous lessons, the students learned to use Python as a calculator,
to output messages to SenseHAT, and to use the `input()` function to get
user input from the Python Shell. In this lesson we will write a program
that mashes all these together. We formulate the concept of data types
and explain in detail why the number `123` is different from the string
`"123"` in Python. Unlike other sessions, this one takes about 2 hours,
with ample time for students to complete their project on their own.

{{% sidebar "Highlights" %}}

##### Computational Thinking Skills:

* **Abstraction**: Data types and conversion

##### Standard Alignments:

* Todo

##### Cross-discipline Applications:

* N/A

##### Duration

* 2 hours

{{% /sidebar %}}

#### The purpose of the lesson is to:

1. Deepen the understanding of data types
2. Explain how computers handle different data types differently
3. Review all students have learned so far

#### Driving Questions:

* What are data types?
* How do computers handle different data types?
* What are binary numbers?

#### Computer Science Concepts:

> data types, binaries, string concatenation

#### Materials Needed:

> Raspberry Pi 3 with SenseHAT, coins (or other chips),

### Target Skills:

1.  SWBAT perform simple binary conversion (under 10)
2.  SWBAT understand the differences between data types
3.  SWBAT perform data type conversion

---

## Instructional Plan and Structure

This lesson features a task that applies all the skills that the
students have learned previously and reintroduces the concept of data
types. It is a conceptual review of all of the topics covered in the
previous seven lessons.

### Overview of the lesson (5 minutes)

Explain to the students that on our first day with Python, we learned
how to use Python [as a sophisticated calculator](/unit1/lesson3).
However, at that time only we could use Python as a calculator. This
time we are going to write a calculator that asks someone else for
numbers and then do the calculation, so that someone else can use the
program as well.

Demonstrate to the students this code without showing them the content:

```python

# Initialization
from sense_hat import SenseHat
sense = SenseHat()

# Input
number1 = input("Give me number 1")
number2 = input("Give me number 2")

number1 = int(number1)
number2 = int(number2)

# Processing
result = number1 + number2
msg = "{0} + {1} is {2}".format(number1, number2, result)

# Output
sense.show_message(msg, text_colour = [255, 0, 0], back_colour = [0, 0, 255])

```

### Figuring it out together (10 minutes)

Ask the students to discuss in groups what they would write to achieve
this result. They will likely come up with the `input()` function, the
initialization, and the `sense.show_message()` function. As they
discuss, write this program:

```python

# Initialization
from sense_hat import SenseHat
sense = SenseHat()

# Input
number1 = input("Give me number 1")
number2 = input("Give me number 2")

# Processing

# Output
sense.show_message(number1 + number2, text_colour = [255, 0, 0], back_colour = [0, 0, 255])

```

Show the students what this program outputs.

### How do computers "see" numbers? (20 minutes)

So, rather than adding the numbers together, we only saw on SenseHAT
that the computer joined the numbers together. This is weird. Let's
figure out what is going on. Remember in the last class (Lesson 6), when
we used the `input()` function, what is the type of the value that we
got from it?

```python
>>> input("What is your name?\n")
What is your name?
Captain America
'Captain America'
```

Turns out that we got a `string` from this function. When we added
strings together, Python will join, or **concatenate**, them for us,
instead of adding them together.

```python
>>> 123 + 456
579
>>> "123" + "456"
'123456'
```

Why? It's because computers see things very differently from us.
Computers are only capable of seeing `0` and `1`. Those are called
binary numbers. For example, computers see `2` as `10`, and `3` as `11`.
How about `7`?

We can use {{% button href="https://github.com/digicosmos86/MicroInventor_Hugo/raw/master/content/unit1/lesson7.files/lesson7worksheet.pdf" icon="fa fa-download" %}}this worksheet{{% /button %}}

Use 7 coins, fill the columns with coins. However, remember, when you
are finished, the columns have to be either empty or full. After you are
finished, write a 0 under the columns that are empty, and a 1 under
those that are full. You should get `111` after this. How about `9`?

We can also use the `bin()` function in Python to get the binary
versions of numbers::

```python
>>> bin(7)
'0b111'
>>> bin(123)
'0b1111011'
>>> bin(255)
'0b11111111'
```

{{% notice note %}}

The `0b` prefix tells us that this is a binary representation. Actual
values come after `0b`. How many ones are in there in the binary version
of `255`? How about `1023`?

{{% /notice %}}

### How do computers "see" strings? (10 minutes)

How the computers see strings is a completely different story. First,
for each character, Python uses a number to represent them. We can use
`ord()` function to get them.:

```python
>>> ord("a")
97
>>> ord("A")
65
>>> ord("1")
49
```

Then we can use the `bin()` function to convert them to binary numbers.
The last step is to fill the number with preceeding 0s if there are
fewer than 0 digits.

```python
>>> bin(49) # "1" is actually 00110001 '0b110001'
```

We can use the following code to see how computers see `123` and
`"123"`:

```python
def int_to_bin(num):
    return bin(num)[2:]

def str_to_bin(string):
    return [bin(ord(ch))[2:].zfill(8) for ch in string]

if __name__ == "__main__":
    print(int_to_bin(123))
    print(str_to_bin("123"))
```

{{% button href="lesson7.files/binary.py" icon="fa fa-download" %}}Download the Code{{% /button %}}

This is what we get when we run the code::

    1111011
    ['00110001', '00110010', '00110011']

Because computers see data differently like this, they perform different
operations on different data types. What type takes more space to store?

### Coding using `int()` and `str()` functions (60 minutes)

Now that they have deeper understanding of the differences between data
types, the students can complete their coding tasks using type
conversions. They can begin with the code we wrote earlier::

```python
# Initialization
from sense_hat import SenseHat
sense = SenseHat()

# Input
number1 = input("Give me number 1") # What is the type of number1?
number2 = input("Give me number 2") # What is the type of number2?

# Processing

# Output
sense.show_message(number1 + number2, text_colour = [255, 0, 0], back_colour = [0, 0, 255])
# What is the type of number1 + number2 now?
```

### Challenges:

1. Change the program so that instead of doing addition, it does multiplication.
2. Unfortunately, if we provide the computer with decimal numbers, the
    calculations will be off. This is because the `int()` function only
    converts strings to integers (hence the name `int`). When we are
    using decimals, we can convert them using `float()`. Try to use this
    function in your program and test what happens.

---

## Review and Assessment

1. How do computers see data types differently?
2. How do we convert between different data types?
