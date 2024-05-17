menu = """

[d] Depositar
[s] Saque
[e] Extrato
[q] Sair

=>"""
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 500
extrato = ""

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Insira o valor para depositar: "))
        
        if valor > 0:
            saldo = valor
            extrato = f"Depósito de R$ {valor:.2f}\n"
            
        else:
            print("Operação inválida")
    
    elif opcao == "s":
        valor = float(input("Insira o valor que desejas sacar: "))
        
        if valor < saldo & valor < limite:
            saldo = valor - saldo
            extrato = f"Saque de R$ {valor:.2f} realizado\n"
            numero_saques + 1
        
        else:
            print("Saque excedeu o limite")
            
    elif opcao == "e":
        print(extrato)
    
    elif opcao == "q":
        break