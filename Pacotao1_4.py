'''
O cardápio de uma lanchonete é o seguinte:

Especificação     Código      Preço
Cachorro quente  100             1,20
Bauru simples     101             1,30
Bauru com ovo    102             1,50
Hambúrger          103             1,20
Cheeseburguer    104             1,30
Refrigerante      105             1,00
Escrever um algoritmo que leia o código do item pedido, 
a quantidade e calcule o valor a ser pago por aquele lanche. 
Considere que a cada execução somente será calculado um item.
'''
codigo = input("Código: ")
quantidade = int(input("Quantidade: "))
valor = 0
if codigo == "100":
    valor = quantidade * 1.2
elif codigo == "101":
    valor = quantidade * 1.3
elif codigo == "102":
    valor = quantidade * 1.5
elif codigo == '103':
    valor = quantidade * 1.2
elif codigo == "104":
    valor = quantidade * 1.3
elif codigo == '105':
    valor = quantidade * 1

print(f"O valor é: {valor:.2f}")