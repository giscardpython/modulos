# import modulo -> importa todas as funções
# from modulo import * -> importa todas as funções

# só importa uma função ou varias funções do módulo
from modulo import calcular_quadrilatero, calcular_circulo 

b = int(input('\nInforme o valor da base: '))
h = int(input('Informe o valor da altura: '))
print(f'Area do quadrilátero: {calcular_quadrilatero(b, h)}.')

r = int(input('\nInforme o valor do raio: '))
print(f'Area do círculo:      {calcular_circulo(r)}.')
