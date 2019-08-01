"""
Conhecendo pep8
python 3
"""


class Calculadora:
    pass


class CalculadoraCientifica:
    pass


def soma():
    pass


def soma_impar():
    pass


numero = 4
idade = 35

numero_impar = 5
name = 'Anderson'


if 'a' in 'banana':
    print ('tem')

print(name)
print(f'{name}')

#cast
# idade = int(input("Qual sua idade?"))
# print(f'Você nasceu em {2019 - idade}')



nome = 'Testing'
lista = [1,2,3,4,5]
numeros = range(1,10)

for letra in nome:
    print(letra)

for numero in lista:
    print(numero)

for numero in range(1,10):
    print(numero)

# from pep8 import falar_ola()  / usa-se este comando para realizar o import da funcion 
#funcion whith return
def falar_ola():
    return "oi"

print(falar_ola())

for i in range(5):
    falar_ola()



def quadrado_de_7():
    print(7*7)