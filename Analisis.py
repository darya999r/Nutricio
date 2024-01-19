import PySimpleGUI as sg

def analisis(data):
    sg.theme('Purple')   # Add a touch of color
    # All the stuff inside your window.

    # ------ Menu Definition ------ #
    main_menu = [['&КАРТОТЕКА', ['&Создать новую карту', '---', '&Поиск карты в архиве'  ]],
                ['&АНАЛИЗЫ', ['&Анализы и исследования', '---', '&Добавить результаты анализа в карту'],],
                ]

    headings = ['Показатели', 'Оптимум', 'Пониженное значение', 'Повышенное значение']

    layout = [  [sg.Menu(main_menu)],
                [sg.Text('\n\n\nОбщий Анализ Крови мужской:             \n')],
                [sg.Table(values=data, headings=headings, max_col_width=60,
                        auto_size_columns=True,
                        justification='left',
                        num_rows=3,
                        alternating_row_color='lightyellow',
                        key='-TABLE-',
                        row_height=120)],
                [sg.Button('Добавить результаты анализа в карту пациента')],
                ]

    # Create the Window
    win_analisis = sg.Window('Nutricio Анализ/исследование', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = win_analisis.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Добавить результаты анализа в карту пациента':
            sg.popup(f"Вы переходите на страницу добавления результатов анализа в карту пациента")

    win_analisis.close()