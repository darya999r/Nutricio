import sqlite3

def current_patients_name():
    #  Устанавливаем соединение с базой данных
    connection = sqlite3.connect('patients.db')
    cursor = connection.cursor()

    # Выбираем всех пользователей
    cursor.execute("SELECT name FROM Registration_data WHERE current_or_archive = '1'")
    users = cursor.fetchall()

    # Преобразуем данные в массив
    cur_pat_users = []
    for i in range(len(users)):
        cur_pat_users.append(users[i][0])

    # Закрываем соединение
    connection.close()
    return cur_pat_users

def all_data_patient(patient_name):
    #  Устанавливаем соединение с базой данных
    connection = sqlite3.connect('patients.db')
    cursor = connection.cursor()

    # Выбираем всех пользователей
    cursor.execute("SELECT id_patient FROM Registration_data WHERE name = ?", (patient_name,))
    id_pat = cursor.fetchone()
    patient = id_pat[0]

    # Получаем регистрационные данные
    cursor.execute("SELECT * FROM Registration_data WHERE id_patient = ?", (patient,))
    reg = cursor.fetchall()
    data_reg = []
    for i in range(len(reg[0])):
        data_reg.append(reg[0][i])

    # Получаем данные антропометрии
    cursor.execute("SELECT * FROM Anthropometry WHERE id_patient = ?", (patient,))
    antr = cursor.fetchall()
    data_antr = []
    for i in range(len(antr[0])):
        data_antr.append(antr[0][i])

    # Получаем данные измерений
    cursor.execute("SELECT * FROM Measurements WHERE id_patient = ?", (patient,))
    meas = cursor.fetchall()
    data_meas = []
    for i in range(len(meas[0])):
        data_meas.append(meas[0][i])
    
    # Получаем данные стиля жизни
    cursor.execute("SELECT * FROM Life_style WHERE id_patient = ?", (patient,))
    life = cursor.fetchall()
    data_life = []
    for i in range(len(life[0])):
        data_life.append(life[0][i])
    
    # Закрываем соединение
    connection.close()

    return data_reg, data_antr, data_meas, data_life

def analisis_name():
    #  Устанавливаем соединение с базой данных
    connection = sqlite3.connect('patients.db')
    cursor = connection.cursor()

    # Выбираем всех пользователей
    cursor.execute("SELECT name_analisis FROM Analises")
    a = cursor.fetchall()

    # Преобразуем данные в массив
    all_analises = []
    for i in range(len(a)):
        all_analises.append(a[i][0])

    # Закрываем соединение
    connection.close()
    return all_analises

def data_analises(analisis_name):
    #  Устанавливаем соединение с базой данных
    connection = sqlite3.connect('patients.db')
    cursor = connection.cursor()

    # Выбираем всех пользователей
    cursor.execute("SELECT id_analisis FROM Analises WHERE name_analisis = ?", (analisis_name,))
    id_an = cursor.fetchone()
    an = id_an[0]

    # Получаем регистрационные данные
    cursor.execute("SELECT * FROM Indicators_analises WHERE id_analisis = ?", (an,))
    analisis = cursor.fetchall()
    data_an = []
    for i in range(2):
        data_an.append(analisis[0][i])

    # Закрываем соединение
    connection.close()

    return analisis

def archive_patients_name():
    #  Устанавливаем соединение с базой данных
    connection = sqlite3.connect('patients.db')
    cursor = connection.cursor()

    # Выбираем всех пользователей
    cursor.execute("SELECT name FROM Registration_data WHERE current_or_archive = '0'")
    users = cursor.fetchall()

    # Преобразуем данные в массив
    arch_pat_users = []
    for i in range(len(users)):
        arch_pat_users.append(users[i][0])

    # Закрываем соединение
    connection.close()
    return arch_pat_users

def all_data_archive_patient(patient_name):
    #  Устанавливаем соединение с базой данных
    connection = sqlite3.connect('patients.db')
    cursor = connection.cursor()

    # Выбираем всех пользователей
    cursor.execute("SELECT id_patient FROM Registration_data WHERE name = ?", (patient_name,))
    id_pat = cursor.fetchone()
    patient = id_pat[0]

    # Получаем регистрационные данные
    cursor.execute("SELECT * FROM Registration_data WHERE id_patient = ?", (patient,))
    reg = cursor.fetchall()
    data_reg = []
    for i in range(len(reg[0])):
        data_reg.append(reg[0][i])

    # Получаем данные антропометрии
    cursor.execute("SELECT * FROM Anthropometry WHERE id_patient = ?", (patient,))
    antr = cursor.fetchall()
    data_antr = []
    for i in range(len(antr[0])):
        data_antr.append(antr[0][i])

    # Получаем данные измерений
    cursor.execute("SELECT * FROM Measurements WHERE id_patient = ?", (patient,))
    meas = cursor.fetchall()
    data_meas = []
    for i in range(len(meas[0])):
        data_meas.append(meas[0][i])
    
    # Получаем данные стиля жизни
    cursor.execute("SELECT * FROM Life_style WHERE id_patient = ?", (patient,))
    life = cursor.fetchall()
    data_life = []
    for i in range(len(life[0])):
        data_life.append(life[0][i])
    
    # Закрываем соединение
    connection.close()

    return data_reg, data_antr, data_meas, data_life