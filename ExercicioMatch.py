'''
Faça um programa que fará a leitura de dois números e o operador 
(+, - , * e /)
'''
n1 = int(input("Informe o número: "))
n2 = int(input("Informe outro número: "))
op = input("Informe o operador: ")
r = 0
match op:
    case "+":
        r = n1 + n2
    case "-":
        r = n1 - n2
    case "*" | "x" | "X" | ".":
        r = n1 * n2
    case "/" | ":":
        if n2 != 0:
            r = n1 / n2
    case _:
        print("Operador inválido")

print(f"O resultado é {r}")