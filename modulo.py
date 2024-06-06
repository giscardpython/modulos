def exibir_menu():
    print('1 - Calcular Quadrilátero')
    print('2 - Calcular Círculo')
    print('3 - Calcular Triângulo')
    print('4 - Calcular Trapézio')
    print('5 - Sair do programa')

def calcular_quadrilatero(base, altura):
    area_quadrilatero = base * altura
    return area_quadrilatero

def calcular_circulo(raio):
    area = 3.141592 * raio * raio
    return area

def calcular_triangulo(base, altura):
    area_triangulo = (base * altura) / 2
    return area_triangulo

def calcular_trapezio(altura, base_menor, base_maior):
    area_trapezio = (altura * (base_menor + base_maior) / 2)
    return area_trapezio

