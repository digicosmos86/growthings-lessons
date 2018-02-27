+++
title = "Node-RED"
date =  2018-02-26T14:09:04-05:00
weight = 8
pre = "<b>Step 3. </b>"
+++

If you are using our custom image, please skip the section below. Node-RED is already set up on your Raspberry Pi.

#### Setting up Node-RED on Raspberry Pi

The easiest way to set up Node-RED on your Raspberry Pi is to use this
command:

``` {.sourceCode .bash}
$ bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)
```

You will also need to install some useful nodes as well:

``` {.sourceCode .bash}
$ sudo npm install -g node-red-dashboard
$ sudo npm install -g node-red-contrib-python3-function
$ sudo npm install -g node-red-contrib-web-worldmap
```

#### Setting up Node-RED on a Server
-------------------------------

The benefit of running Node-RED on a Raspberry Pi is that you can create
flows that control the SenseHAT. However, sometimes it is easier to have
it run on a server. To do this, you need to, first, make sure you have
node.js set up on the server. You can use this command to check:

``` {.sourceCode .bash}
$ node --version
```

If you are running node.js version 6.x and above, you are ready to
install Node-RED. Otherwise, go to [the official node.js download
page](https://nodejs.org/en/download/) to install the LTS version.

npm will be automatically installed with node.js. On Linux systems, you
can run the following command to install Node-RED.

``` {.sourceCode .bash}
$ sudo npm install -g node-red
$ sudo npm install -g node-red-dashboard
$ sudo npm install -g node-red-contrib-python3-function
$ sudo npm install -g node-red-contrib-web-worldmap
```

On Windows systems, you can start a command line window with
administrative privileges: Start Menu -\> Windows System -\> right click
on Command Line and select run as administrator. Then, run the following
commands:

``` {.sourceCode .bash}
$ npm install -g node-red
$ npm install -g node-red-dashboard
$ npm install -g node-red-contrib-python3-function
$ npm install -g node-red-contrib-web-worldmap
```

#### Setting Up Node-RED on the Cloud

There are also benefits running Node-RED on a Cloud Platform. The
Node-RED official websites have excellent instructions on setting up
Node-RED on different cloud platforms. We recommend that you use the [IBM Cloud](https://ibmcloud.com) since IBM has better support for Node-RED.

- [IBM Bluemix](https://nodered.org/docs/platforms/bluemix)
- [Amazon Web Services](https://nodered.org/docs/platforms/aws)
- [Microsoft Azure](https://nodered.org/docs/platforms/azure)

#### Running Node-RED

To launch the Node-RED web-based flow editor, go to
<http://127.0.0.1:1880> in your browser.