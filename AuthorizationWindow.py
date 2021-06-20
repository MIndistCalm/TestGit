# импортируем библиотеку tkinter всю сразу
import tkinter
from tkinter import messagebox
from MainActivityWindow import *

def run_authorization():

    # главное окно приложения
    window = tkinter.Tk()
    # кортежи и словари, содержащие настройки шрифтов и отступов
    font_header = ('Calibri', 18)
    font_entry = ('Calibri', 12)
    label_font = ('Calibri', 12)
    base_padding = {'padx': 10, 'pady': 8}
    header_padding = {'padx': 10, 'pady': 12}
    background = "#A9A9A9"
    color_font = "#fff"
    # заголовок окна
    window.title('Авторизация')
    # размер окна
    x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2 - 120
    y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2 - 60
    window.geometry('460x240')
    window.geometry("+%d+%d" % (x, y))

    # можно ли изменять размер окна - нет
    window.resizable(False, False)
    window["bg"] = background


    # обработчик нажатия на клавишу 'Войти'
    def clicked():
        # получаем имя пользователя и пароль
        username = username_entry.get()
        password = password_entry.get()
        if username == "1" and password == "1":
            # выводим в диалоговое окно введенные пользователем данные
            messagebox.showinfo('Авторизация', 'Вы успешно вошли в систему')
            window.destroy()
            c = Main_activity_window()
            c.__init__()

    # заголовок формы: настроены шрифт (font), отцентрирован (justify), добавлены отступы для заголовка
    # для всех остальных виджетов настройки делаются также
    main_label = Label(window, text='Авторизация', font=font_header, bg=background , fg="#fff", justify=CENTER, **header_padding)
    # помещаем виджет в окно по принципу один виджет под другим
    main_label.pack()

    # метка для поля ввода имени
    username_label = Label(window, text='Имя пользователя', bg=background, fg="#fff", font=label_font, **base_padding)
    username_label.pack()

    # поле ввода имени
    username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    username_entry.pack()

    # метка для поля ввода пароля
    password_label = Label(window, text='Пароль', bg=background, fg="#fff", font=label_font, **base_padding)
    password_label.pack()

    # поле ввода пароля
    password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
    password_entry.pack()

    # кнопка отправки формы
    send_btn = Button(window, text='Войти', bg="#C0C0C0", bd="1", width="7", activebackground="#DCDCDC", font=label_font, command=clicked)
    send_btn.pack(**base_padding)

    # запускаем главный цикл окна
    window.mainloop()