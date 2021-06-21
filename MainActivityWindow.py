from tkinter import *
import pypyodbc

# Класс главного окна
class Main_activity_window:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("{0}x{1}+0+0".format(
            self.root.winfo_screenwidth(),
            self.root.winfo_screenheight()))
        self.frames()
        self.root.mainloop()
    # def get_table_names(self, conn):
    #     cur = conn.cursor()
    #     cur.execute('SELECT * FROM '+ str() + ';')
    #     l = cur.fetchall()
    #     # we will populate a list with the names of your tables
    #     tbl_name_list = []
    #     for item in l:
    #         # if sql_type == 'table':
    #         # tbl_name_list.append(sql_name)
    #         print(item)
    #     # your list of table names is constructed
    #     return tbl_name_list

    def frames(self):
        frame_table = LabelFrame(text="Таблицы", font="14", bd="5", )
        x_table = self.root.winfo_screenwidth() / 30
        y_table = self.root.winfo_screenheight() / 20
        x_label_table = round(self.root.winfo_screenwidth() / 30)
        y_label_table = round(self.root.winfo_screenheight() / 20)
        frame_table.pack(side=LEFT, padx='80')
        # labels_table = self.get_table_names(self.connection())


        tables_name = ['Акции_и_скидки', 'Должности', 'Клиенты', 'Меню', 'Поставщики', 'Реестр_мебели',
                       'Реестр_оборудования', 'Реклама', 'Смета', 'Сотрудники', 'Товарооборот', 'Филиал']
        labels_table = []
        for i in tables_name:
            label = Button(frame_table, width=x_label_table, bg='#D3D3D3', text=i, font="12").pack(side=TOP, padx=10)
            labels_table.append(label)
        # label_1.pack(side=TOP, padx=10, pady=10)
        # label_1.pack(side=TOP, padx=10, pady=10)
        # label_2 = Button(frame_table, width=x_label_table, bg='orange', text="2")
        # label_2.pack(side=TOP)

        frame_fields = LabelFrame(text="Записи")
        frame_fields.pack(side=LEFT, padx='80')
        conn = self.connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM ' + tables_name[0] + ';')
        l = cur.fetchall()
        labels_fields = []
        for i in l:
            for j in i:
                label = Button(frame_fields, width=len(str(j)), bg='#D3D3D3', text=j, font="12").pack(side=LEFT)
                labels_fields.append(label)

        # label_3 = Label(frame_bottom, width=7, height=4, bg='lightgreen', text="3")
        # label_3.pack(side=TOP, padx=100, pady=50)
        # label_4 = Label(frame_bottom, width=7, height=4, bg='lightblue', text="4")
        # label_4.pack(side=TOP, padx=100, pady=50)

    def toggle_geom(self):
        geom = self.root.winfo_geometry()
        print(geom, self._geom)
        self.root.geometry(self._geom)
        self._geom = geom

    # Метод, проверяющий соединение с БАЗОЙ ДАННЫХ
    def connection(self):
        try:
            conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\suxin\PycharmProjects\pythonProject\CafeDataBase.accdb;')
            return conn
        except:
            print("Problem with connection, File was not founded\n")
    # Метод устанавливающий курсор в базе данных в выбранное место
    def cursor(self, conn, current):
        cursor = conn.cursor()
        cursor.execute('select * from ' + str(current))
        return cursor
    # Метод, показывающий
    def show(self, item="Смета"):
        self.connection()
        cur = self.cursor(self.connection(), item)
        for row in cur.fetchall():
            print(row)

