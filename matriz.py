class Matriz:
    def __init__(self):
        self.matriz = [[9, 7, 4, 2], [10, 13, 18, 21], [33, 5, 7, 90], [23, 31, 51, 60]]

    def mostrar_matriz(self):
        for row in self.matriz:
            for number in row:
                print(number, end=" ")
            print("")
            
    def mostrar_menu(self):
        print("1 - Mostrar matriz original")
        print("2 - Mostrar matriz transposta")
        print("3 - Soma da diagonal principal")
        print("4 - Números pares")
        print("5 - Números ímpares")
        print("0 - Sair do sistema")
        print("")

    def mostrar_transposta(self):
        matriz_tranposta = list(map(list,zip(*self.matriz)))
        for row in matriz_tranposta:
            for number in row:
                print(number, end=" ")
            print("")
    

    def soma_diagonal_princial(self):
        matriz = self.matriz
        soma = matriz[0][0] + matriz[1][1] + matriz[2][2] + matriz[3][3]
        print(soma)


    def numeros_pares(self):
        print("Números pares: ", end="")
        for row in self.matriz:
            for number in row:
                if (number % 2 == 0):
                    print(number, end=" ")

    def numeros_impares(self):
        print("Números ímpares: ", end="")
        for row in self.matriz:
            for number in row:
                if (number % 2 != 0):
                    print(number, end=" ")