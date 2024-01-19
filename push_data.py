import sqlite3

def push_patient_reg(reg_data):
    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    # Добавляем нового пользователя
    cursor.execute('INSERT INTO Registration_data (name, sex, birth_date, telefon_number, address, email, current_or_archive) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                   (reg_data[0], reg_data[1], reg_data[2], reg_data[3], reg_data[4], reg_data[5], reg_data[6]))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()

def push_patient_antr(antr_data):
    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    # Добавляем нового пользователя
    cursor.execute('INSERT INTO Anthropometry (id_patient, height, weight_fluctuations) VALUES (?, ?, ?)', 
                   (antr_data[0], antr_data[1], antr_data[2]))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()

def push_patient_meas(meas_data):
    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    # Добавляем нового пользователя
    cursor.execute('INSERT INTO Measurements (id_patient, date_measurement, weight, breast_volume, waist, hip_volume, comment) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                   (meas_data[0], meas_data[1], meas_data[2], meas_data[3], meas_data[4], meas_data[5], meas_data[6]))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()

def push_patient_life(life_data):
    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    # Добавляем нового пользователя
    cursor.execute('INSERT INTO Life_style (id_patient, lifestyle, family_status, exercise_stress, sleeping_mode, sleep_quality, drinking_fluids, bad_habits, eating_behavior) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                   (life_data[0], life_data[1], life_data[2], life_data[3], life_data[4], life_data[5], life_data[6], life_data[7], life_data[8]))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()