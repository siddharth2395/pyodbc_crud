import pyodbc

con = pyodbc.connect('Trusted_Connection=yes', driver = '{ODBC Driver 13 for SQL Server}',server = 'localhost\SQLEXPRESS', database = 'TestDB')
cursor = con.cursor()
cursor.execute("select * from person")
for row in cursor.fetchall():
	print row
id_var = int(raw_input("enter id to delete record:"))
cursor.execute("delete from person where id = %d" % (id_var))
con.commit()
con.close()
