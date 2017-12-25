#Import Module
import pandas as pd
import matplotlib.pyplot as plt
import MySQLdb

def generate_graph():  #Function to Generate Graph
	conn = MySQLdb.connect(user = 'username', passwd = 'password', host = 'IP address of host', db = 'DB name')  #MySQL connection
	query = 'SELECT * FROM tablename'

	#Database imported into dataframe & Cleaning of Data
	df = pd.read_sql(query,conn)  
	df['Time'] = pd.DatetimeIndex(df['Time'])
	df['Time'] = df['Time'].dt.time
	df.set_index('Time', inplace= True)

	#Plotting Graph & saves a .png image
	df.plot(title = 'Plant Data', rot = 45, figsize = (15,10))
	plt.savefig('graph.png', transparent = False)
	plt.close()
	conn.close()

if __name__ == '__main__':
	pass
	
