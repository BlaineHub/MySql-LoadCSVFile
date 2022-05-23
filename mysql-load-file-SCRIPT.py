import csv
import mysql.connector as mc
from tkinter import Tk    
from tkinter.filedialog import askopenfilename

#DB Connection
db = mc.connect(
    host='',
    user='',
    password='',
    database=''
    )
cursor = db.cursor()
print('Connected! Starting Import')

#GUI to select file to import 
Tk().withdraw() 
filename = askopenfilename() 
file_path = filename 
table_name = ''

#Reading the new CSV file as a list of lists (skipping the first row header)
csv_data = csv.reader(open(file_path)) # 
next(csv_data)

#Looping through the list of rows, joining the values with a comma and executing script
for row in csv_data:
    print(row)
    values = ",".join(row)
    cursor.execute(f"INSERT INTO {table_name} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",row)

db.commit()
cursor.close()
print('COMPLETED SUCCESSFULLY')
        