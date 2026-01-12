# Aqui não precisamos importar o paciente, apenas definir o molde
class Consulta:
    proximo_id_consulta = 1

    def __init__(self, paciente, data, motivo):
        self.id_consulta = Consulta.proximo_id_consulta
        Consulta.proximo_id_consulta += 1
        
        self.paciente = paciente 
        self.data = data
        self.motivo = motivo

    def exibir_agendamento(self):
        print(f"--- CONSULTA AGENDADA [ID: {self.id_consulta}] ---")
        # Pega o nome lá do arquivo de pacientes automaticamente
        print(f"Paciente: {self.paciente.nome}") 
        print(f"Data: {self.data}")
        print(f"Motivo: {self.motivo}")
        print(f"--------------------------------------")