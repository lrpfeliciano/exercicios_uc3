'''
2) Escrever um algoritmo que leia um número, 
o programa calcule e exibirá a tabuada deste 
número. Mostre a tabuada na forma:
1 x n = n
2 x n = 2n
3 x n = 3n
'''
numero = int(input("Informe um número: "))
for i in (1,11):
    r = numero * i
    print(f"{i} x {numero} = {r}")