'''
1) Tendo como dados de entrada a altura e o 
sexo de uma pessoa ("M" masculino e "F" 
feminino), construa um algoritmo que calcule 
seu peso ideal, utilizando as seguintes 
fórmulas:
 - para homens: (72.7*h)-58
 - para mulheres: (62.1*h)-44.7

'''
altura = float(input("Informe a altura: "))
sexo = input("Informe o sexo: ")
peso = 0
if sexo == 'm' or sexo == 'M':
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.7
print (f"O seu peso ideal {peso:.2f}") 