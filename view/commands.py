from tkinter import *
# from tkinter import messagebox
# import Window

def clicked_search_current_card():
    # window_search_current_card = Tk()
    # window_search_current_card.title("NUTRICIO Поиск в текущих картах")
    # window_search_current_card.geometry('400x250')
    lbl = Label(Tk, text="Перешли в поиск текущей карты", font=("Arial Bold", 10))  
    lbl.grid(column=0, row=0)
    # messagebox.showinfo("NUTRICIO", "Поиск в текущих картах")

def clicked_search_archive_card():
    lbl = Label(Tk, text="Перешли в поиск карты в архиве", font=("Arial Bold", 10))  
    lbl.grid(column=0, row=0)

def clicked_new_card():
    lbl = Label(Tk, text="Перешли к созданию новой карты", font=("Arial Bold", 10))  
    lbl.grid(column=0, row=0)

def clicked_analisis_data():
    lbl = Label(Tk, text="Перешли в данные по анализам", font=("Arial Bold", 10))  
    lbl.grid(column=0, row=0)

def clicked_adding_results_analises():
    lbl = Label(Tk, text="Перешли к добавлению результатов анализов в карту", font=("Arial Bold", 10))  
    lbl.grid(column=0, row=0)

# main_menu = Menu()

# cardindex_menu = Menu()
# cardindex_menu.add_command(label="Поиск текущей карты", command=clicked_search_current_card)
# cardindex_menu.add_separator()
# cardindex_menu.add_command(label="Поиск карты в архиве", command=clicked_search_archive_card)
# cardindex_menu.add_separator()
# cardindex_menu.add_command(label="Создать новую карту", command=clicked_new_card)

# analyses_menu = Menu()
# analyses_menu.add_command(label="Посмотреть данные по анализу", command=clicked_analisis_data)
# analyses_menu.add_separator()
# analyses_menu.add_command(label="Добавить результаты анализа в карту", command=clicked_adding_results_analises)

# main_menu.add_cascade(label="КАРТОТЕКА", menu=cardindex_menu)
# main_menu.add_cascade(label="АНАЛИЗЫ", menu=analyses_menu)
# main_menu.add_cascade(label="ВИТАМИНЫ")