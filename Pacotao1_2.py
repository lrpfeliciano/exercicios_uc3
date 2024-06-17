'''
Faça um programa que receba o ano de nascimento de uma pessoa 
e o ano atual, calcule e mostre:
a) a idade dessa pessoa em anos;
b) a idade dessa pessoa em meses;
c) a idade dessa pessoa em dias;
'''
nascimento = int(input("Ano de nascimento: "))
atual = int(input("Ano atual: "))

idade = atual - nascimento
print (f'Idade em anos: {idade}')
print (f'Idade em meses: {idade*12}')
print (f'Idade em dias: {idade*365}')
