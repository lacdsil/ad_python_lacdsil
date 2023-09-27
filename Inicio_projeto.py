from cliente import menu_cliente

def menu_inicial(): 
    validador_menu = True
    while validador_menu:
     print("\nSeja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo:\n")
     print ("1 - Cliente")
     print("2 - Ordem")
     print("3 - Realizar análise da carteira")
     print("4 - Imprimir relatório da carteira")
     print("5 - Sair\n")

     opcao_cliente = int(input("Digite a opção desejada:"))
     if opcao_cliente ==1:
          menu_cliente()
     elif opcao_cliente == 2:
          pass
     elif opcao_cliente == 3:
          pass
     elif opcao_cliente == 4:
          pass
     elif opcao_cliente == 5:
          validador_menu = False
          
           
menu_inicial()