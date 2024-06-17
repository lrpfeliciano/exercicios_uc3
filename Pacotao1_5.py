'''
Escrever um algoritmo que lê o número de 
identificação, as 3 notas obtidas por um aluno 
nas 3 verificações e a média dos exercícios 
que fazem parte da avaliação. 
Calcular a média de aproveitamento, 
usando a fórmula:

MA = (Nota1 + Nota2 x 2 + Nota3 x 3 + ME )/7

A atribuição de conceitos obedece a tabela 
abaixo:

Média de Aproveitamento Conceito
9,0                            A
7,5 e < 9,0                       B
6,0 e < 7,5                       C
4,0 e < 6,0                       D
< 4,0                           E
'''
identificacao = input("Identificação: ")
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
me = float(input("Média de exercícios: "))

ma = (n1 + n2 * 2 + n3 * 3 + me) / 7
if ma >= 9:
    print("A")
elif ma >= 7.5 and ma < 9:
    print("B")
elif ma >= 6 and ma < 7.5:
    print("C")
elif ma >= 4 and ma < 6:
    print("D")
else:
    print("E")