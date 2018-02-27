+++
title = "A Sophisticated Calculator"
date =  2018-02-26T18:07:34-05:00
weight = 7
pre = "<b>Lesson 3. </b>"
+++

---

## Lesson Information

This lesson introduces the students to the basic mathematical and string
operations in Python. Although we will not formally formulate the
differences between data types, they will have first hand experience of
the differences between numeric types and string types. They will also
have basic concepts of variables and how to store values in variables.
Using interactive programming, the students will use Python to solve
mathematical problems in Python and print it out.


{{% sidebar "Highlights" %}}

##### Computational Thinking Skills

* **Abstraction**: What is computation?

##### Standard Alignments

* N/A

##### Cross-discipline Applications

* Students will learn the connection between programming and mathematics.

##### Duration

* 1 hour

{{% /sidebar %}}

#### The purpose of the lesson is to:

1. Introduce students to Python programming using the interactive shell
2. Familiarize students with mathematical operations in Python
3. Informally introduce the concept of data types and variables
4. Use Python to solve mathematical problems

#### Driving Questions:

* What does computation mean?
* How can we use computation in Python?
* What are the differences between numbers and strings?
* How can we save the result of our computation?

#### Computer Science Concepts:

> Mathematical operators, primitive data types (string and numbers), variables (storing values)

#### Materials Needed:

> Raspberry Pi 3

#### Target Skills:

1. SWBAT use mathematical operators to work on math problems in Python shell
2. SWBAT informally distinguish the differences between data types
3. SWBAT understand one reason why we need variables

---

## Instructional Plan and Structure

### Overview of the lesson (5 minutes)

Why do we call computers computers? What do we mean by computation?
Begin the class by asking the students these questions, and engage them
in a brief whole-class discussion. Then, introduce the students to the
topic of this class: mathematical computations.

### Let's Code Together! (30 minutes)

Start a Python shell (either in **Thonny Python** or the **terminal**),
and if possible, also start a Linux calculator on the side or use a real
calculator, so students understand that Python can be used as a
sophisticated calculator. Start typing in basic math operations, such as
`5 + 10` and `1.2-1.0`. Addition and subtraction might be easy, but some
students might not be familiar with the multiplication `*` operator, the
division `/` operator, and/or the exponentiation operator `**`. Make
sure they locate these operators on the keyboard. The exponentiation
operator can be used to obtain really large numbers, which Python
handles well. Make sure the students have the chance to experience that.

{{% notice tip %}}

The result of `1.2-1.0` might not be unexpected. It has something to do
with the way Python represents floating numbers, and we will get back to
that more formally later in this course. Also, it does **NOT** matter if there are spaces between values and
operators.

{{% /notice %}}

Here are the basic mathematical operators in Python:

Python operator  |Mathematical Operator
-----------------|-----------------------
`a + b`          |\\(a+b\\)
`a - b`          |\\(a-b\\)
`a * b`          |\\(a \times b\\)
`a / b`          |\\(a \div b\\)
`a ** b`         |\\(a^b\\)

It is possible to carry out complicated operations. The order in which
each operation is performed is exactly the same as what students are
familiar in math. It is, of course, possible to change the precedence by
using the parenthesis `()`.

With this knowledge, let's do some math! The following two questions
are taken from [6th Grade MCAS Math released
problems](http://www.doe.mass.edu/mcas/2016/release/Gr6-Math.pdf).

* At the beginning of the day, a water tank contained 526.8 gallons of water. During the day, some of the water was used to water a garden. At the end of the day, the water tank contained 318.05 gallons of water. What was the total amount of water used that day?
* Which of the following expressions have the largest value?

    1. \\(2^3+2^3\\)
    2. \\(2^3+7^1\\)
    3. \\(3^2+3^2\\)
    4. \\(3^2+7^1\\)

### Saving the results of our computation (10 minutes)

Just like we want to save the games that we have played for a while,
sometimes we want to save the results of operations so that we can use
them in the future. We can achieve this by using **variables**. For
example:

```python
>>> a = 2**5 
>>> b = (3+10)* 8
```

The computer will associate these names with the values, and later when
we use them, we can just use the name:

```python
>>> a
32
>>> b
104
>>> c = a + b
>>> c
136
```

{{% notice note %}}

What happens if we write `a = a + b`?

{{% /notice %}}

### Numbers and Strings (10 minutes)

What if we want to use texts in Python? Unfortunately, if we use texts
directly like this:

```python
>>> Hello Python!
File "<stdin>", line 1
    Hello Python!
            ^
SyntaxError: invalid syntax
```

As you can see we encountered an error called `SyntaxError`. This means
Python does not understand what we just wrote. In Python (and most
programming languages), texts are put in quotation marks. For example:

```python
>>> "Hello, Python!"
'Hello, Python!'
```

{{% notice tip %}}

Single quotation marks `'` or double `"`? It doesn't matter as long as they match.

{{% /notice %}}

What if we put numbers in quotation marks?

```python
>>> "123" + "456"
'123456'
```

We got unexpected results!!! And when we do this:

```python
>>> "123" + 456
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: must be str, not int
```

We got a `TypeError`!!! We will discuss that in our next lesson.

## Review and Assessment

Answer the following review questions:

1. What is computation?
2. What is one type of computation Python is really good at?
3. Why do we need variables?
