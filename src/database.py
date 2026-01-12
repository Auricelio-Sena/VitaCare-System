import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('../clinica.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            cpf TEXT UNIQUE NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()
    print("Banco de dados inicializado com sucesso!")

def salvar_paciente_no_banco(nome, idade, cpf):
    conexao = sqlite3.connect('../clinica.db')
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO pacientes (nome, idade, cpf) 
        VALUES (?, ?, ?)
    ''', (nome, idade, cpf))
    
    # Captura o ID que o banco acabou de gerar
    id_gerado = cursor.lastrowid
    
    conexao.commit()
    conexao.close()
    print(f"Dados de {nome} salvos com sucesso! (ID Gerado: {id_gerado})")

def buscar_pacientes():
    conexao = sqlite3.connect('../clinica.db')
    cursor = conexao.cursor()
    
    # Selecionamos todas as colunas para o ID aparecer
    cursor.execute('SELECT id, nome, idade, cpf FROM pacientes')
    dados = cursor.fetchall()
    
    conexao.close()
    return dados