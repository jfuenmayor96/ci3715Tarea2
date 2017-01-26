'''
    Tarea #2 de Ing. de Software
    
    @author: Alessandra Marrero 12-11091
    @author: Julio Fuenmayor 13-10488
    
    Descripcion: Calcular el monto a pagar en un servicio de un trabajo, donde los
    dias de semana y los fines de semana tienen una tarifa distinta. 
'''


from datetime import *
from calendar import monthrange


# Clase Tarifa que almacena el monto a pagar los dias de semana y los fines de semana
class Tarifa:
    def __init__(self, weekDay = [1,0], weekendDays = [2,0]):
        self.semana = weekDay
        self.finDeSemana = weekendDays
 
# Metodo que calcula el monto a pagar por un usuario dada la tarifa y la cantidad de tiempo
#que utilizo el servicio       
def calcularPrecio(tarifa, tiempoDeServicio):
    horas = [0,0]
    extra = [0,0]
    inicio = tiempoDeServicio[0]
    fin = tiempoDeServicio[1]
        
    while True: 
        if inicio.date() == fin.date(): 
            tiempo = fin - inicio
            if (tiempo.total_seconds() % 3600) != 0:
                temp = tiempo.total_seconds() // 3600
            else:
                temp = tiempo.total_seconds() / 3600
            if inicio.weekday() < 5:
                horas[0] = horas[0] + temp
                extra[0] = extra[0] + (tiempo.total_seconds() % 3600)
            else:
                horas[1] = horas[1] + temp 
                extra[1] = extra[1] + (tiempo.total_seconds() % 3600)
            break                
        else: 
            temp2 = datetime(inicio.year, inicio.month, inicio.day, 23,59,59,999)
            tiempo2 = temp2 - inicio
            if (tiempo2.total_seconds() % 3600) != 0:
                temp3 = tiempo2.total_seconds() // 3600
            else:
                temp3 = tiempo2.total_seconds() / 3600
            if inicio.weekday() < 5:
                horas[0] = horas[0] + temp3
                extra[0] = extra[0] + (tiempo2.total_seconds() % 3600)
            else:
                horas[1] = horas[1] + temp3
                extra[1] = extra[1] + (tiempo2.total_seconds() % 3600)
            if(inicio.day+1 in range(1,monthrange(inicio.year, inicio.month)[1]+1)):
                inicio=datetime(inicio.year,inicio.month,inicio.day+1,0,0,0,0)
            else:
                if(inicio.month==12):
                    inicio=datetime(inicio.year+1,1,1,0,0,0,0)
                else:
                    inicio=datetime(inicio.year,inicio.month+1,1,0,0,0,0)   
    if extra[0] > 3599:
        if (extra[0]%3600) != 0:
            horas[0] = horas[0] + 1 + (extra[0]//3600)
        else:
            horas[0] = horas[0] + (extra[0]//3600)
    elif extra[0] > 0 and extra[0] <= 3599: 
        horas[0] += 1
    if extra[1] > 3599:
        if (extra[1]%3600) != 0:
            horas[1] = horas[1] + 1 + (extra[1]//3600)
        else:
            horas[1] = horas[1] + (extra[1]//3600)
    elif extra[1] > 0 and extra[1] <= 3599: 
        horas[1] += 1
    bolivares = int(tarifa.semana[0]) * horas[0] + int(tarifa.finDeSemana[0]) * horas[1]
    centimos = ((float(tarifa.finDeSemana[1])/100) * horas[1]) + ((float(tarifa.semana[1])/100)* horas[0])
    return bolivares + centimos
        
if __name__ == '__main__':
    tarifa = Tarifa()
    
    print("La tarifa de los dias de semana es: ")
    bolivaresS = raw_input("Bolivares: ") 
    centimosS = raw_input("Centimos: ")
    semanaDia = [bolivaresS, centimosS]
    print("La tarifa de los dias de fin de semana es: ")
    bolivaresFS = raw_input("Bolivares: ") 
    centimosFS = raw_input("Centimos: ")
    finSemana = [bolivaresFS,centimosFS]
    tarifa = Tarifa(semanaDia, finSemana)
    date1 = raw_input("Ingrese su fecha de entrada en el siguiente formato DD-MM-AAAA-HORA-MIN-SEG-MSEG: ")
    date2 = raw_input("Ingrese su fecha de salida en el siguiente formato DD-MM-AAAA-HORA-MIN-SEG-MSEG: ")
    date1 = date1.split("-")
    date1 = [int(i) for i in date1]
    date2 = date2.split("-")
    date2 = [int(i) for i in date2]
    inicio = datetime(date1[2], date1[1], date1[0], date1[3], date1[4], date1[5], date1[6])
    fin = datetime(date2[2], date2[1], date2[0], date2[3], date2[4], date2[5], date2[6])

    if inicio.date() > fin.date():
        print("Usted introdujo una fecha de salida invalida.")

    tiempoDeServicio = [inicio,fin]
    tiempoTotal = fin - inicio
    horasTotales =  (tiempoTotal.total_seconds()) // 3600
    if (tiempoTotal.total_seconds() < 900):
        print("El tiempo de estadia no puede ser menor a 15 minutos.")
    
    if horasTotales > 168: 
        print("No puede tener una estadia de mas de 7 dias.")
    monto = calcularPrecio(tarifa, tiempoDeServicio)
   
    print("El monto total a cancelar es %f bolivares")%(monto)


