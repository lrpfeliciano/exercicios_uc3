resp = ''
totalSalario = 0
totalFilhos = 0
quantidade = 0
while True:
    # Comentário de uma linha
    salario = float(input("Informe salário: "))
    filhos = int(input("Informe número de filhos: "))

    totalSalario = totalSalario + salario
    totalFilhos = totalFilhos + filhos
    quantidade += 1

    resp = input("Deseja continuar? (s/n) ").lower()
    if resp == 'n':
        break
    '''
    '''
mediaSalario = totalSalario / quantidade
mediaFilhos = totalFilhos / quantidade
print(f"A média de salários é {mediaSalario:.2f}")
print(f"A média de filhos é {mediaFilhos:.2f}")
print("fim")