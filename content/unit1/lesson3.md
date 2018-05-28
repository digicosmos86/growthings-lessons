+++
title = "Lights, Buttons, and Lux"
date =  2018-05-17T10:57:00-04:00
weight = 7
pre = "<b>Lesson 3: </b>"
+++

---

## Lesson Information

A challenge with greenhouses in the Boston area is that in the fall and spring the daylight hours can be rather short.  Most plants need at least 8 hours of light to grow well.  In fact, some plants need at least 12 hours of light to grow well.  In this activity you will learn:

- how to measure the amount of light shining on your greenhouse using a light sensor
- how to use a button to turn on and off your LED strip if you need to manually increase the amount of light to your house.
  
{{% sidebar "Highlights" %}}

##### Computational Thinking Skills and Concepts

- Data Collection
- Algorithms and Procedures

##### CSTA Computer Science Practices

- **Practice 1**: Recognizing and Defining Computational Problems
- **number**: Creating Computational Artifacts

##### Cross-discipline Applications



##### Duration

30-45 minutes for the temperature and humidity sensor and 30-45 minutes for the connecting and programming of the relay.

{{% /sidebar %}}

#### The purpose of the lesson is to:

1. Learn how to measure light intensity
2. Learn how to manually control your LED strip

#### Driving Questions:

- How can I determine the amount that my greenhouse is receiving?
- How can I control my LED strip?

#### Science Concepts:

- **Lux**:  is the basic unit for light intensity.  It is one lumen per square meter. 
- **Lumen**:  a measure of the total amount of visible light emitted by a source. For example, a light bulb is rated at 400 lumens or 800 lumens.  The more lumens the brighter the bulb.


#### Computer Science Concepts:

- **Automation**: Use code to enable hardware to collect data and to impact its surroundings by itself 
- **While Loop**: A coding structure that tests a condition and if that condition is true an action is taken  if it is not true something else is done. This loop can repeat forever until the program is interrupted

#### Materials Needed:

![light lesson picture](https://lh3.googleusercontent.com/cdBml57bVKexJpEdtVdXnyzzNI1g5PGAAZGX7azDxD-7Y5pvDa5nQcghcqfy7qNH37rf1dKeXIb-)
Digital Light Sensor, Wio_link Board, 3 cable connectors, USB cable, LED light strip, Button

#### Target Skills:

1. SWBAT connect light sensors and measure light levels
2. SWBAT build a basic button control
3. SWBAT learn how to create a simple while Loop

---

## Instructional Plan and Structure

There are three components to this lesson.

- Part 1:  Use a button to control your LED Strip
- Part 2:  Connect a Light Sensor to record Lux
- Part 3:  Set up a program to continuously record Light readings and to do so at regular times

### Overview of the lesson

The purpose of this lesson is to learn how to create a simple control for your LED light strip using a button. One of the core problems with greenhouses often involves the amount light that a plant receives.  Plants absorb mostly blue and red light as they are different frequencies of energy that the different chlorophyll cells in a plant use to make its food.  In systems that use artificial light the problem is also distance from the light source.  The further a plant is from a light source the less energy that plant receives.  In fact, the intensity of light decreases rapidly the further the plant is away from the light.  Light intensity behaves follows an inverse square law rule which means that if the light if one has a light that is 1 meter away from a plant and another light that is 2 meters from a plant.  The plant that is one meter from the plant receives 4 times as much energy.

### Do Now (5-10 minutes)

In the previous lesson you learned how to hook up a LED strip and write code to turn on and off  and control that light strip.  Can you write the lines of code that you used to connect your LED strip to port 3 of your board and to have the light turn on and then go off after 6 seconds?

### Activity 1: Controlling the LED grow light with a button

What is the first thing we need to do when starting a new program?  We need to import sensors or objects to our board.  As we have learned the LED strip is a display and a button is an object called an actuator.  An actuator is an object that causes something else to move to change. 

So we need to import our GrowLight and our Button

``` python
from displays import GrowLight 
from actuators import Button
```

Now do you remember what is the next step?  We need to define the variables and the port that the GrowLight and the Button are attached to the board.  Lets put the GrowLight on port 1 and the Button on port 2.  So our next lines of code are:

``` python
gl = GrowLight(1)
b = Button(2)
```

What if we wanted the GrowLight to come on if we are pressing the button? 

We need to tell the board what will happen IF the Button is pressed and what will happen if the button is not pressed.  This is a if, else statement.  an If-else statement means that if a condition is true then do something, if it is not true then do something else.  So our code will look like

``` python
if b.is_pressed():
    gl.on()
else:
    gl.off()
```

NOTE: the : at the end of the if and else lines and the indention in the the if-else loop.  The colons tell python that the next line of code is part of the same statement and to run that code if the condition is true.  You will likely get an error if you forget one of the colons.

Now your complete program should look like this:

``` python
from displays import GrowLight
from actuators import Button

gl = GrowLight(1)
b = Button(2)

if b.is_pressed():
    gl.on()
else:
    gl.off()
```

If you haven't connected your board to your computer do so and run the program.  Be sure to hold down the button as you hit the run button in your programming environment and see what happens?
What happens when you start the program and you are not holding down the button?

### Activity 2:  Improving your Button

So you have learned how to turn on and off the GrowLight depending on whether the button is pressed or not.  This is not very useful as you can't control your GrowLight with the button as the program ends and just stops and you left with either an on GrowLight or an off Growlight.

We need to be able to turn on and off the GrowLight.  You need to use a new function called a While loop.  While loops are conditional loop that tells python that if a condition is True then do something and if it is False then do something else. 

In our code we will need to add in a while loop right above the if statement:

``` python
from displays import GrowLight
from actuators import Button

gl = GrowLight(1)
b = Button(2)

while True: 
    if b.is_pressed():
        gl.on()
    else:
        gl.off()
```

Your program should now run forever and what do you think will happen when you press the button? What happens when you release the button?

### Challenges

For help with the button and Growlight go here:
http://growthings.readthedocs.io/en/latest/displays.html#grow-light 

Challenge #1:  Have the GrowLight blink white when the button is pushed

{{% expand "Expand to see answer" %}}

``` python
from displays import GrowLight
from actuators import Button
gl = GrowLight(1)
b = Button(2)
while True:
    if b.is_pressed():
        gl.blink()
    else:
        gl.off()
```

{{% /expand %}}

Challenge #2:  Blink the LED light all RED and really fast

{{% expand "Expand to see answer" %}}

``` python
from displays import GrowLight
from actuators import Button
gl = GrowLight(1)
b = Button(2)
while True:
    if b.is_pressed():
       gl.blink([255,0,0], 60,.1)
    else:
       gl.off()
```

{{% /expand %}}

Challenge #3:  Have your GrowLight come on only after the Button has been pressed for 3 seconds

{{% expand "Expand to see answer" %}}

``` python
from displays import GrowLight
from actuators import Button
import time
gl = GrowLight(1)
b = Button(2)
delay = 3
while True:
    if b.is_pressed():
       time.sleep(delay)
       gl.on()
    else:
       gl.off()
```

{{% /expand %}}

Challenge #4:  Have the LED light blink red, white, then blue when the button is pressed but be solid blue when the button is not pressed

{{% expand "Expand to see answer" %}}

``` python
from displays import GrowLight
from actuators import Button
import time
gl = GrowLight(1)
b = Button(2)
while True:

    if b.is_pressed():
        gl.blink([255,0,0], 1, 1)
        gl.blink([0,255,0], 1, 1)
        gl.blink([0,0,255], 1, 1)
    else:
        gl.on()
```

{{% /expand %}}

---

## Review and Assessment (5 minutes)

Please upload your final code to Google Classroom. Save your file in the format of `wa1-0529.py`.

### Exit slip

1. How does light intensity affect plant growth?
2. How to use the light sensor to measure light intensity? What is the unit of the light intensity?

### Video diary
- What did you learn about science today? Did you have any problems understanding it? Why or why not?
- What did you learn about coding today? Did you have any problems understanding it? Why or why not?
- What do you want to learn tomorrow?

### If you are interested...

Play around with the Button and GrowLight and see what else you can control with the Button.  For example, can you make a program that will allow you to push the button and have the light go on and then push the button and have the light go off? 

Learn more about actuators and buttons here:
http://growthings.readthedocs.io/en/latest/actuators.html
