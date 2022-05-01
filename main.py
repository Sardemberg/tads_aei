from matriz import Matriz

cont = -1
matriz = Matriz()

operacoes = {
    1: matriz.mostrar_matriz,
    2: matriz.mostrar_transposta,
    3: matriz.soma_diagonal_princial,
    4: matriz.numeros_pares,
    5: matriz.numeros_impares
}

while cont != 0:
    print("\nEscolha a operação que deseja realizar: ", end="\n\n")
    matriz.mostrar_menu()
    operacao = int(input())
    print("")
    cont = operacao
    if operacao != 0: operacoes[operacao]()



