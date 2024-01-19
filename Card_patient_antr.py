import PySimpleGUI as sg

sg.theme('Purple')   # Add a touch of color
# All the stuff inside your window.

# ------ Menu Definition ------ #
main_menu = [['&КАРТОТЕКА', ['&Создать новую карту', '---', '&Поиск карты в архиве'  ]],
            ['&АНАЛИЗЫ', ['&Анализы и исследования', '---', '&Добавить результаты анализа в карту'],],
            ]

layout = [
    [sg.Text('\n\n\nАНТРОПОМЕТРИЯ:')],
    [sg.Text('Выберите ФИО пациента: ', size=(30, 1)), 
     sg.Combo(['Иванов Иван Иванович', 'Васин Сергей Петрович', 'Иванова Валерия Сергеевна'])], #value[0]
    [sg.Text('Рост:', size=(30, 1)), sg.InputText()], #value[1]
    [sg.Text('Колебания веса с 16-летнего возраста:', size=(30, 1)), sg.InputText()], #value[2]
    [sg.Submit('Сохранить'), sg.Cancel('Отмена')]
]

win_card_antr = sg.Window('Nutricio Антропометрия', layout)
event, values = win_card_antr.read()
win_card_antr.close()
print(values[0], values[1])    # the input data looks like a simple list when auto numbered