from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import Window


class MainWindow(Window.Window):
    def __init__(self):
        Window.Window.__init__(self)
        self.title("NUTRICIO Главная страница")

        # заголовок списка
        label = ttk.Label(text="\n\n\n\nТекущие пациенты:", font=("Arial", 14))
        label.pack()

        # определяем данные для отображения
        people = [("Tom", 38, "tom@email.com"), ("Bob", 42, "bob@email.com"), ("Sam", 28, "sam@email.com")]
        
        label = ttk.Label()
        label.pack(anchor=N, fill=X)
        # определяем столбцы
        columns = ("name", "age", "email")
        tree = ttk.Treeview(columns=columns, show="headings")
        tree.pack(expand=1, fill=BOTH)
        
        # определяем заголовки
        tree.heading("name", text="Имя", anchor=W)
        tree.heading("age", text="Возраст", anchor=W)
        tree.heading("email", text="Email", anchor=W)
        
        tree.column("#1", stretch=NO, width=70)
        tree.column("#2", stretch=NO, width=60)
        tree.column("#3", stretch=NO, width=100)
        
        # добавляем данные
        for person in people:
            tree.insert("", END, values=person)

        def click_button():
            showinfo(title="Информация", message="Вы переходите в карту пациента!")

        def item_selected(event):
            selected_people = ""
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                person = item["values"]
                selected_people = f"{selected_people}{person}\n"
            label["text"]=selected_people
            btn = ttk.Button(text="Перейти в карту", command=click_button)
            btn.pack()
        
        tree.bind("<<TreeviewSelect>>", item_selected)
