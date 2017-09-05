import pyodbc
import random
import string
con = pyodbc.connect('Trusted_Connection=yes', driver = '{ODBC Driver 13 for SQL Server}',server = 'localhost\SQLEXPRESS', database = 'TestDB')
cursor = con.cursor()
cursor.execute("select * from Persons")
for row in cursor.fetchall():
	print row
con.close()
