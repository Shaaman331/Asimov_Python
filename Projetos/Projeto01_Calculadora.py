import os

print("===================")
operations = {
    "+": "Soma",
    "-": "Subtracao",
    "*": "Multiplicacao",
    "/": "Divisao",
    "^": "Exponenciacao",
}

while True:
    os.system("clear" if os.name == "posix" else "cls")  # Limpa a tela
    i = 0
    for op, name in operations.items():
        print(i, ":", name)
        i += 1

    print("")
    print("Escolha a operação:")
    op_index = int(input())
    
    # Verifica se o índice da operação é válido
    if op_index < 0 or op_index >= len(operations):
        print("Operação inválida! Tente novamente.")
        continue

    op_strings = list(operations.keys())[op_index]
    
    print("") 
    print("{} escolhida".format(op_strings))
    print("")
    print("Qual o primeiro valor? ")
    num1 = float(input())
    print("")
    print("Qual o segundo valor? ")
    num2 = float(input())
    print("")

    # Realiza a operação escolhida
    if op_strings == "+":
        result = num1 + num2
    elif op_strings == "-":
        result = num1 - num2
    elif op_strings == "*":
        result = num1 * num2
    elif op_strings == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Erro: Divisão por zero!")
            continue
    elif op_strings == "^":
        result = num1 ** num2

    print("")
    print("{} {} {} = {}".format(num1, op_strings, num2, result))
    print("")
    print("===================")

    cont = input("Deseja continuar? (S/N) ")
    if cont.upper() == "N":
        break