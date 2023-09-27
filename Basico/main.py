# 1. int: Variáveis int são usadas para armazenar números inteiros. Exemplo: x = 5
# 2. float: Variáveis float são usadas para armazenar números de ponto flutuante (números com casas decimais). Exemplo: pi = 3.14159
# 3. str: Variáveis str (cadeias de caracteres) são usadas para armazenar texto. Exemplo: nome = "João"
# 4. bool: Variáveis bool são usadas para armazenar valores booleanos True (verdadeiro) ou False (falso). Exemplo: ativo = True
# 5. list: Variáveis list são usadas para armazenar sequências mutáveis de elementos. Exemplo: números = [1, 2, 3, 4, 5]
# 6. tuple: Variáveis tuple são usadas para armazenar sequências imutáveis de elementos. Exemplo: coordenadas = (3, 4)
# 7. dict: Variáveis dict (dicionário) são usadas para armazenar pares chave-valor. Exemplo: pessoa = {'nome': 'Maria', 'idade': 30}
# 8. set: Variáveis set (conjunto) são usadas para armazenar coleções de elementos únicos e não ordenados. Exemplo: frutas = {'maçã', 'banana', 'laranja'}
# 9. NoneType: A variável None é usada para representar a ausência de valor ou um valor nulo. Exemplo: vazio = None


# Validador de Balada

#idade = int(input("digite sua idade"))
#if idade < 18:
#  print("nao pode entrar")
#elif idade >= 18:
#  print("pode entrar com restricoes")
#else: 
#  print("pode entrar!")
  
#num = 1*20/1*(10)**2/1*10**2
#print(num)

#Dado o código a seguir, elaborado para um orçamento caseiro, assinale verdadeiro ou falso. 
conta_luz = 70;
conta_agua = 50;
aluguel = 2100;
salario = 3000;
investimento =  salario * 0.3;
gasto_essencial = conta_luz + conta_agua;gasto_essencial += aluguel;lazer = salario - (gasto_essencial + investimento);
print(f' O orçamento da casa é {lazer} reais para lazer, {gasto_essencial} reais para itens essenciais e {investimento} reais para investimentos.')


#Dado o código a seguir, elaborado para um planejamento de investimento, assinale verdadeiro ou falso. 
valor_aplicado = 1000;
rentabilidade_mensal_porcentagem = 0.6814 ;
rentabilidade_mensal = rentabilidade_mensal_porcentagem / 100;
meses_investidos = 12;
valor_final = valor_aplicado * 1+rentabilidade_mensal**meses_investidos;
print('Valor após ',meses_investidos,' meses: R$ ',valor_final);

horario_trasacao = int(input('Em qual horario do dia (0-23)h ocorreu a transação financeira?'));
valor_transacao = float(input('Qual valor da transação financeira feita?'));
limite_seguranca = int(input('Qual o limite de segurança do usuário?'));
if (horario_trasacao > 21 or horario_trasacao < 5 ):
  limite_seguranca*=0.3;
  if (valor_transacao > limite_seguranca):
    print('Transação financeira negada pois ultrapassa o limite permitido.');
elif (valor_transacao <= limite_seguranca):
  print('Transação financeira autorizada.');




  

#valor_inicial = int(input("Digite Valor inicial: "))
#valor_final = int(input("Digite Valor final: "))
#multiplicador = int(input("Digite o multiplicador: "))
#for interador in range(valor_inicial,valor_final):
#  print(interador,"X",multiplicador,"=",interador*multiplicador)