import psycopg2
from faker import Faker

conn = psycopg2.connect(
       database="lojadb",
       user="postgres",
       password="senha123",
       host="127.0.0.1",
       port="5432"
   )

print("Conexão com o banco de dados aberta com sucesso!")
cur = conn.cursor()
cur.execute('''
       CREATE TABLE PRODUTO (
           CODIGO SERIAL PRIMARY KEY,
           NOME VARCHAR(100) NOT NULL,
           PRECO NUMERIC(10, 2) NOT NULL
       );
   ''')
conn.commit()
print("Tabela criada com sucesso!")
conn.close()