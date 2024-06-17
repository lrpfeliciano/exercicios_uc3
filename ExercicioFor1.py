'''
1) Faça um programa que peça 10 números 
inteiros, calcule e mostre a quantidade de 
números pares e a quantidade de números 
ímpares.
'''
quantPar = 0
quantImpar = 0
for numero in range(10):
    n = int(input("Informe o número: "))
    if n % 2 == 0:
        quantPar += 1
    else:
        quantImpar += 1

print(f"Qtde. número de pares: {quantPar}")
print(f"Qtde. número de ímpares: {quantImpar}")

