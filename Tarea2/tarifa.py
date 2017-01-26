'''
Created on Jan 23, 2017

@author: Alessandra Marrero 12-11091
@author: Julio Fuenmayor
'''
from datetime import *

class Tarifa:
    def __init__(self, weekDay = 1, weekendDays = 2):
        self.semana = weekDay
        self.finDeSemana = weekendDays
    
        
def calcularPrecio(tarifa, tiempoDeServicio):
    
    
    return 
        


if __name__ == '__main__':
    tarifa = Tarifa()
    
    print("La tarifa de los dias de semana es: %d")%(tarifa.semana)
    print("La tarifa de los dias de fin de semana es: %d")%(tarifa.finDeSemana)
    date1 = raw_input("Ingrese su fecha de entrada en el siguiente formato DD-MM-AAAA: ")
    date2 = raw_input("Ingrese su fecha de salida en el siguiente formato DD-MM-AAAA: ")
    date1 = date1.split("-")
    date1 = [int(i) for i in date1]
    date2 = date2.split("-")
    date2 = [int(i) for i in date2]
    
    if date(date2[2], date2[1], date2[0]) < date(date1[2], date1[1], date1[0]):
        print("Usted introdujo una fecha de salida invalida.")
        exit()
    
    
    