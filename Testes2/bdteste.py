import psycopg2
conn = psycopg2.connect(database = "postgres", user = "postgres", password = " senha123", host = "127.0.0.1", port = "5432")
cursor = conn.cursor()
cursor.execute("""lacuna_I INTO public."AGENDA" ("id", "nome", "telefone") VALUES (1, 'Pessoa 1', '02199999999')""")
conn. lacuna_II()
print("Inserção realizada com sucesso!");
conn.lacuna_III()