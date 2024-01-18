import PySimpleGUI as sg

sg.theme('Purple')   # Add a touch of color
# All the stuff inside your window.

# ------ Menu Definition ------ #
main_menu = [['&КАРТОТЕКА', ['&Создать новую карту', '---', '&Поиск карты в архиве'  ]],
            ['&АНАЛИЗЫ', ['&Анализы и исследования', '---', '&Добавить результаты анализа в карту'],],
            ]

data = [['Гематокрит', '40-48', '1.Анемии любого происхождения\n2.Кровопотеря\n3.Беременность\n'+
         '4.Употребление большого количества соли\n5.Гипергидратация (чрезмерное употребление воды)\n'+
         '6.Гиперальбуминемия (повышенное содержание альбуминов в крови)\n7.ЛОЖНОПОНИЖЕН - при дефиците железа',
          '1.Обезвоживание(за счет уменьшения жидкой части крови)-\nв том числе при рвоте, ожоговой болезни,\n'+
           ' перитоните, чрезмерном приеме мочегонных препаратов\n 2.Полицитемия(за счет увеличения образования эритроцитов)\n'+
            '-в том числе при различных гипоксиях,приеме кортикостероидов,\nзаболеваниях почек и костной ткани\n'+
            '3.ЛОЖНОПОВЫШЕН при дефиците В9 и В12'], 
        ['Гемоглобин', '14-15', '1. "Спортивное" малокровие - относительное снижение за счет увеличения жидкой части крови\n'+
         '2. Дефицит микроэлементов: железа, селена, цинка,  меди\n'+
         '3. Дефицит витаминов В9, В12, Д, А, Е\n'+
         '4. Острое и/или хроническое кровотечение\n'+
         '5. Беременность (необходимо смотреть в комплексе с MCV - если он уменьшен,\n'+
          'то это истинная анемия, если нет - относительная).\n', 
          '1. Физиологическое - временное повышение гемоглобина в крови за счет \n'+
          'уменьшения объема жидкой части крови (восстанавливается в течение 24 часов)\n'+
          '2. Гипоксия (компенсаторный механизм) - в том числе при курении,\n'+
          'сердечно-сосудистых и респираторных заболеваниях, в условиях высокогорья\n'+
          '3. Обезвоживание\n'+
          '4. Избыток тестостерона, кортизола, соматотропного гормона и ИФР-1'], 
        ['MVC (средний объем эритроцитов)', '83-85', '1. Дефицит железа\n2. Дефицит меди\n'+
         '3. Наследственные гемолитические анемии (талассемия, микросфероцитоз)', '1. Дефицит витамина В9\n'+
         '2. Дефицит витамина В12'], 
        
        ]

headings = ['Показатели', 'Оптимум', 'Пониженное значение', 'Повышенное значение']

layout = [  [sg.Menu(main_menu)],
            [sg.Text('\n\n\nОбщий Анализ Крови мужской:             \n')],
            [sg.Table(values=data, headings=headings, max_col_width=60,
                    # background_color='light blue',
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