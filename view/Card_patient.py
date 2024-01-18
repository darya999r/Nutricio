import PySimpleGUI as sg

sg.theme('Purple')   # Add a touch of color
# All the stuff inside your window.

# ------ Menu Definition ------ #
main_menu = [['&КАРТОТЕКА', ['&Создать новую карту', '---', '&Поиск карты в архиве'  ]],
            ['&АНАЛИЗЫ', ['&Анализы и исследования', '---', '&Добавить результаты анализа в карту'],],
            ]

reg_data = ('Сидоров Андрей Николаевич', 'мужской', '15.03.1987', 
            '89154625253', 'Москва Ленинградский пр. 25-123', 'ssdfesfdv@mail.ru')

antr_data = ('Сидоров Андрей Николаевич', '184', '53-98')

meas_data = ('Сидоров Андрей Николаевич', '18.01.2024', '98', '105', '115', '125', 'вес снизился на 2 кг')

life_data = ('Сидоров Андрей Николаевич', 'не активный', 'не женат', 'минимальная', 
             '00:00-7:00', 'плохое', '1.5 л/день', 'нет', '2 р/день, обед и ужин')

tab1_layout = [[sg.Text(f'Фамилия Имя Отчество: {reg_data[0]}')], 
               [sg.Text(f'Пол: {reg_data[1]}')],
               [sg.Text(f'Дата рождения: {reg_data[2]}')],
               [sg.Text(f'Телефон: {reg_data[3]}')],
               [sg.Text(f'Адрес: {reg_data[4]}')],
               [sg.Text(f'e-mail: {reg_data[5]}')]]

tab2_layout = [[sg.Text(f'Рост: {antr_data[1]}')], 
               [sg.Text(f'Колебания веса с 16-летнего возраста: {antr_data[2]}')]]

tab3_layout = [[sg.Text(f'Дата измерения: {meas_data[1]}')],
               [sg.Text(f'Вес: {meas_data[2]}')],
               [sg.Text(f'Обьем груди: {meas_data[3]}')],
               [sg.Text(f'Объем талии: {meas_data[4]}')],
               [sg.Text(f'Объем бедер: {meas_data[5]}')],
               [sg.Text(f'Комментарий: {meas_data[6]}')]]

tab4_layout = [[sg.Text(f'Стиль жизни: {life_data[1]}')],
               [sg.Text(f'Семейное положение: {life_data[2]}')],
               [sg.Text(f'Физическая нагрузка: {life_data[3]}')],
               [sg.Text(f'Режим сна: {life_data[4]}')],
               [sg.Text(f'Качество сна: {life_data[5]}')],
               [sg.Text(f'Объем выпитой жидкости: {life_data[6]}')],
               [sg.Text(f'Вредные привычки: {life_data[7]}')],
               [sg.Text(f'Пищевое поведение: {life_data[8]}')]]

layout = [[sg.Menu(main_menu)],
          [sg.Text(f'\n\n\nКАРТА ПАЦИЕНТА:  {reg_data[0]}')],
          [sg.TabGroup([[sg.Tab('РЕГИСТРАЦИОННЫЕ ДАННЫЕ:', tab1_layout), 
                         sg.Tab('АНТРОПОМЕТРИЯ:', tab2_layout),
                         sg.Tab('ИЗМЕРЕНИЯ ТЕЛА:', tab3_layout),
                         sg.Tab('СТИЛЬ ЖИЗНИ:', tab4_layout),
                         ]])],
          [sg.Button('Редактировать данные')],
          ]


# Create the Window
win_card_patient = sg.Window('Nutricio Карта пациента', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = win_card_patient.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Редактировать данные':
        sg.popup(f"Вы переходите в редактирование данных карты пациента!")


win_card_patient.close()