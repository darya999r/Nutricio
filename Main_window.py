import PySimpleGUI as sg
import pull_data

def main_window(cpn):
    sg.theme('Purple')   # Add a touch of color
    # All the stuff inside your window.

    # ------ Menu Definition ------ #
    main_menu = [['&КАРТОТЕКА', ['&Создать новую карту', '---', '&Поиск карты в архиве'  ]],
                 ['&АНАЛИЗЫ', ['&Анализы и исследования', '---', '&Добавить результаты анализа в карту'],],
                ]

    # current_patients = ['Иванов Иван Иванович', 'Васин Сергей Петрович', 'Иванова Валерия Сергеевна']

    layout = [  [sg.Menu(main_menu)],
                [sg.Text('\n\n\nТекущие пациенты (выбрать из списка):             \n')],
                [sg.Listbox(cpn, size=(30, len(cpn)), key='-CUR_PAT-')],
                [sg.Button('Перейти в карту пациента')],
                ]

    # Create the Window
    main_window = sg.Window('Nutricio Главное окно', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = main_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Перейти в карту пациента':
            if values['-CUR_PAT-']:    # if something is highlighted in the list
                sg.popup(f"Вы переходите в карту пациента {values['-CUR_PAT-'][0]}.\nЗакройте главное окно.")
                patient_name = ''.join(map(str, values['-CUR_PAT-'][0]))
    
    main_window.close()
    
    return patient_name