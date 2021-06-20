from tkinter import *
import pypyodbc

conn = pypyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\suxin\OneDrive\Documents\CafeDataBase.accdb;')
cursor = conn.cursor()
cursor.execute('select * from Смета')

for row in cursor.fetchall():
    print(row)

root = Tk()

root.mainloop()