+++
title = "Light Intensity and Plant Growth"
date =  2018-05-17T10:57:00-04:00
weight = 7
pre = "<b>Lesson 3. </b>"
+++

---

## Lesson Information

In the the Boston area we get nearly 15.5 hours of sunlight in the middle of Summer, however, in March and April Boston receives around 11 and in the middle of winter we get about 9 hours of sunlight.  Most plants require 12 hours of sunlight per day to grow well and if you are a greenhouse owner and you want to grow plants year round artificial light will be needed to grow plants.  Or if you want to grow light plant indoors artificial lights will be needed.  However, lights cost money to run so it would be good to know if your plants are getting enough light from natural sources and only use additional artificial light when needed.

In this lesson you will learn how to measure light intensity, measured in lux and how to use that information to turn on and off a GrowLight.

{{% sidebar "Highlights" %}}

##### Computational Thinking Skills and Concepts

* **Automation**
* **Controls and Loops (If-Then-What)** (Optional, for more advanced students)

##### CSTA Computer Science Practices

* **Practice 1**: Recognizing and Defining Computational Problems
* **Practice 2**: Creating Computational Artifacts

##### Cross-discipline Applications

Light is a form of electromagnetic energy and plants, particularly most vegetables, need both blue and red light to produce their own food.  The blue and red light activate the chlorophyll cells that enable photosynthesis to occur.

##### Duration

30 to 45 minutes

{{% /sidebar %}}

#### The purpose of the lesson is to:

1. Learn how to use light sensor to measure light intensity
2. Learn how to graph data and use that to make predictions

#### Driving Science Questions:

* How does the amount of light affect plant growth?
* Is my grow light going to be efficient enough for my plants?

#### Science Concepts:

* **Light Energy**: is the only form of **energy** that we can actually see directly.  Plants use light across the visible spectrum but especially the high energy blue and lower energy red photons.

#### Computer Science Concepts:

* **Automation**: Use code to enable hardware to collect data and to impact its surroundings by itself
* **Abstraction**: Collect data using electronic devices

#### Materials Needed:

> Wio Link board, digital light sensor, two connector cables, 1 LED GrowLight, rulers, {{% button href="https://www.dropbox.com/s/7iga8k361xscfia/Lesson%203.%20Light%20intensity%20and%20duration%20impact%20on%20plant%20growth%20DVSM.docx?dl=1" icon="fa fa-download"%}}Reading Material{{% /button %}}

#### Target Skills:

1. SWBAT program and code a Light Sensor
2. SWBAT use data from the Light Sensor to control a GrowLight

---

## Instructional Plan and Structure

### Do Now (Review Questions)

In your composition notebook, write down answers to these two questions:

1. What aspect of plant growth is red light specifically helpful for? How about blue light?
2. Write down code to blink the LED strip 5 times, in .1 second intervals, and in color blue. The LED strip is at Port 2.

### Overview of the lesson

In the last lesson we learned how to turn on/off our LED grow lights. The LEDs are in red and blue, the desired colors for the plants. However, have you wondered whether these lights will be bright enough sufficient for your plants? Can it replace sunlight for our plants? Today we are going to learn how to measure the **light intensity** of our grow lights. This is going to help us make decisions about where we put our LED lights in the smart greenhouse.

### Activity 1:  `get` a Light Sensor Reading

Start by introducing the do now:

``` python
from sensors import LightSensor
ls = LightSensor(port=6)
ls.get_lux()
```

To get a light sensor reading is relatively straightforward. One just needs to import the LightSensor, assign a variable, say ls, and use the `.get_lux()` function to get the lux level.  The code for this is just three lines and is:

{{% notice tip %}}

Note that the light sensor has to go on port 6, because it is an I2C device. Also, when you are working with sensors, (that is, whatever you import from the `sensors` module), you always use `get_xxx()` to get a reading, whether it is moisture, light intensity(lux), or temperature/humidity, which we are going to use in the future.

{{% /notice %}}

Create a new file and write down the above lines. Run the script, and you should be able to see a light sensor reading in the terminal.

Move your light sensor around and run the program a few times to make sure that your light sensor is working.  Now like we will want to be able to use the light sensor information to do something.

Alter the ambient light condition and repeat the readings. What are the light readings with the lights on/off? With the curtains drawn/not drawn? Are there differences between light sensors close/away from the windows? Facing the windows?

### Activity 2: make a graph using the light sensor readings

Now that we can measure light intensity, how about our own grow lights? If you are going to install the grow lights inside the greenhouse, what are some decisions you might have to make? Discuss with your partner.

Here are a couple of questions that might be helpful. Where do I put the grow light?  How close should they be to the plants? Are my grow lights strong enough to replace sunlight?

There are two types of lights on the grow light - red and blue ones. Are they as bright as each other? Why or why not?

Now let's use our light sensor to answer these questions. Turn on your Grow Light (see the script below). Place your light sensor at different distances from the red and blue lights, for example, 0 inches, 0.5 inches, 1 inch, etc. Record the lux readings on {{% button href="https://www.dropbox.com/s/y1kmjj8qau94csr/Lesson%203.%20Light%20Sensor%20Worksheet.docx?dl=1" icon="fa fa-download" %}}this worksheet{{% /button %}}.

When you have finished recording your data, graph the data in the blank spaces on the worksheet. Use different color lines for blue and red lights.

Answer the following questions:

* Are blue and red lights different in light intensity?
* What did you notice from the graph?
* What might be some of the reasons why your graph looks this way?
* What is the relationship between distance and light intensity?

### Activity 3: For advanced students or classes with extra time

#### Control individual lights

The first step of controlling individual lights on the LED strip is the same:

``` python
from displays import GrowLight
gl = GrowLight(port=1)
```

Now you can assign individual colors to the GrowLight with this syntax:

``` python
gl[0] = [255, 0, 0]
gl.write()
```

This sets the first light to red. In the square bracket on the left of the equal sign, the number is the index of each individual light on the strip. This index starts with `0`, so the first light is 0, and the second is `1`, and so on. On the right of the equal sign is the color in `[R, G, B]`. The square bracket makes sure that the three individual numbers are read as a whole by Python, not three individual numbers.  They collectively have a meaning. The gl.write() actually sets the colors. This means, you can set more colors before calling gl.write:

``` python
gl[0] = [255, 0, 0]
gl[1] = [0, 255, 0]
gl[2] = [0, 0, 255]
gl.write()
```

We can think of the LED matrix as a list holding each individual colors like this:

![List](list.jpg)

We can put each individual colors in these cells, and then call `gl.write()` to actually set all these colors to the LED strip.

#### Setting multiple LEDs at once

We will need a **for loop** to do this. **For loop** is a more sophisticated structure that we might come back to in the future, so don't worry about it if you don't know what the following means:

``` python
for i in [0, 1, 2, 3, 4]:
    gl[i] = [255, 0, 0]
gl.write()
```

Run the code and see what happens.

Now try to change the numbers in `[0, 1, 2, 3, 4]` and see what happens. How about this line?

``` python
for i in [0, 2, 4, 6, 8]:
    gl[i] = [255, 0, 0]
for i in [1, 3, 5, 7, 9]:
    gl[i] = [0, 0, 255]
gl.write()
```

Again, feel free to modify the code and see what happens.

## Review and Assessment (5 minutes)

Please upload your final code to Google Classroom. Save your file in the format of `wa1-0529.py`.

### Exit slip

1. What is the relationship between distance and light intensity?
2. How to use the light sensor to measure light intensity (Write down the code)? What is the unit of the light intensity that we use here?

### Video diary

* What did you learn about science today? Did you have any problems understanding it? Why or why not?
* What did you learn about coding today? Did you have any problems understanding it? Why or why not?
* What do you want to learn tomorrow?