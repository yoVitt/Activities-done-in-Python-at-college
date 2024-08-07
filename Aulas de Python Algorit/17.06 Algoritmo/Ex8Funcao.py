def valorPagamento():
    diarioNao = []
    diarioPago = []

    while True:
        val = float(input("Digite o valor da prestação: "))
        atr = int(input("Digite os dias de atraso: "))
        if atr > 0:
            total = 0.00
            multa = 0.3
            multa_dia = 0.001 * atr
            total = val+(val*multa_dia)+(val*multa)
        else:
            total = val

        print(f"O valor total a ser pago é R${total}")
        i = input("Você deseja pagar essa prestação? S=SIM; N=NÃO: ").upper()
        if i == 'S':
            diarioPago.append(total) # Adiciona na lista o valor pago
        else:
            diarioNao.append(total)

        continuar = input("Digite S para continuar ou N para sair: ").upper()
        if continuar == 'N':
            break

    print(f"As prestações pagas de hoje foram {diarioPago}")
    print(f"As adiadas/Não pagas de hoje foram {diarioNao}")
    print("Encerrado")


valorPagamento()