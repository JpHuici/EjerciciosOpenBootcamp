import time

int_horas = time.strftime("%H")
int_minutos = time.strftime("%M")

if int(int_horas) < 7:
    print("Faltan {} horas y {} minutos para irnos a casa.".format(6 - int(int_horas), 60 - int(int_minutos)))
else:
    print("Hora de irse a casa.")
