import PySimpleGUI as sg

sg.theme('Purple')   # Add a touch of color
# All the stuff inside your window.

# ------ Menu Definition ------ #
main_menu = [['&КАРТОТЕКА', ['&Создать новую карту', '---', '&Поиск карты в архиве'  ]],
            ['&АНАЛИЗЫ', ['&Анализы и исследования', '---', '&Добавить результаты анализа в карту'],],
            ]


layout = [  [sg.Menu(main_menu)],
            [sg.Text('\n\n\nАрхив пациентов')],
            [sg.Text('Выберите ФИО пациента:')],
            [sg.Combo(['Наумова Ольга Викторовна', 'Васильев Олег Петрович'], key='-ARCHIVE-')],
            [sg.Button('Открыть карту пациента')],
            [sg.Button('Перенести карту пациента в список Текущих карт')],
        ]


# Create the Window
win_archive = sg.Window('Nutricio Архив пацентов', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = win_archive.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Открыть карту пациента':
        sg.popup(f"Вы переходите в карту пациента!")


win_archive.close()