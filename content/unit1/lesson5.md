+++
title = "Treasure Hunt with Sensors and Live Dashboard"
date =  2018-05-31T16:29:07-04:00
weight = 9
pre = "<b>Lesson 5. </b>"
+++

---

## Lesson Information

This lesson is a treasure hunt game. Students program sensors and send sensor data to an online dashboard that displays the data in real time. Half of them will then try to hide their sensors somewhere within the range of internet connection in the school, and the other half will use the information from the live dashboard to locate the sensors that their classmates hid.

{{% sidebar "Highlights" %}}

##### Computational Thinking Skills

* **Abstraction**: data collection
* **Abstraction**: data visualization and sense making
* **Automation**: automating the collection of data

##### CSTA Computer Science Standards

* **number**: description
* **number**: description

##### Duration

45 to 50 minutes

{{% /sidebar %}}

#### The purpose of the lesson is to:

1. Formulate scientific hypotheses and use empirical data to support/disprove them
2. Teach how to make sense of data with artifacts created by the students themselves
3. Understand the process of graphing and data visualization

#### Driving Science Questions:

* What do you think are some factors that affect temperature, humidity, and (optionally) light intensity?
* Do the data that you have collected support your hypotheses?

#### Science Concepts:

* **Scientific Hypotheses**: an idea that proposes a tentative explanation about a phenomenon or a narrow set of phenomena observed in the natural world
* **Empirical Evidence**: information acquired by observation or experimentation. Scientists record and analyze this data. The process is a central part of the scientific method.

#### Computer Science Concepts:

* **Data visualization**: Data visualization is the presentation of data in a pictorial or graphical format. It enables decision makers to see analytics presented visually, so they can grasp difficult concepts or identify new patterns.

#### Materials Needed:

> WioLink board, router that's already connected to the Internet, temperature sensor, light sensor, live dashboard ([link](http://ts.bc.edu:1880/ui)), rechargeable batteries, {{% button href="https://www.dropbox.com/s/s105hgh5gwzpdlt/Lesson%205.%20Plants_inquiry.docx?dl=1" icon="fa fa-download"%}}Reading Material{{% /button %}}

#### Target Skills:

1. SWBAT make scientific hypotheses
2. SWBAT understand data from data visualizations
3. SWBAT use data to test their hypotheses

---

## Instructional Plan and Structure

In this lesson the students will mainly be playing a treasure hunt game. They will program their WioLink boards to send data to a live dashboard ([found here](http://ts.bc.edu:1880/ui)). Using the information from the dashboard, they will try to find the boards hidden by other students.

### Do Now (Review of Concepts)

In your composition notebook, quickly write code that displays information from a temperature sensor onto an OLED screen with `os.show_sensor_data()`.

### Internet connection (10 minutes)

Before the students start coding, they need to use the "File Manager" button to view the files on the board. Make sure that they delete the "main.py" file written by other students before they start coding.

The students connect their boards to the Internet and send data from their temperature sensor with the following code:

``` python
from iot import WiFi, BcServer

wifi = WiFi("GrowThings", "Grow2018")
wifi.connect()

from sensors import TemperatureSensorPro
import time
tsp = TemperatureSensorPro()

server = BcServer(team = "wa1") #use your own team name, lower case

while True:
    server.send_sensor_data(tsp)
    time.sleep(20)
```

{{% notice note %}}
The students can feel free to use a light sensor too. Apart from importing the LightSensor name, they also need to use the code as follows:
{{% /notice %}}

``` python
from iot import WiFi, BcServer

wifi = WiFi("GrowThings", "Grow2018")
wifi.connect()

from sensors import TemperatureSensorPro
import time
tsp = TemperatureSensorPro(port=3)
ls = LightSensor(port=6)

server = BcServer(team = "wa1") #use your own team name, lower case

while True:
    server.send_sensor_data([tsp, ls])
    time.sleep(20)
```

The teacher needs to go to the [live dashboard](http://ts.bc.edu:1880/ui) and use the correct tab for his/her class (there is one dashboard for each block).

If everything works correctly, the students will receive a "data sent" message every 20 seconds (we recommend that the sample rate is at least 20 seconds so as not to overwhelm the server). Their team name will show up on the live dashboard.

### Treasure hunt (30 minutes)

Make sure that each board has a rechargeable battery attached to the battery port. After the students have programed their board, they can rename their board to `main.py` and upload the code to the board using the "upload" button.  Now the students will have their code working on their board without having to be connected to a computer.

Now, half of the students are going to hide their boards (the other half need to turn off their boards). Before they do so, they need to write on a cue card where they are going to hide their boards so their classmates can easily locate them and why they made these decisions. The teacher can reset the dashboard before they start.

Switch the groups after 15 minutes.

### Reflection (15 minutes)

Give some time for the students to reflect on their experience. Ask students why they chose to hide their boards the way they did, and did the data support their **scientific** hypothesis?  Do they think this process is **scientific inquiry**? Why or why not? They can also write their answers on their composition notebook too.

---

## Review and Assessment (5 minutes)

Please upload your final code to Google Classroom. Save your file in the format of `wa1-0529.py`.

### Exit slip

The students can write their reflection as exit slip.

### Video diary
- What did you learn about science today? Did you have any problems understanding it? Why or why not?
- What did you learn about coding today? Did you have any problems understanding it? Why or why not?
- What do you want to learn tomorrow?
