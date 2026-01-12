# 🏥 VitaCare-System

Sistema de gestão clínica feito em Python com banco de dados SQLite.

## 🛠️ Ferramentas
* *Python*: Linguagem principal.
* *SQLite*: Banco de dados (já vem com Python).
* *VS Code*: Editor de código.

## 🚀 Como Rodar
1. Baixe o código.
2. No terminal, digite: python src/main.py.

## 📂 O que tem no projeto?
* Cadastro de pacientes.
* Salvamento automático no banco de dados.
* Geração de ID exclusivo para cada pessoa.
* Relatório para ver os pacientes cadastrados.

-------------------------------------------------------------------------------------------------------------------
O que é o VitaCare-System?
O VitaCare-System é um programa de gerenciamento para clínicas médicas. Ele funciona como uma ponte entre o que o usuário digita no teclado e um banco de dados que guarda essas informações para sempre.

Como ele funciona por trás das câmeras?
A Interface (O Menu): O programa roda no terminal (aquela tela preta). Ele apresenta um menu numérico. Quando você escolhe uma opção, o Python decide qual "estrada" seguir: cadastrar um novo paciente ou ler os que já existem.

O Molde (A Classe Paciente): Usamos o conceito de Programação Orientada a Objetos (POO). Imagine que criamos um "formulário em branco" chamado Paciente. Toda vez que você cadastra alguém, o Python preenche uma cópia desse formulário com o nome, idade e CPF que você digitou.

O Banco de Dados (SQLite): Esta é a parte mais importante. Em vez de guardar os nomes apenas na memória do computador (que apaga quando você fecha o programa), o sistema envia esses dados para um arquivo chamado clinica.db.

O "Xerife" (ID): O banco de dados foi configurado para criar um número de identidade (ID) único para cada paciente. Mesmo que você não digite um ID, o banco gera um automaticamente (1, 2, 3...) para garantir que ninguém seja confundido.

O Relatório: Quando você pede para ver o relatório, o Python vai até o arquivo do banco de dados, "lê" todas as linhas que estão salvas lá e as exibe de forma organizada na sua tela, mostrando inclusive o ID que o banco gerou.

Por que essa estrutura é boa?
Organização: O código não está em um lugar só. Existe um arquivo para o menu, outro para o banco de dados e outro para as regras do paciente. Isso facilita encontrar erros.

Segurança de Dados: Como os dados estão em um banco de dados real (SQLite), você pode desligar o computador e, ao ligar amanhã, todas as informações do "Geraldo da Silva" e de outros pacientes continuarão lá.

Ferramentas utilizadas
Python: O "cérebro" que executa a lógica.

SQLite: O "cofre" onde os dados ficam guardados.

VS Code: A "oficina" onde o código foi escrito.

Git: O "histórico" que registra cada evolução que você fez no projeto
