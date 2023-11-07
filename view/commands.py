from tkinter import *
from tkinter import ttk
import AnalisesWindow


def clicked_new_card():
    lbl = Label(text="Перешли к созданию новой карты", font=("Arial Bold", 10))  
    lbl.pack()

def clicked_search_archive_card():

    search_archive_card_window = Toplevel()
    search_archive_card_window.title("Поиск карты в архиве")
    search_archive_card_window.geometry("450x250")

    def show_message():
        entry_mass = entry.get()     # получаем введенный текст
        lbl = Label(search_archive_card_window, text=entry_mass, font=("Arial Bold", 10))
        lbl.pack()


    # поле ввода фио пациента для поиска
    entry = ttk.Entry(search_archive_card_window)
    entry.pack(anchor=NW, padx=10, pady=10)
    # кнопка поиска
    btn1 = ttk.Button(search_archive_card_window, text="Поиск", command=show_message)
    btn1.pack(anchor=E, padx=6, pady=6)

    # кнопка выводит список всех пациентов архива
    btn2 = ttk.Button(search_archive_card_window, text="Вывести список пациентов в архиве")
    btn2.pack(side=BOTTOM)

    search_archive_card_window.grab_set()


def clicked_analisis_data():
    # lbl = Label(text="Перешли в данные по анализам", font=("Arial Bold", 10))  
    # lbl.pack()
    analises_window = AnalisesWindow.AnalisesWindow()

def clicked_adding_results_analises():
    lbl = Label(text="Перешли к добавлению результатов анализов в карту", font=("Arial Bold", 10))  
    lbl.pack()
