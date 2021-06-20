from tkinter import *
import pypyodbc

# Класс главного окна
class Main_activity_window:
    def __init__(self):
        self.root = Tk()
        self.root.attributes('-disabled', True)
        self.root.mainloop()


    # Метод, проверяющий соединение с БАЗОЙ ДАННЫХ
    def connection(self):
        try:
            conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\suxin\OneDrive\Documents\CafeDataBase.accdb;')
            return conn
        except:
            print("Problem with connection, File was not founded\n")
    # Метод устанавливающий курсор в базе данных в выбранное место
    def cursor(self, conn, current):
        cursor = conn.cursor()
        cursor.execute('select * from ' + str(current))
        return cursor
    # Метод, показывающий набор
    def show(self, item="Смета"):
        self.connection()
        cur = self.cursor(self.connection(), item)
        for row in cur.fetchall():
            print(row)

