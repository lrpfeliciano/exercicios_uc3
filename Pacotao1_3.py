'''
Faça um programa fará a leitura de uma 
temperatura em graus Kelvin e apresentá-la em 
graus Celsius.
A fórmula da conversão é C = K - 273.15323
'''
k = float(input("Temperatura em Kelvin: "))
c = k - 273.15323
print (f'{k:.2f} em kelvin equivale a {c:.2f}°C')