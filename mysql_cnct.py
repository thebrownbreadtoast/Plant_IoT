#Module Import
import MySQLdb

class Database():

	def connect(self): #Function to establish Connection.
		self.connection = MySQLdb.connect(user = 'username', passwd = 'password', host = 'IP address of host', db = 'DB name')
		self.cursor_db = self.connection.cursor()


	def insert_data(self,time,air_moist,moist,temper): #Function to insert data into Table.
		time, air_moisture,moisture, temperature = time,air_moist,moist,temper
		query = 'INSERT INTO tablename VALUES(%s,%s,%s,%s)'
		self.cursor_db.execute(query,(time, air_moisture,moisture,temperature))
		print('Data Inserted.')
		self.connection.commit()
		self.cursor_db.close()
		self.connection.close()

	def update_data(self,time,air_moist,moist,temper): #Function to insert data into Table.
		time, air_moisture,moisture, temperature = time,air_moist,moist,temper
		query = 'UPDATE tablename SET Time = %s, AirMoisture=%s,Moisture=%s,Temperature=%s WHERE ID= 0'
		self.cursor_db.execute(query,(time, air_moisture,moisture,temperature))
		print('Data Updated.')
		self.connection.commit()
		self.cursor_db.close()
		self.connection.close()


if __name__ == '__main__':
	pass



# cursor.execute ("""
#    UPDATE tblTableName
#    SET Year=%s, Month=%s, Day=%s, Hour=%s, Minute=%s
#    WHERE Server=%s
# """, (Year, Month, Day, Hour, Minute, ServerID))