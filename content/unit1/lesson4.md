+++
title = "Temperature, humidity, and plant growth"
date =  2018-05-31T08:02:39-04:00
weight = 8
pre = "<b>Lesson 4. </b>"
+++

---

## Lesson Information

In this lesson the students are going to learn why temperature and humidity are crucial to plant growth. They are going to use the temperature sensor to measure temperature/humidity and display the information on the OLED screen using the **while loop**.

{{% sidebar "Highlights" %}}

##### Computational Thinking Skills

* **Abstraction**: Passing an object as a function argument
* **Abstraction**: Differences between data types
* **Automation**: Using **infinite loops** and **time control**

##### CSTA Computer Science Standards

* **number**: TODO
* **number**: TODO

##### Duration

45-50 minutes

{{% /sidebar %}}

#### The purpose of the lesson is to:

1. Understand the science behind temperature/humidity and photosynthesis
2. Learn to use loops, more specifically, infinite loops

#### Driving Science Questions:

* How are temperature and humidity conditions related to plant growth?

#### Science Concepts:

* **Relative humidity**: the amount of water vapor in the air relative to the maximum amount of water vapor that the air can hold at a certain temperature.
* **Stomata**: a pore, found in the epidermis of leaves, stems, and other organs, that facilitates gas exchange.

#### Computer Science Concepts:

* **loops**: a sequence of instructions that is continually repeated. An infinite loop never stops.
* **String**: any finite sequence of characters.
* **Sample rate**: the rate at which data is read or transferred.

#### Materials Needed:

> Wio Link board, Temperature/humidity sensor pro, OLED screen, {{% button href="https://www.dropbox.com/s/buh5mibeuj5a4pt/Lesson%204.%20Temperature%2C%20humidity%2C%20and%20plant%20growth.docx?dl=1" icon="fa fa-download"%}}Reading Material{{% /button %}}

#### Target Skills:

1. SWBAT explain how temperature/humidity affect plant growth
2. SWBAT use sample rates to control infinite loops
3. SWBAT distinguish between strings and numbers

---

## Instructional Plan and Structure

We all know that greenhouses are great for climate control - maintaining temperature and humidity at certain levels ensures that we have certain types of plants all year round. However, have you thought about why temperature and humidity affect plant growth?

### Do now (Review questions)

On your composition notebook, write down code that reads data from a light sensor.

Think: if we have a temperature sensor (TemperatureSensorPro) connected to port 3, how would you write code to read temperature and humidity from the sensor?

### Temperature, humidity, plant growth (15 minutes)

#### Discussion: temperature and plant growth

The students recall and discuss what they read from the reading material. We can explain this in terms of biology. Is there an explanation in terms of chemistry? (Temperature affect the rate of chemical reaction)

#### Video: Humidity and plant growth

Humidity is also an important part of climate control that's often overlooked. Below is a video that shows how the stomata on plant leaves interact with humidity and other environmental factors.

{{< youtube "lENdPHwJYxQ" >}}

### Temperature Sensor and OLED Screen (15 minutes)

<img src="https://github.com/SeeedDocument/Grove-Temperature_and_Humidity_Sensor_Pro/raw/master/img/main.jpg" width="500" />

Show students the temperature sensor pro. Ask the students to figure out, without the cheatsheet, how they can read the temperature and humidity from the temperature sensor, given the way they worked with the light sensor:

``` python
from sensors import TemperatureSensorPro
tsp = TemperatureSensorPro(port=3)

tsp.get_temperature()
tsp.get_humidity()
```

Note that the temperature is in Fahrenhit. We can get the Celsius temperature by using `tsp.get_temperature(celsius=True)`.

This shouldn't be too much of a challenge to the students. Next, we are going to display the information on the OLED screen. First, we need to attach the screen to **Port 6**.

Then, we need to import the functionalities that we can use to control the OLED screen:

``` python
from sensors import TemperatureSensorPro
from displays import OledScreen

tsp = TemperatureSensorPro(port=3)
os = OledScreen(port=6)

tsp.get_temperature() # can be deleted
tsp.get_humidity()    # can be delteed
os.show_sensor_data(tsp, 1)
```

The last line of the code instructs the OLED screen to show the data in the temperature sensor to the OLED screen at line 1. The OLED screen can display 8 lines. Change the number and see what happens.

{{% notice note %}}
`tsp.get_temperature()` and `tsp.get_humidity()` have nothing to do with the last line. You do NOT need to write these two lines to show the data on the OLED screen. Actually, they show the data to the terminal, which shows us the options that we have in displaying our data.
{{% /notice %}}

Now we have a problem: the information on the OLED screen never changes. We need to tell Python to **repeatedly** update the information on the OLED screen in certain time intervals. We will need a **while loop** or **infinite loop** to do so:

``` python
from sensors import TemperatureSensorPro
from displays import OledScreen
import time

tsp = TemperatureSensorPro(port=3)
os = OledScreen(port=6)

# notice the lines deleted here
while True:
    os.show_sensor_data(tsp, 1)
    time.sleep(5)
```

Here's quite a bit more information we have here. Let's first explain how the `while True` loop works. It ends with a colon and the next line starts with an indentation (tab key). The indented lines are called "in the loop", which means they will be repeatedly executed, until the condition after `while` is `False`. However, since we wrote `True` here, this means it will never be `False`, so the code will repeat forever.

The `time.sleep()` function in the `time` module simply stops the program and waits for the number of seconds that you specify, and then continue. To use this function, we need to write `import time` at the beginning. Now we update the screen every 5 seconds. This is called the **sample rate**.

#### Discussion

What are some considerations in setting the sample rate?

### Challenges (15 minutes)

#### Challenge 1: Working with additional sensors and show their data on to the OLED screen

The students can guess how to complete this challenge with the cheat sheet. They should figure it out pretty quickly. Here is an example of adding the light sensor:

{{% notice hint %}}
Both the light sensor and the OLED screen go to Port 6, so you will probably need an I2C hub or I2C Branch cable for this:
{{% /notice %}}

``` python
from sensors import TemperatureSensorPro, LightSensor
from displays import OledScreen
import time

tsp = TemperatureSensorPro(port=3)
ls = LightSensor(port=6)
os = OledScreen(port=6)

# notice the lines deleted here
while True:
    os.show_sensor_data(tsp, 1)
    os.show_sensor_data(ls, 2)
    time.sleep(10)
```

#### Challenge 2: Customize the text on the OLED screen

Now we know how to display sensor information on the OLED screen. That's pretty cool, but we can't really change what we see on the screen. Is there a way that we can customize the information on the OLED screen?

Absolutely! We can use the `os.show_line()` function to write certain texts to the screen. For example: `os.show_line(1, "Hello Python!")`

Remember the quotation marks around `"Hello Python"`? This is called a **string** in Python. Strings are important because it tells Python that this text is different from the rest of the program, so interpret it literally. For example: if we write `from sensor import TemperatureSensorPro`, the words `from` and `import` are blue and bolded, because they mean something to Python. Now if we put the same text within quotation marks, it will be grey. They lose the special meaning. So strings differentiate between program code and text.

Now, we can use `os.show_line()` to show some additional texts on the OLED screen.

The most difficult part is how we can have the OLED screen show something like: "Temp: 72.5".  Here's how we do it:

``` python
from sensors import TemperatureSensorPro
from displays import OledScreen
import time

tsp = TemperatureSensorPro(port=3)
os = OledScreen(port=6)

# notice the lines deleted here
while True:
    t = tsp.get_temperature()
    os.show_line(1, "Temp:"+str(h))
    time.sleep(5)
```

Within the `while True` loop, the first line gets the temperature from the temperature sensor, and saves this information to a variable called `h`. Then next step, the `str()` function converts `t` to a string. Afterwards, we join these two strings together.

---

## Review and Assessment (5 minutes)

Please upload your final code to Google Classroom. Save your file in the format of `wa1-0529.py`.

### Exit slip

1. What are stomata?
2. Look at this code here:

``` python
from sensors import TemperatureSensorPro
from displays import OledScreen
import time

tsp = TemperatureSensorPro(port=3)
os = OledScreen(port=6)

while True:
    os.show_sensor_data(tsp, 1)
    time.sleep(5)

os.show_line(4, "Hello")
```

Will you see "Hello" on the OLED screen? Why?

{{% expand "Expand to see answer" %}}
You won't, because it is outside the while loop. The while loop is going to loop forever, so the program will never reach the last line.
{{% /expand %}}

### Video diary

* What did you learn about science today? Did you have any problems understanding it? Why or why not?
* What did you learn about coding today? Did you have any problems understanding it? Why or why not?
* What do you want to learn tomorrow?
