# Accessing SQL DB from Python

import pyodbc                                     # Driver for SQL Server

server = 'XYZ.database.windows.net'               # Connection credentials for the SQL DB
database = 'XYZ_DB'
username = 'shahzad@faserv'
password = 'xxxxxx'


driver= '{ODBC Driver 13 for SQL Server}'          # Construction of connection string
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute("select @@VERSION")                      # making a cursor              
cursor.execute('''insert dbo.MasterExpense (            # Now its ready, write SQL statements wrapped within cursor execute method
Project,
 Tr_date,
 Funds_From, Funds_to,Fund_Amount, 
 Expense_Head,Exp_Amount,Exp_Detail, Account
 ) values ('Morning Dew','21-Dec-16','SR','SW','-265','Paint',
 '265', 'Beige and White paint','AMEX CarD # 1013') ''')
cursor.commit()                                                # Must commit the previous SQL Command

cursor.execute("select * from MasterExpense ")                 
row=cursor.fetchone()                                         # fetchone will fetch the data from last line
print(row)
