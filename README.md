# Overview

As a software engineer, I want to explore different areas of software design. To further my understanding of programming network connections I decided to explore setting up my own Server-Client relationship using Python.

The program I've written includes two separate parts, designed to connect two computers. There is software included in the package for the Server device. Also, there is a file for the Client device. To properly connect the devices, run the file serverSide.py on one device. And run the file clientSide.py on the other device you are connecting to.

This software was written to help me understand the abilities of network modules within Python. I was able to practice sending and receiving data using the built in network modules. I also ran **pip install python-dotenv** to use the .env file.

[Software Demo Video](https://youtu.be/lD0WhWyWb8Q)

# Network Communication

I used a Server-Client architecture in my design. This required that I had two separate programs. One for the server and one for the client.

This is being run using a TCP/IP connection with the socket connection. I hid the variables for the port in the .env file.
I ran the software using port 12345. This made it easy to remember. The harder part was figuring out which IP address to reference for the server.
Since both computers were on the same network, I ran IPConfig in the Terminal and used the device IP address listed on the shared network.

The format of the messages being sent is a bytes object. Using encode() and decode(), when sending messages, converts strings into bytes and vise versa.
This made it easy to send information in a flexible manner.

# Development Environment

The software was written in Python language using the Visual Studio Code IDE. I used two computers, with similar development resources to test the communications of the program.

Using Python language, there were built in network modules to use. I had to install the dotenv module as I mentioned in the Overview. Ultimately, this was all accomplished without installing additional modules.

# Useful Websites

* [Python.Org](https://docs.python.org/3/library/socketserver.html)
* [Stack Overflow](https://stackoverflow.com/)
* [Pythontic.com](https://pythontic.com/modules/socket/introduction)

# Future Work

* It can be a bit buggy when the connection is closed outside of using the menu options. I would like to improve that in the future.
* This program could easily be incorporated into software designed to use on a Private Network. I would like to explore that more.
* An addition of a GUI menu would allow this program to be used for messaging and sharing on mobile devices too.
