# 1. Sistema de Filmes Favoritos
def sistema_filmes():
    print("\n=== Sistema de Filmes Favoritos ===")
    filmes = []
    contador = 1
    
    # Adiciona 5 filmes à lista
    while contador <= 5:
        filme = input(f"Digite o nome do {contador}º filme favorito: ")
        filmes.append(filme)
        contador += 1
    
    print("\nLista de Filmes Favoritos:")
    # Imprime os filmes usando enumerate
    for indice, filme in enumerate(filmes):
        print(f"Posição {indice + 1}: {filme}")

# 2. Sistema de Material Escolar
def sistema_material():
    print("\n=== Sistema de Material Escolar ===")
    # Primeiro dicionário com 3 itens
    materiais1 = {
        "001": "Caderno",
        "002": "Lápis",
        "003": "Borracha"
    }
    
    # Segundo dicionário vazio
    materiais2 = {}
    contador = 1
    
    # Adiciona 5 itens ao segundo dicionário
    while contador <= 5:
        codigo = input(f"\nDigite o código do {contador}º produto: ")
        tipo = input(f"Digite o tipo do {contador}º material: ")
        materiais2[codigo] = tipo
        contador += 1
    
    # Atualiza o primeiro dicionário com o conteúdo do segundo
    materiais1.update(materiais2)
    
    print("\nLista completa de materiais:")
    for codigo, tipo in materiais1.items():
        print(f"Código: {codigo} - Material: {tipo}")

# 3. Sistema de Cadastro de Alunos
def sistema_alunos():
    print("\n=== Sistema de Cadastro de Alunos ===")
    alunos = {}
    contador = 1
    
    # Cadastra 5 alunos
    while contador <= 5:
        print(f"\nCadastro do {contador}º aluno:")
        matricula = input("Digite a matrícula: ")
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        email = input("Digite o e-mail: ")
        
        # Armazena os dados do aluno em uma lista
        dados_aluno = [nome, sobrenome, email]
        # Adiciona a lista ao dicionário com a matrícula como chave
        alunos[matricula] = dados_aluno
        
        contador += 1
    
    print("\nDados dos alunos cadastrados:")
    for matricula, dados in alunos.items():
        print(f"\nMatrícula: {matricula}")
        print(f"Nome: {dados[0]} {dados[1]}")
        print(f"E-mail: {dados[2]}")

# Menu principal
def menu():
    while True:
        print("\n=== Menu Principal ===")
        print("1 - Sistema de Filmes Favoritos")
        print("2 - Sistema de Material Escolar")
        print("3 - Sistema de Cadastro de Alunos")
        print("4 - Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            sistema_filmes()
        elif opcao == "2":
            sistema_material()
        elif opcao == "3":
            sistema_alunos()
        elif opcao == "4":
            print("Programa encerrado!")
            break
        else:
            print("Opção inválida!")

# Executa o programa
if __name__ == "__main__":
    menu()