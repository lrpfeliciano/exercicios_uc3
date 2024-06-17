'''
vetorNome = []
vetorIdade = []
vetorEmail = []
vetorEndereco = []
vetorTelefone = []
'''

agenda = []
while True:
    nome = input("Informe nome: ")
    idade = int(input("Informe a idade: "))
    email = input("Informe o e-mail: ")
    endereco = input("Informe o endereço: ")
    telefone = input("Informe o telefone: ")

    agenda.append([nome, idade, email, endereco, telefone])

    r = input("Deseja continuar (s/n) ? ").lower()
    if r == 'n':
        break

for contato in agenda:
    if contato[1] <= 18:
        for item in contato:
            print (item)


#Nome 
print(agenda[0][0])
print(agenda[1][0])
