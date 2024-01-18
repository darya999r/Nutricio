import PySimpleGUI as sg

sg.theme('Purple')   # Add a touch of color
# All the stuff inside your window.

# ------ Menu Definition ------ #
main_menu = [['&КАРТОТЕКА', ['&Создать новую карту', '---', '&Поиск карты в архиве'  ]],
            ['&АНАЛИЗЫ', ['&Анализы и исследования', '---', '&Добавить результаты анализа в карту'],],
            ]

analises_list = ('Общий Анализ Крови мужской', 'Общий Анализ Крови женский', 'Биохимия крови', 'Углеводный обмен', 'Оценка запасов железа')

layout = [  [sg.Menu(main_menu)],
            [sg.Text('\n\n\nАнализы и исследования (выбрать из списка):             \n')],
            [sg.Listbox(analises_list, size=(30, len(analises_list)), key='-ANALISES-')],
            [sg.Button('Перейти на страницу анализа/исследования')],
            ]

# Create the Window
win_main_analisis = sg.Window('Nutricio Анализы', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = win_main_analisis.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Перейти на страницу анализа/исследования':
        if values['-ANALISES-']:    # if something is highlighted in the list
            sg.popup(f"Вы переходите на страницу анализа {values['-ANALISES-'][0]}")


win_main_analisis.close()