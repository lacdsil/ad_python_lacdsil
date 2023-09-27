import pyodbc

def acesso_banco():
    connection = pyodbc.connect(retorna_conexao())
    cursor = connection.cursor()
    return cursor, connection
    
def retorna_conexao():
    return(
        "DRIVER={SQL SERVER};"
        "SERVER=HOESQL633;"
        "DATABASE=SkillUp_LACDSIL;"
        "Trusted_Connection=yes;"
    )
    
def select_banco_dados():
  cursor, connection = acesso_banco()
  cursor.execute("select * from cliente;")
  clientes = cursor.fetchall()
  print(clientes)
  connection.commit()
  
def select_cpf(cpf):
  cursor, connection = acesso_banco()
  cursor.execute("select * from cliente WHERE cpf = '" + cpf + "';")
  clientes = cursor.fetchall()
  print(clientes)
  connection.commit()
  
def insert_banco_dados(cliente):
  cursor, connection = acesso_banco()
  insert_query = """
  INSERT INTO cliente (nome, cpf, rg, data_nascimento, cep, numero_residencia)
  VALUES (?, ?, ?, ?, ?, ?);
  """

  values = (cliente['Nome'], cliente['CPF'],cliente['RG'], cliente['Nascimento'], cliente['Endereco'], cliente['Numero'] )
  cursor.execute(insert_query, values)
  connection.commit()
  
  
def update_cpf(cliente):
  cursor, connection = acesso_banco()
  cpf_local = cliente['CPF']
  print(cpf_local)
  update_query = "UPDATE cliente SET nome = ?, cpf = ?, rg = ?, data_nascimento = ?, cep = ?, numero_residencia = ? cpf = '02912820081';"
  values_update = (cliente['Nome'], cliente['CPF'], cliente['RG'], cliente['Nascimento'], cliente['Endereco'], cliente['Numero'] )
  cursor.execute(update_query, values_update)
  connection.commit()



def delete_banco_dados(cpf):
  cursor, connection = acesso_banco()
  delete_query = "DELETE FROM cliente WHERE cpf = '" + cpf + "';"
  cursor.execute(delete_query)
  connection.commit() 
  
def update_banco_dados(cliente):
  cursor, connection = acesso_banco()
  update_query = """
  INSERT INTO cliente (nome, cpf)
  VALUES (?, ?);
  """

  values = (cliente['Nome'], cliente['CPF'])
  cursor.execute(update_query, values)
  connection.commit()
  