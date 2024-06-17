from funcoes import cadastrar, cadastrarMarca, listar, listarVeiculos
import os
frota = []

while True:
    os.system("cls" if os.name == 'nt' else 'clear' )    
    print("Concessionária")
    print("1 - Cadastrar Veículos")
    print("2 - Listar Veículos")
    print("3 - Cadastrar Marca")
    print("4 - Listar Marca")
    print("0 - Sair")
    try: 
        opcao = input("Digite opção: ")
        match(opcao):
            case '1':
                cadastrar(frota)
            case '2':
                listarVeiculos()
            case '3':
                cadastrarMarca()
            case '4':
                pass
            case '0':
                print("Até a próxima.")
                break
            case _:
                print("Opção inválida.")
    except:
        print("Erro na seleção da opção.")


'''
for carro in frota:
    print(f'Carro: {carro["nome"]}')
    print(f'Ano: {carro["ano"]}')    
    print(f'Valor: {carro["valor"]}')
    print(f'Descrição: {carro["descricao"]}')
    print(f'Tipo: {carro["tipo"]}')
    print("_"*100)
'''