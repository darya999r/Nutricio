import PySimpleGUI as sg

sg.theme('Purple')   # Add a touch of color
# All the stuff inside your window.

# ------ Menu Definition ------ #
main_menu = [['&КАРТОТЕКА', ['&Создать новую карту', '---', '&Поиск карты в архиве'  ]],
            ['&АНАЛИЗЫ', ['&Анализы и исследования', '---', '&Добавить результаты анализа в карту'],],
            ]

layout = [
    [sg.Text('\n\n\nСТИЛЬ ЖИЗНИ:')],
    [sg.Text('Выберите ФИО пациента: ', size=(20, 1)), 
     sg.Combo(['Иванов Иван Иванович', 'Васин Сергей Петрович', 'Иванова Валерия Сергеевна'])], #value[0]
    [sg.Text('Стиль жизни:', size=(20, 1)), sg.InputText()], #value[1]
    [sg.Text('Семейное положение:', size=(20, 1)), sg.InputText()], #value[2]
    [sg.Text('Физическая нагрузка:', size=(20, 1)), sg.InputText()], #value[3]
    [sg.Text('Режим сна:', size=(20, 1)), sg.InputText()], #value[4]
    [sg.Text('Качество сна:', size=(20, 1)), sg.InputText()], #value[5]
    [sg.Text('Объем выпитой жидкости:', size=(20, 1)), sg.InputText()], #value[6]
    [sg.Text('Вредные привычки:', size=(20, 1)), sg.InputText()], #value[7]
    [sg.Text('Пищевое поведение:', size=(20, 1)), sg.InputText()], #value[8]
    [sg.Submit('Сохранить'), sg.Cancel('Отмена')]
]

win_card_life = sg.Window('Nutricio Стиль жизни', layout)
event, values = win_card_life.read()
win_card_life.close()
print(event, values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8])    