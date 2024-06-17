
total = 0
contador = 1
while True:
    valor = float(input(f"Produto {contador}: "))
    
    total += valor
    contador += 1

    if valor == 0:
        break
print(f"Total: R$ {total:.2f}")
recebido = float(input("Dinheiro: R$ "))

troco = recebido - total
print(f"Troco: R$ {troco:.2f}") 