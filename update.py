import pyodbc
import random
import string
con = pyodbc.connect('Trusted_Connection=yes', driver = '{ODBC Driver 13 for SQL Server}',server = 'localhost\SQLEXPRESS', database = 'TestDB')
cursor = con.cursor()
cursor.execute("select * from person")
for row in cursor.fetchall():
	print row
id_var = int(raw_input("enter id to update record:"))
cursor.execute("select * from person where id=%d" % (id_var))
result = cursor.fetchone()
if result is not None:
	print result
	lname="".join( [random.choice(string.letters) for i in xrange(5)])
	fname="".join( [random.choice(string.letters) for i in xrange(5)])
	city="".join( [random.choice(string.letters) for i in xrange(5)])
	cursor.execute("update person set lastname='%s', firstname='%s', city='%s' where id=%d" % (lname,fname,city,id_var))
	con.commit()
	print "updated record:"
	cursor.execute("select * from person where id=%d" % (id_var))
	print cursor.fetchone()
else:
	print "enter valid id"
con.close()
