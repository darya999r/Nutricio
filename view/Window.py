from tkinter import *
# import analises_window
# from tkinter import ttk
import commands
 
class Window(Tk):
    def __init__(self):
        super().__init__()
 
        # конфигурация окна
        self.title("NUTRICIO")
        self.geometry("450x400")
 
        # # определение кнопки
        # self.button = ttk.Button(self, text="закрыть")
        # self.button["command"] = self.button_clicked
        # self.button.pack(anchor="center", expand=1)

        # menu
        self.option_add("*tearOff", FALSE)
        main_menu = Menu()

        cardindex_menu = Menu()
        cardindex_menu.add_command(label="Карты текущих пациентов", command=commands.clicked_search_current_card)
        cardindex_menu.add_separator()
        cardindex_menu.add_command(label="Создать новую карту", command=commands.clicked_new_card)
        cardindex_menu.add_separator()
        cardindex_menu.add_command(label="Поиск карты в архиве", command=commands.clicked_search_archive_card)
        

        analyses_menu = Menu()
        analyses_menu.add_command(label="Анализы и исследования", command=commands.clicked_analisis_data)
        analyses_menu.add_separator()
        analyses_menu.add_command(label="Добавить результаты анализа в карту", command=commands.clicked_adding_results_analises)

        main_menu.add_cascade(label="КАРТОТЕКА", menu=cardindex_menu)
        main_menu.add_cascade(label="АНАЛИЗЫ", menu=analyses_menu)
        main_menu.add_cascade(label="ВИТАМИНЫ")
        
        self.config(menu=main_menu)
 
    # def button_clicked(self):
    #     self.destroy()


