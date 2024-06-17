# Vetor - Conjunto - Array - Lista

vetor = [] # Declarando o vetor
vetor.append("Luis") # Adicionando elementos
vetor.append("Renato")
vetor.append("Pedro")
print(vetor)
print(vetor[0]) # 0 é a primeira posição do vetor


vetor.append(input("Informe o nome: "))
vetor.append(1981)
print(vetor)

# "len" retorna o número de elementos de um vetor
print(len(vetor)) 

for nome in vetor:
    print(nome)

