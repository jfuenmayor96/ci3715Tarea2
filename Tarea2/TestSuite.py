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