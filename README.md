# Queue ticket system

Those scripts allow you to simulate a queue system that can be used in a class. 
I was bored to raise my hand in class and waiting for the teacher to come and help me. 

Requests are displayed as follow:
```
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|   Timestamp   |   IP address  |   Group name  |   Message     |
|_______________|_______________|_______________|_______________|
|               |               |               |               |
|00:05:54       |127.0.0.1      |Arnaud         |Help please    |
|00:05:59       |127.0.0.2      |Lucas          |I'm blocked    |
|00:03:31       |127.0.0.3      |Charlotte      |Help on ex2    |
|00:00:00       |127.0.0.4      |Celia          |(╯°□°)╯ ┻━┻    |
|_______________|_______________|_______________|_______________|
```
Client has to know IP address of the server and his port. 
Server is using IP address that DHCP server gave him. 
By default, server is listening to the port n°5000. It is possible to change it in *server.py*. 

If client want to disconnect from server, it needs to send *'exit'* as a message.