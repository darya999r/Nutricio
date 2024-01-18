import PySimpleGUI as sg

sg.theme('Purple')   # Add a touch of color
# All the stuff inside your window.

# ------ Menu Definition ------ #
main_menu = [['&КАРТОТЕКА', ['&Создать новую карту', '---', '&Поиск карты в архиве'  ]],
            ['&АНАЛИЗЫ', ['&Анализы и исследования', '---', '&Добавить результаты анализа в карту'],],
            ]

layout = [
    [sg.Text('\n\n\nИЗМЕРЕНИЯ ТЕЛА:')],
    [sg.Text('Выберите ФИО пациента: ', size=(30, 1)), 
     sg.Combo(['Иванов Иван Иванович', 'Васин Сергей Петрович', 'Иванова Валерия Сергеевна'])], #value[0]
    [sg.Text('Дата измерения (формат "12.11.2023"):', size=(30, 1)), sg.InputText()], #value[1]
    [sg.Text('Вес:', size=(30, 1)), sg.InputText()], #value[2]
    [sg.Text('Объем груди:', size=(30, 1)), sg.InputText()], #value[3]
    [sg.Text('Объем талии:', size=(30, 1)), sg.InputText()], #value[4]
    [sg.Text('Объем бедер:', size=(30, 1)), sg.InputText()], #value[5]
    [sg.Text('Комментарий:', size=(30, 1)), sg.InputText()], #value[6]
    [sg.Submit('Сохранить'), sg.Cancel('Отмена')]
]

win_card_meas = sg.Window('Nutricio Измерения тела', layout)
event, values = win_card_meas.read()
win_card_meas.close()
print(event, values[0], values[1], values[2], values[3], values[4], values[5], values[6])   