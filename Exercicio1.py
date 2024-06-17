# Python
'''
Faça um programa que realiza a leitura do total de uma compra e 
o número de parcelas. O programa deverá informar o valor da 
parcela.
'''
valorTotal = float(input("Informe o valor total: "))
numeroParcela = int(input("Informe o número de parcelas: "))

valorParcela = valorTotal / numeroParcela

print(f"O valor da parcela é: {valorParcela:.2f}")