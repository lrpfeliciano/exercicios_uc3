'''
Faça um programa fará a leitura de uma temperatura em graus 
Fahrenheit e apresentá-la em graus Celsius.
A fórmula da conversão é C = 5 * (F - 32) / 9
'''
f = float(input("Informe a temperatura em Fahrenheit: "))
c = 5 * (f - 32) / 9
print(f'A temperatura é: {c:.2f}')