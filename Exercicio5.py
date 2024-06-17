'''
Faça um programa que calcula e apresente o valor do volume 
de um recipiente, utilizando a fórmula 
Volume = 3.14159 * raio * raio * altura
'''
r = float(input("Informe o raio: "))
a = float(input("Informe a altura: "))

v = 3.14159 * r * r * a
print(f"O volume é {v:.2f}")

v = 3.14159 * r ** 2 * a
print(f"O volume é {v:.2f}")
