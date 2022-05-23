from tkinter import *
import mysql.connector as mc
import csv   
from tkinter.filedialog import askopenfilename

#GUI WINDOW DESIGHN

class Window(object):
    host = ''
    username = ''
    password = ''
    db_name = ''
    def __init__(self, window):
        self.window = window
        self.window.geometry('400x120')
        self.window.configure(bg='#1098ad')
        self.window.wm_title('MySQL Load File')

        self.v1=StringVar()
        self.v2=StringVar()
        self.v3=StringVar()
        self.v4=StringVar()


        Label(window, text="Host:",width=20).grid(row=0, column=0)
        Label(window, text="Username:",width=20).grid(row=1)
        Label(window, text="Password:",width=20).grid(row=2)
        Label(window, text="Db Name:",width=20).grid(row=3)

        self.e1 = Entry(window, width=50, textvariable=self.v1)
        self.e2 = Entry(window, width=50, textvariable=self.v2)
        self.e3 = Entry(window, show='*', width=50, textvariable=self.v3)
        self.e4 = Entry(window, width=50, textvariable=self.v4)

        self.e1.grid(row=0, column=2)
        self.e2.grid(row=1, column=2)
        self.e3.grid(row=2, column=2)
        self.e4.grid(row=3, column=2)
        
        b1=Button(window,text='Submit',width=40,command=self.submit)
        b1.grid(row=5,column=2)
        b1.place(relx=0.5, rely=0.85, anchor=CENTER)


    def submit(self):
      global host, username,password,db_name
      host = self.v1.get()
      username = self.v2.get()
      password = self.v3.get()
      db_name = self.v4.get()
      
      self.window.destroy()

#Gui Enter Detials
window = Tk()
Window(window)
window.mainloop()

#DB Connection
db = mc.connect(
    host=host,
    user=username,
    password=password,
    database=db_name
    )
cursor = db.cursor()
print('Connected! Starting Import')


#GUI to select file to import 
Tk().withdraw() 
filename = askopenfilename() 
file_path = filename.removesuffix('.csv')
table_name = 'order_items'
data=""

#Replacing the " value in the csv file with ' for sql.
with open(file_path +'.csv') as file:
     data = file.read().replace('"', "'")

with open(file_path + '_updated.csv','w') as file:
    file.write(data)


#Reading the new CSV file as a list of lists (skipping the first row header)
csv_data = csv.reader(open(file_path + '_updated.csv'))
next(csv_data)

#Looping through the list of rows, joining the values with a comma and executing script
for row in csv_data:
    values = ",".join(row)
    cursor.execute(f"INSERT INTO {table_name} VALUES ({values})")

db.commit()
cursor.close()
print('COMPLETED SUCCESSFULLY')
        

  











