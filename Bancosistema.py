menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITES_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        valor = float(input("Digite o valor que deseja depositar"))

        if valor > 0:
            saldo += valor
            extrato = f"O valor do deposito foi de: {valor: .2f}\n"
        else:
            print("Número inválido, por favor tente novamente")
    elif opcao == "s":
        
        valor = float(input("Digite o valor a ser sacado"))
        if valor > saldo:
            print("operação invalida, sem saldo!")
        elif valor > limite:
            print("Operação excede o limite permitido, tente novamente") 
        elif numero_saque > LIMITES_SAQUE:
            print("Essa operação é inválida")    
        elif valor > 0:
            saldo -= valor
            extrato = f"o saque foi de {valor: .2f}\n"
            numero_saque += 1
        else:
            print("Esse numero não é válido")
    elif opcao == "e":
        print("Não foram realizadas operações" if not extrato else extrato)
        print(f"O saldo é:{saldo: .2f}\n")
    elif opcao == "q":
        print("Obrigada por utilizar nossos servioços, volte sempre")
    else:
        print("Opção invalida")
