vetor = []
numero = -1
# Entrada
while True:
    try:
        numero = int(input("Informe número: "))
        vetor.append(numero)
    except:
        print("Por favor, informe apenas números.")
        

    if numero == 0:
        break


vetor.pop()

vetor.append("Luis")
# Processamento
soma = 0
for n in vetor:
    soma += n

# Saída
print(f"O soma dos elementos é {soma}")
print(f"A quantidade de elementos: {len(vetor)}")

print(f"Utilizando a função sum: {sum(vetor)}")

