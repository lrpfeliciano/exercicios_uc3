'''
Ler indeterminados nomes e imprimir o número de
nomes lidos
'''
r = ""
quant = 0
while True:
    nome = input("Informe nome: ")
    quant += 1
    r = input("Deseja continuar? (s/n) ").lower()
    if r == 'n':
        break

print(f"A quantidade de nomes: {quant}")