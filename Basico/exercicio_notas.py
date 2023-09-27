# Exercício:

  # Solicitar quantas notas o aluno teve. Receber cada uma dessas notas e armazenar em
  # uma lista. Realizar média do aluno e verificar se ele foi aprovado. Caso tenha nota abaixo de 6 
  # será reprovado, se a nota for 7 ficará de recuperação senão será aprovado. Exibir um dicionário
  # informando: média, maior nota, menor nota e status que deve informar se foi aprovado, recuperado
  # ou se está em recuperação.
  
numero_notas = int(input('Quantas notas o aluno teve?'));
lista_de_notas = [];
while numero_notas > 0:
    print(numero_notas);
    nota = int(input('Entre com a nota numero:'));
    lista_de_notas.append(nota);
    numero_notas = numero_notas-1;

print(lista_de_notas);