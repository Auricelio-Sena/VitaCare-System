class Paciente:
    def _init_(self, nome, idade, cpf, id=None):
        self.id = id  # O ID agora vem do banco de dados
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def exibir_dados(self):
        # Usamos o ID que o banco gerou
        print(f"--- Ficha do Paciente [ID: {self.id}] ---")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")
        print("-------------------------")