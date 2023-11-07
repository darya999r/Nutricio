from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


class AnalisesWindow(Toplevel):
    def __init__(self):
        super().__init__()
 
        # конфигурация окна
        self.title("NUTRICIO Анализы")
        self.geometry("450x500")

        # заголовок списка
        label = ttk.Label(self, text="\n\n\n\nАнализы и исследования:", font=("Arial", 14))
        label.pack()

        # определяем данные для отображения
        people = [("OAK", "man"), ("OAK", "woman"), ("OAM", "man")]
        
        label = ttk.Label(self)
        label.pack(anchor=N, fill=X)
        # определяем столбцы
        columns = ("name", "sex")
        tree = ttk.Treeview(self, columns=columns, show="headings")
        tree.pack(expand=1, fill=BOTH)
        
        # определяем заголовки
        tree.heading("name", text="Название", anchor=W)
        tree.heading("sex", text="Пол", anchor=W)
        
        tree.column("#1", stretch=NO, width=70)
        tree.column("#2", stretch=NO, width=60)
        
        # добавляем данные
        for person in people:
            tree.insert("", END, values=person)

        def click_button():
            showinfo(title="Информация", message="Вы переходите на страницу анализа/исследования!")
        
        def item_selected(event):
            selected_test = ""
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                analis = item["values"]
                selected_test = f"{selected_test}{analis}\n"
            label["text"]=selected_test
            btn = ttk.Button(self, text="Перейти на страницу анализа", command=click_button)
            btn.pack()
        
        tree.bind("<<TreeviewSelect>>", item_selected)
        self.grab_set()       # захватываем пользовательский ввод

