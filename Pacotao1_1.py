'''
Faça um programa que fará a leitura de duas notas
e irá calcular a média

Se a média for maior ou igual a 7, o programa irá escrever 
"Aprovado"
Senão o programa irá pedir a nota de recuperação,
e fará um novo cálculo de média envolvendo a  
média com a recuperação.
   Se a nova média for maior ou igual a 6, 
    o programa escreverá "Aprovado" senão, escreverá "Reprovado"
'''
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
m = (n1 + n2) / 2

if m >= 7:
    print("Aprovado")
else:
    # Continuar o fluxo do reprovado
    r = float(input("Nota de recuperação: "))        
    nm = (m + r) / 2
    if nm >= 6:
        print("Aprovado")
    else:
        print("Reprovado")
