'''
Faça um programa que converta uma temperatura em Celsius 
para Fahrenheit utilizando a fórmula abaixo:
 F = 9C / 5 + 32
'''
celsius = float(input("Informe a temperatura em Celsius: "))
fahrenheit = 9 * celsius / 5 + 32
print(f'A temperatura é {fahrenheit:.2f}')