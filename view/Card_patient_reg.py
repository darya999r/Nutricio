import PySimpleGUI as sg

sg.theme('Purple')   # Add a touch of color
# All the stuff inside your window.

# ------ Menu Definition ------ #
main_menu = [['&КАРТОТЕКА', ['&Создать новую карту', '---', '&Поиск карты в архиве'  ]],
            ['&АНАЛИЗЫ', ['&Анализы и исследования', '---', '&Добавить результаты анализа в карту'],],
            ]

layout = [
    [sg.Text('\n\n\nРЕГИСТРАЦИОННЫЕ ДАННЫЕ:')],
    [sg.Text('Фамилия Имя Отчество:', size=(15, 1)), sg.InputText()], #value[0]
    [sg.Text('Пол:'), sg.Combo(['мужской', 'женский'])], #value[1]
    [sg.Text('Дата рождения:', size=(15, 1)), sg.InputText()], #value[2]
    [sg.Text('Телефон:', size=(15, 1)), sg.InputText()], #value[3]
    [sg.Text('Адрес:', size=(15, 1)), sg.InputText()], #value[4]
    [sg.Text('e-mail:', size=(15, 1)), sg.InputText()], #value[5]
    [sg.Submit('Сохранить'), sg.Cancel('Отмена')]
]

win_card_reg = sg.Window('Nutricio Регистрационные данные', layout)
event, values = win_card_reg.read()
win_card_reg.close()
print(event, values[0], values[1], values[2], values[3], values[4], values[5])    