# Module Imports
import serial
import time, datetime
import mysql_cnct
import graph

#Connections
serial_connection = serial.Serial('/dev/ttyACM0', baudrate = 9600,timeout = 3000)
mysqlcon = mysql_cnct.Database()

#Infinite Loop
while 1:

	sensorsdata = serial_connection.readline().decode('UTF-8').split('/t')

	sensorairmois = float(sensorsdata[0])
	sensortemp = float(sensorsdata[1])
	sensorsoil = float(str(sensorsdata[2].strip('\r\n')))
	sensortime = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%H:%M')) #Current Time

	#Database Operations
	mysqlcon.connect()
	mysqlcon.insert_data(sensortime,sensorairmois,sensorsoil,sensortemp)
	mysqlcon.connect()
	mysqlcon.update_data(sensortime,sensorairmois,sensorsoil,sensortemp)

	#Generate Graph
	graph_image = graph.generate_graph()

	#Flow control
	if (sensorsoil > 30):
		print(str('Everything is fine, Air Moisture is {}% , Soil Moisture is {}% and Temperature is {}C').format(sensorairmois,sensorsoil,sensortemp))
		time.sleep(15)

	elif (sensorsoil <=30):
		print(str('Need Attention, Air Moisture is {}% , Soil Moisture is {}% and Temperature is {}C').format(sensorairmois,sensorsoil,sensortemp))
		time.sleep(15)


