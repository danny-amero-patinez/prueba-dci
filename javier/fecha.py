from datetime import datetime

if True:
	fecha_uno = input('\n')
	fecha1 = datetime.strptime(fecha_uno, '%d/%m/%Y')
	fecha_dos = input('\n')
	fecha2 = datetime.strptime(fecha_dos, '%d/%m/%Y')
	resta = fecha1-fecha2
print(resta)