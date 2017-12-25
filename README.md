# Plant_IoT
This is my College Minor Project, so it is not perfect and need some work to be done.

It is an IoT project which uses Arduino UNO, Soil Moisture sensor YL-69 and DHT11 Air Moisture and Temperature sensor.

The idea for this project was to help Plant owners who are too busy but love their plants, or some stoners who loves their home grown Weed. Just kidding.

Files in Project:

    main.py - It is the main file which fetches data from Arduino UNO and calls Operations on Database.
    project_arduino.ino - This is Arduino UNO Sketch which connects with sensors.
    mysql_cnct.py - This is used to connect to a MySQL Database and establishes a connection.
    graph.py - This uses Pandas and Matplotlib.pyplot to connect with Database manipulates Dataframe and Plots a graph.

Sorry for horrible Documentation, just a noob programmer.
