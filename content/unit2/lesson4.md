+++
title = "Abstraction with Functions - Single Parameter"
date =  2018-03-26T12:57:28-04:00
weight = 8
pre = "<b>Lesson 4. </b>"
+++

---

## Lesson Information

In this lesson the students will learn how to vary the behavior of functions according to inputs - **Parameterization**. We will familiarize them with the concept of parameterization with real-world examples from other disciplines. We will only focus on functions with a single parameter for now, but we will go deeper and talk about how to use one-parameter functions with for loops.

{{% sidebar "Highlights" %}}

##### Computational Thinking Skills

* **Abstraction**: Build and use functions with one parameter
* **Automation**: Varying function behavior with parameters
* **Analysis**: Reason why we need parameters

##### Standard Alignments

TODO

##### Cross-discipline Applications

* Again, functions with parameters are everywhere in our daily life.

##### Duration

1 hour

{{% /sidebar %}}

#### The purpose of the lesson is to:

1. Understand the concept of parameterization
2. Learn the syntax of defining a function with one parameter
3. Discuss the benefit of parameterization

#### Driving Questions:

* What are parameters in functions?
* What are real-life equivalents of function parameters?
* Why do we need function parameters?
* How do we define functions with one single parameter?

#### Computer Science Concepts:

> Parameters (also called arguments), formal parameters

#### Materials Needed:

> Raspberry Pi + SenseHAT

#### Target Skills:

1. SWBAT understand and use one-parameter functions
2. SWBAT write `draw_line()` functions to draw arbitrary lines on the LED matrix
3. SWBAT articulate the difference between formal parameters and actual parameters

---

## Instructional Plan and Structure

### Overview of the lesson (xx minutes)

In the previous lesson we learned how to give names to "code blocks" a.k.a. functions, so that we can do a series of things with one function call. Now let's write a function that "sings" a happy birthday song to someone, for example, Caitlin (feel free to use any other names). How do we do that?

### Class Activity - Happy Birthday (10 minutes)

Well actually it's quite easy to do. We can write a function called `happy_birthday_caitlin()` to do so:

```python
def happy_birthday_Caitlin():
    print("Happy Birthday to You")
    print("Happy Birthday to You")
    print("Happy Birthday, dear Caitlin")
    print("Happy Birthday to you")

happy_birthday_Caitlin()
```

Easy, isn't it. But wait. It's Emily's birthday, too. So we write a song to Emily as well:

```python
def happy_birthday_Caitlin():
    print("Happy Birthday to You")
    print("Happy Birthday to You")
    print("Happy Birthday, dear Caitlin")
    print("Happy Birthday to you")

def happy_birthday_Emily():
    print("Happy Birthday to You")
    print("Happy Birthday to You")
    print("Happy Birthday, dear Emily")
    print("Happy Birthday to you")

happy_birthday_Caitlin()
happy_birthday_Emily()
```

Now we've got a problem. For each person, we have to write a new function. That's not convenient at all. Can we write only one function that keeps everything else the same, but only changes the name of the person?

Absolutely!! Let's look at this function.

```python
def happy_birthday(person):
    print("Happy Birthday to You")
    print("Happy Birthday to You")
    print("Happy Birthday, dear " + person)
    print("Happy Birthday to you")

happy_birthday(person="Caitlin")
happy_birthday("Emily")
```

Works out perfectly. Now let's take a look at what is going on here.

### Function Parameters - One Parameter (10 minutes)

The first thing that we notice is that in the function definition header `def happy_birthday(person):`, there is something called person. This person is called a **formal parameter**, which means it is there for formality. It serves as a placeholder. Here's an example of a placeholder. On facebook (or any social media), whenever someone doesn't have a profile picture, the website will use a placeholder like this: ![placeholder](https://pbs.twimg.com/profile_images/728424402929352705/RNjnnveq_400x400.jpg)

The website will replace this placeholder with the actual profile picture as soon as one is uploaded.

Here it's the same. `person` is just a placeholder for this function. When you call the function like `happy_birthday(person="Caitlin")`, Python will replace `person` with the value it's assigned to (`"Caitlin"`), so we get the birthday song for Caitlin.

{% note %}
We are not unfamiliar with the concept of placeholders. In a for-loop, such as `for i in [1, 2, 3]:`, the variable `i` is also a placeholder, which will be replaced with actual values in the actual loop.
{% /note %}

{% hint %}
Since we only have one parameter here, we do not have to specify the name of the placeholder here. We can simply call `happy_birthday("Emily")`
{% /hint %}

### Drawing arbitrary lines (10 minutes)

In the previous class we wrote a function called `draw_fifth_row()`. However, if we need to draw a line on a different row, we had to write a new function. Now that we know function parameter, we can write a function called `draw_row()`, and we can pass a parameter to it to change on which row the function draws.

```python
def draw_row(row):
    for i in range(8):
        sense.set_pixel(i, row, r)
        time.sleep(0.5)

draw_row(row=1)
draw_row(2)
```

### Free coding time (30 minutes):

* Write a function that takes one parameter so that you can draw on any column on the LED matrix
* Use a for-loop to fill the LED matrix row by row, or column by column. Don't worry about colors yet.
* **Challenge**: Wow, 5 students are celebrating their birthday today.  Their names are `["Jackie", "Andre", "Jason", "Bridget", "Tiffany"]`. Use a for-loop and the function `happy_birthday`, print out Happy Birthday" songs for all of them.

---

## Review and Assessment

1. How do we define and call functions that have only one parameter?
2. What are "formal parameters", or placeholders?