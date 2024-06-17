'''
Construa um programa que fará o cálculo do salário líquido 
de um professor. Para fazer esse cálculo, é necessário que 
sejam lidos o valor da hora aula, o número de horas dadas 
no mês e o valor total de descontos.
'''
valorHoraAula = float(input("Informe o valor da hora aula: "))
numeroAulas = int(input("Informe o número de horas: "))
d = float(input("Informe o total de descontos: "))

#Salário Líquido
sl = (valorHoraAula * numeroAulas) - d

print(f'O salário líquido é: {sl:.2f}')