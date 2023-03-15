"""
Eduard Gibert Ramon

"""
from collections import Counter as C 

def esPrimo(numero):
    """
    Devuelve **True** si su argumento es primo, y **False** si no lo es.  

    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    """
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True                         

def primos(numero):
    """
    Devuelve una **tupla** con todos los números primos menores que su argumento.

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """

    return tuple([prueba for prueba in range(2, numero) if esPrimo(prueba)])

def descompon(numero):
    """
    Devuelve una **tupla** con la descomposición en factores primos de su argumento.

    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
  
    lista = [] #lista vacia

    for prueba in primos(numero):            
        while numero % prueba == 0:          
            lista.append(prueba)            
            numero //= prueba     
                            
    return tuple(lista)                   
    
def mcm(num1, num2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.

    >>> mcm(90, 14)
    630
    """
    
    numero1 = C(descompon(num1))
    numero2 = C(descompon(num2))

    
    fact = numero1 | numero2  

    mcm = 1 
    for factor, exp in fact.items():
        mcm *= (factor**exp)

    return mcm                     


# Usamos un codigo muy parecido al del MCM pero cambiando algunas cosas
def mcd(num1, num2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    
    >>> mcd(924, 780)
    12
    """
    numero1 = C(descompon(num1))
    numero2 = C(descompon(num2))

    fact = numero1 & numero2 

    mcd = 1 
    for factor, exp in fact.items():
        mcd *= (factor**exp)

    return mcd

 
import doctest
doctest.testmod()