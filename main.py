from tkinter import *
from AuthorizationWindow import run_authorization
import pypyodbc

conn = pypyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\suxin\OneDrive\Documents\CafeDataBase.accdb;')
cursor = conn.cursor()
cursor.execute('select * from Смета')

for row in cursor.fetchall():
    print(row)

run_authorization()
# if run_authorization():
    # root = Tk()
    # root.attributes('-fullscreen', True)
    # root.mainloop()