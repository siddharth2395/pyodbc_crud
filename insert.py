import pyodbc
import random
import string
con = pyodbc.connect('Trusted_Connection=yes', driver = '{ODBC Driver 13 for SQL Server}',server = 'localhost\SQLEXPRESS', database = 'TestDB')
cursor = con.cursor()
for i in range(1,10):
	lname="".join( [random.choice(string.letters) for i in xrange(5)])
	fname="".join( [random.choice(string.letters) for i in xrange(5)])
	city="".join( [random.choice(string.letters) for i in xrange(5)])
	cursor.execute("insert into Persons(LastName, FirstName, City) values ('%s', '%s', '%s')" % (lname,fname,city))
con.commit()
con.close()
