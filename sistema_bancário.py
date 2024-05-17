menu = """

============== MENU ==============

[d] Depositar
[s] Saque
[e] Extrato
[q] Sair

==================================

=>"""

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Insira o valor para depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}.\n"
            
        else:
            print("Operação inválida")
    
    elif opcao == "s":
        valor = float(input("Insira o valor que desejas sacar: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if  excedeu_saldo:
            print("Saldo Insuficiente!")
        
        elif excedeu_limite:
            print("Saque excedeu o limite de R$ 500.00.")
        
        elif excedeu_saques:
            print("Falha! Excedeu o limite de saques diários.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saoque realizado no valor de R$ {valor:.2f}.\n"  
            numero_saques += 1
        else:
            print("Saque Falhou!!")  
            
    elif opcao == "e":
        print("\n================= EXTRATO ================")
        print("Nenhuma movimentação foi feita na sua conta" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == "q":
        break
    
    else:
        print("Operação não reconhecida, por favor tente novamente!")