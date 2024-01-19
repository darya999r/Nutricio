import pull_data as pld
import Main_window as mw
import Card_patient as cp
import Main_analisis as ma
import Analisis as an
import Archive_search as ars


patient_name = mw.main_window(pld.current_patients_name())
cp.card_patient(pld.all_data_patient(patient_name))

analisis_name = ma.name_analisis(pld.analisis_name()) # возвращает название выбранного анализа
an.analisis(analisis_name)

archive_patient_name = ars.archive_search()
cp.card_patient(pld.all_data_archive_patient(archive_patient_name))