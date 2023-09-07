from os import system
import operacoes as op

s = ["1", "2", "3", "4", "5", "6"]
funcoes = [op.soma, op.diferenca, op.produto, op.dividir, op.potencia]

while (True):
    print("\n\nCALCULADORA PYTHON\n\n1 - SOMA\n2 - DIFERENÇA\n3 - PRODUTO\n4 - DIVISÃO\n5 - POTÊNCIA\n6 - SAIR")

    comando = input("\nCOMANDO: ")
    system("clear")

    if comando not in s:
        print("Comando inválido!")
    elif comando == "6":
        break
    else:
        comando = int(comando)
        system("clear")

        a = float(input("Digite o primeiro valor: "))
        b = float(input("Digite o segundo valor:  "))
        system("clear")

        funcoes[comando - 1](a, b)
