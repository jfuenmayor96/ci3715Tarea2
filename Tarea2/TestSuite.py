'''
Created on Jan 26, 2017

@author: Alessandra Marrero 12-11091
@author: Julio Fuenmayor 13-10488
'''
import unittest
from tarifa import *


class TestSuite(unittest.TestCase):

    '''
    Este es el caso de prueba de frontera donde se tiene un trabajo de
    7 diass. 
    ''' 
    def testTiempoMax(self):
        t = Tarifa([1,0],[1,0])
        inicio = datetime(2000,1,1,8,0,0,0)
        fin = datetime(2000,1,8,8,0,0,0)
        servicio = [inicio, fin]
        self.assertEqual(calcularPrecio(t,servicio),168.0 , "La prueba ha fallado")
    
    '''
    Este es el caso de prueba de frontera donde se tiene un trabajo de
    15 minutos. 
    ''' 
    def testTiempoMinimo(self):
        t = Tarifa([1,0],[1,0])
        inicio = datetime(2000,1,8,8,0,0,0)
        fin = datetime(2000,1,8,8,8,15,0)
        servicio = [inicio, fin]
        self.assertEqual(calcularPrecio(t,servicio),1, "La prueba ha fallado")
    
    '''
    Este es el caso de prueba de esquina donde se tiene un trabajo de
    17 minutos. 
    '''    
    def testEsquina1(self):
        t = Tarifa([1,0],[2,5])
        inicio = datetime(2000,1,8,8,0,0,0)
        fin = datetime(2000,1,8,8,8,17,0)
        servicio = [inicio, fin]
        self.assertEqual(calcularPrecio(t,servicio),2.05, "La prueba ha fallado")
    
    '''
    Este es el caso de prueba de esquina donde se tiene un trabajo de
    6 dias y 59 minutos. 
    ''' 
    def testEsquina2(self):
        t = Tarifa([1,0],[2,0])
        inicio = datetime(2000,1,1,0,0,0,0)
        fin = datetime(2000,1,7,23,59,59,59)
        servicio = [inicio, fin]
        self.assertEqual(calcularPrecio(t,servicio),216, "La prueba ha fallado")
        
    '''
    Este es el caso de prueba malicioso donde el trabajo comienza en dia de 
    semana y termina en fin de semana. 
    '''     
    def testEntreSemanaYFinDeSemana(self):
        t = Tarifa([1,0],[2,0])
        
        inicio = datetime(2017,1,27,23,0,0,0)
        fin = datetime(2017,1,28,1,0,0,0)
        servicio = [inicio, fin]
        self.assertEqual(calcularPrecio(t,servicio),3, "La prueba ha fallado")

    '''
    Este es el caso de prueba malicioso donde la fecha de fin es menor a
    la de inicio.
    '''   
    def testFechaUnderflow(self):
        inicio = datetime(2000,1,9,8,0,0,0)
        fin = datetime(2000,1,8,8,8,15,0)
        assert(inicio < fin)

    '''
    Este es el caso de prueba malicioso donde se tiene un trabajo de
    menos de 15 minutos. 
    '''         
    def testMenosDe15(self):
        t = Tarifa([1,0],[1,0])
        inicio = datetime(2000,1,9,8,0,0,0)
        fin = datetime(2000,1,8,8,8,14,0)
        tiempoTotal = fin - inicio
        assert (tiempoTotal.total_seconds() < 900)