# import modulo -> importa todas as funções
# from modulo import * -> importa todas as funções

# só importa uma função ou varias funções do módulo
#from modulo import calcular_quadrilatero, calcular_circulo 

import os
from modulo import *

if __name__ == "__main__":
    while True:
        exibir_menu()
        opcao = input('Opção desejada: ')

        match opcao:
            case '1':
                b = int(input('\nInforme o valor da base: '))
                h = int(input('Informe o valor da altura: '))
                print(f'Area do quadrilátero: {calcular_quadrilatero(b, h)}.')
                continue
            case '2':
                r = int(input('\nInforme o valor do raio: '))
                print(f'Area do círculo:      {calcular_circulo(r)}.')
                continue
            case '3':
                b = int(input('\nInforme o valor da base: '))
                h = int(input('Informe o valor da altura: '))
                print(f'Area do triângulo:      {calcular_triangulo(b, h)}.')
                continue
            case '4':
                h = int(input('Informe o valor da altura: '))
                bmenor = int(input('\nInforme o valor da base menor: '))
                bmaior = int(input('\nInforme o valor da base maior: '))
                print(f'Area do trapézio:      {calcular_trapezio(h, bmenor, bmaior)}.')
                continue
            case '5':
                break
            case _:
                print('Opção inválida!')
                continue