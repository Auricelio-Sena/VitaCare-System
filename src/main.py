from database import inicializar_banco, salvar_paciente_no_banco
from modules.paciente import Paciente
from modules.consulta import Consulta

# 1. Inicia o banco de dados ao abrir o programa
inicializar_banco()

# 2. Lista para guardar pacientes na memória (temporário)
pacientes_cadastrados = []

while True:
    print("\n--- MENU VITACARE ---")
    print("1. Cadastrar Paciente")
    print("2. Ver Relatório Geral")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- CADASTRO DE PACIENTE ---")
        nome = input("Nome do paciente: ")
        idade = int(input("Idade: "))
        cpf = input("CPF: ")

        # Criamos o objeto e guardamos na lista
        novo_p = Paciente(nome, idade, cpf)
        pacientes_cadastrados.append(novo_p)

        # Salvamos no banco de dados (SQLite)
        salvar_paciente_no_banco(nome, idade, cpf)
        
        print(f"Paciente {nome} cadastrado e salvo com sucesso!")

    elif opcao == "2":
        from database import buscar_pacientes
        dados_do_banco = buscar_pacientes()
        
        print("\n=== RELATÓRIO GERAL (DADOS DO BANCO) ===")
        for p in dados_do_banco:
            # p[0] é o ID, p[1] o nome, p[2] a idade e p[3] o CPF
            print(f"ID: {p[0]} | Nome: {p[1]} | CPF: {p[3]}")

    elif opcao == "3":
        print("Encerrando o sistema...")
        break 
    
    else:
        print("Opção inválida! Tente novamente.")

        elif opcao == "3":
        print("Encerrando o sistema...")
        break # Sai do loop