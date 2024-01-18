import PySimpleGUI as sg

sg.theme('Purple')   # Add a touch of color
# All the stuff inside your window.

# ------ Menu Definition ------ #
main_menu = [['&КАРТОТЕКА', ['&Создать новую карту', '---', '&Поиск карты в архиве'  ]],
            ['&АНАЛИЗЫ', ['&Анализы и исследования', '---', '&Добавить результаты анализа в карту'],],
            ]

layout = [
    [sg.Text('\n\n\nАНТРОПОМЕТРИЯ:')],
    [sg.Text('Рост:', size=(30, 1)), sg.InputText()], #value[0]
    [sg.Text('Колебания веса с 16-летнего возраста:', size=(30, 1)), sg.InputText()], #value[1]
    [sg.Submit('Сохранить'), sg.Cancel('Отмена')]
]

win_card_antr = sg.Window('Nutricio Антропометрия', layout)
event, values = win_card_antr.read()
win_card_antr.close()
print(event, values[0], values[1])    # the input data looks like a simple list when auto numbered