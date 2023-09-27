from utils import *
from banco_dados import *

def menu_cliente():
 validador_menu = True
 cliente_dicionario_update = []
 cliente_dicionario = []
 numero_cpf = 12345656789
 while validador_menu:
    print("1 - Cadastrar Cliente")
    print("2 - Alterar Cliente")
    print("3 - Buscar Cliente")
    print("4 - Deletar Cliente")
    print("5 - Listar Clientes")
    print("6 - Voltar ao menu anterior\n")
    opcao_cliente = int(input("Digite a opção desejada:\n"))
    if opcao_cliente == 1:
         cliente_dicionario = {
         "Nome": input("Digite o Nome: "),
         "CPF": valida_cpf(numero_cpf),
         "RG": valida_rg(input("Digite o RG: ")),
         "Nascimento": valida_data_nascimento(),
         "Endereco": input("Digite o CEP: "),
         "Numero": input("Digite o Número da casa: ")}
         insert_banco_dados(cliente_dicionario)
    elif opcao_cliente == 2:
        cliente_dicionario_update = {
         "Nome": input("Digite o Nome: "),
         "CPF": valida_cpf(numero_cpf),
         "RG": valida_rg(input("Digite o RG: ")),
         "Nascimento": valida_data_nascimento(),
         "Endereco": input("Digite o CEP: "),
         "Numero": input("Digite o Número da casa: ")}
        update_cpf(cliente_dicionario_update)
    elif opcao_cliente == 3:
          busca_cpf = input("Digite o CPF do cliente para busca:")
          select_cpf(busca_cpf)
    elif opcao_cliente == 4:
        remove_cpf = input("Digite o CPF do cliente a ser removido:")
        delete_banco_dados(remove_cpf)
        print("Cliente removido com sucesso.")
    elif opcao_cliente == 5:
        select_banco_dados()
    elif opcao_cliente == 6:
        validador_menu = False
    else:
        print("opcao invalida")