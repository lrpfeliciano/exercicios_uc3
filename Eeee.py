a = int(input("Informe número: "))
b = int(input("Informe outro número: "))
op = input("Informe a operação")

r = 0
if op == "+":
    r = a + b
elif op == "-":
    r = a - b
elif op == "*":
    r = a * b
elif op == "/":
    r = a / b
else:
    print ("Operação inválida")


