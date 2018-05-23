+++
title = "Light and Plant Growth"
date =  2018-05-17T10:56:42-04:00
weight = 6
pre = "<b>Lesson 2. </b>"
+++

---

## Lesson Information

This lesson focuses on one factor that affects plant growth: **light**. We know that plants require light in order to perform photosynthesis, but not all types of light are needed for plant growth, and the light requirement vary plant by plant. In this lesson the students will learn colors of light (light spectrum) and the effect of different colors of light on plant growth.

{{% sidebar "Highlights" %}}

##### Computational Thinking Skills

* **Abstraction**: using abstractions (classes and objects)
* **Abstraction**: using data structures (lists)

##### CSTA Computer Science Standards

* **number**: description
* **number**: description

##### Cross-discipline Applications

* N/A

##### Duration

50 Minutes

{{% /sidebar %}}

#### The purpose of the lesson is to:

1. Explain the concept of light spectrum
2. Use the GrowLight class to control the LED strip
3. Explore the use of functions

#### Driving Questions:

* Why are most plants green?
* Why are most grow lights red and blue?
* How to control the GrowLight to do different things?

#### Science Concepts:

* **Light Spectrum**: is the many different wavelengths produced by a light source
* **Photosynthesis**: is a process used by plants and other organisms to convert light energy into chemical energy that can later be released to fuel the organisms' activities (energy transformation).

#### Computer Science Concepts:

* **Functions**: A function is a block of organized, reusable code that is used to perform a single, related action.
* **Function arguments (parameters**: Input for functions to produce different results
* **String vs numbers**: How programming languages differentiate text and number

#### Materials Needed:

> Wio Link board, LED strip, {{% button href="https://www.dropbox.com/s/7pi9lnz0b6m2peo/Lesson%202.%20Can%20plants%20see%20light.docx?dl=1" icon="fa fa-download"%}}Reading Meaterial{{% /button %}}

#### Target Skills:

1. SWBAT explain why plants need red and blue lights
2. SWBAT control the LED strip to do different things
3. SWBAT tell the difference between "text (strings)" and numbers in Python.

---

## Instructional Plan and Structure

### Do Now - Review of Concepts (5 minutes)

* What does a greenhouse do?
* What are some common operators and functions in Python?
* What is a module and how to use a module?

### Why are Grow Lights so Red and Blue? (15 minutes)

Ask the students why greenhouses are transparent. Explain to the students that a greenhouse usually needs to maximize the amount of light going in, so that the plants can use the light to perform **photosynthesis**. If there is not enough light, what can greenhouses do?

Well, it turns out that we can use artificial light sources. Connect the LED strip and turn it on without letting the students see the code. The LED strip turns on and only shows two colors - red and blue. Why is that? Actually, most of the plant grow lights are red and blue. [See this Google Image Search result](https://www.google.com/search?q=plant+grow+light&safe=off&biw=1310&bih=714&tbm=isch&source=lnms&sa=X&ved=0ahUKEwiljonkrZXbAhWSq1kKHRt3BlQQ_AUIigIoAQ).

Why are are these commercial grow lights also red and blue? The [reading material]() explains it perfectly:

Plants have adapted, over millions of years, to use sunlight as their source of energy to grow through the process of photosynthesis. In photosynthesis a plant produces sugar when a plant’s chlorophyll is exposed to light with a wavelength of in the visible part of the light spectrum of 400–700 nanometers. The amount of sugar is almost directly proportional to the intensity of the light. We can use this knowledge to expose plants to light of a specific frequency during each phase of its development.

![light spectrum](http://eyelighting.com/wp-content/uploads/2018/02/quality-of-a-light-source.jpg)

Why red and blue lights?

It is important to note that all visible colors of the light spectrum are used by plants but blue and red are very important for plants.  The reason is that the chlorophyll cells in plants are very good at absorbing and using both blue and red light.  Blue light drives the photosynthesis process and promotes good root development.  If plant is receiving plenty of blue light it should have thick leaves, strong stems and will be shorter (but healthier). Red light also helps a plant grow but is particularly important for flower production. 

### How to turn on the Grow Light? (10 minutes):

Now that we know why we need red and blue lights, let's turn on our grow lights. In this course, it is a general rule that you can interact with a device with these three steps (refer to the cheat sheet).

1. Connect the device to a port. Different devices use different ports. Please see the cheat sheet for the ports that we recommend for different devices.
2. From the appropriate module import the appropriate device name. Specify a shortcut name and the port number.
3. Using the shortcut name you have specified, perform an action. The list of actions are available on your cheat sheet. More available actions can be found on the [documentation website](http://growthings.readthedocs.io/en/latest/api.html).

``` python
from displays import GrowLight
gl = GrowLight(port=1)

gl.on()
```

### Free coding and challenges (15 minutes)

* Turn on the Grow Light
* Make the Grow Light blink
* Make the Grow Light blink in different colors, for different times, and for different intervals.
* Make the Grow Light do a demonstration - change to different programs

---

## Review and Assessment (5 minutes)

Upload your final code to Google Classroom

### Exit slip

1. What is light spectrum and why are there different colors of light in sunlight?
2. How to control the Grow Light to do different things?

### Video diary
