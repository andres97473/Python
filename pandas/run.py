import pandas as pd

parsedMessage = ''
data=pd.read_csv('citas.csv')
data_dict = data.to_dict('list')
#Listado de campos
documento = data_dict['num_doc_usr']
phone_no = data_dict['celular']
apellido1 = data_dict['apellido1']
apellido2 = data_dict['apellido2']
nombre1 = data_dict['nombre1']
nombre2 = data_dict['nombre2']
dia_cita = data_dict['fec_cita']
hora_cita = data_dict['hora_cita']
especialidad = data_dict['especialidad']
profesional = data_dict['profesional']
combo = zip(documento,phone_no,apellido1,apellido2,nombre1,nombre2,dia_cita,hora_cita,especialidad,profesional)

for documento,phone_no,apellido1,apellido2,nombre1,nombre2,dia_cita,hora_cita,especialidad,profesional in combo:
    parsedMessage= "Estimando usuario "+nombre1+" "+nombre2+" "+apellido1+" "+apellido2+", "\
        +"La E.S.E. Centro hospital Luis Antonio Montero, le recuerda la oportuna asistencia a si cita "\
        +" de "+especialidad+" "\
        +"El dia "+str(dia_cita)+" a las "+str(hora_cita)+", "\
        +"con el Doctor(a) "+profesional+", "\
        +"En caso de no poder asistir recuerde cancelar con 24 horas de anticipacion."
    print(parsedMessage)

