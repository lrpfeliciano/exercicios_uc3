'''
2) Uma empresa concederá um aumento de salário aos 
seus funcionários, variável de acordo com o cargo, 
conforme a tabela abaixo. Faça um algoritmo que leia o 
salário e o cargo de um funcionário e calcule o novo salário. 
Se o cargo do funcionário não estiver na tabela, ele deverá, 
então, receber 40% de aumento. 
Mostre o salário antigo, o novo salário e a diferença.

Código  Cargo        Percentual
101     Gerente      10%
102     Engenheiro   20%
103     Técnico      30%
'''
salario = float(input("Salário: "))
cargo = int(input("Cargo: "))
novoSalario = 0
diferenca = 0
if cargo == 101:
    diferenca = salario * 0.1
elif cargo == 102:
    diferenca = salario * 0.2
elif cargo == 103:
    diferenca = salario * 0.3
else:
    diferenca = salario * 0.4
novoSalario = salario + diferenca
print (f'Salario: {salario:.2f}\nDiferenca: {diferenca:.2f}')
print (f'Novo Salário: {novoSalario:.2f}')