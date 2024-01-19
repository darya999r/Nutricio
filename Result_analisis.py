import PySimpleGUI as sg

sg.theme('Purple')   # Add a touch of color
# All the stuff inside your window.

# ------ Menu Definition ------ #
main_menu = [['&КАРТОТЕКА', ['&Создать новую карту', '---', '&Поиск карты в архиве'  ]],
            ['&АНАЛИЗЫ', ['&Анализы и исследования', '---', '&Добавить результаты анализа в карту'],],
            ]


layout = [  [sg.Menu(main_menu)],
            [sg.Text('\n\n\nОБЩИЙ АНАЛИЗ КРОВИ мужской')],
            [sg.Text('Выберите ФИО пациента:')],
            [sg.Combo(['Иванов Иван Иванович', 'Васин Сергей Петрович', 'Иванова Валерия Сергеевна'], key='-PACIENT-')],
            [sg.Text('Введите дату сдачи анализа:')],
            [sg.InputText('', key='-DATE_RES-')],
            [sg.Text('Гематокрит:', key='-GEMATOKRIT-')],
            [sg.InputText('')],
            [sg.Text('Гемоглобин:', key='-GEMOGLOBIN-')],
            [sg.InputText('')],
            [sg.Text('MCV:', key='-MCV-')],
            [sg.InputText('')],
            [sg.Button('Сохранить результаты в карте пациента')],
            ]

# Create the Window
win_res_analisis = sg.Window('Nutricio Результаты анализа', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = win_res_analisis.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Сохранить результаты в карте пациента':
        if values['-DATE_RES-']:    # if something is highlighted in the list
            sg.popup(f"Данные сохранены в карте пациента")


win_res_analisis.close()