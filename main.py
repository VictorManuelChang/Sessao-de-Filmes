from sistema import Sistema



def listar_opcoes(opcoes):
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")
    print()


def menu():
    print("╔" + "═"*48 + "╗")
    print("║" + "Bem-vindo à SESSÃO FILMES".center(48) + "║")
    print("╚" + "═"*48 + "╝")
    print("╔" + "═"*48 + "╗")
    print("║" + "1. Cadastrar novo filme".center(48) + "║")
    print("║" + "2. Cadastrar novo gênero".center(48) + "║")
    print("║" + "3. Cadastrar nova plataforma".center(48) + "║")
    print("║" + "4. Listar todos os filmes".center(48) + "║")
    print("║" + "5. Listar todos os gêneros".center(48) + "║")
    print("║" + "6. Listar todas as plataformas".center(48) + "║")
    print("║" + "7. Cadastrar gêneros preferidos do usuário".center(48) + "║")
    print("║" + "8. Recomendar filme".center(48) + "║")
    print("║" + "9. Sair".center(48) + "║")
    print("╚" + "═"*48 + "╝")

def main():
    sistema = Sistema()
    
    while True:
        print("\n")
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print("\n" + "-"*50)
            print("          Cadastro de Novo Filme")
            print("-"*50)
            nome = input("Nome do filme: ")
            ano = input("Ano de lançamento: ")

            print("\nPlataformas disponíveis:")
            plataformas = [p.nome for p in sistema.listar_plataformas()]
            listar_opcoes(plataformas)
            plataforma_idx = int(input("Escolha a plataforma: ")) - 1
            plataforma_nome = plataformas[plataforma_idx]

            print("\nGêneros disponíveis:")
            generos = [g.nome for g in sistema.listar_generos()]
            listar_opcoes(generos)
            generos_indices = input("Escolha os gêneros (separados por vírgula): ").split(", ")
            generos_nomes = [generos[int(i)-1] for i in generos_indices]

            sistema.cadastrar_filme(nome, ano, plataforma_nome, generos_nomes)

        elif escolha == '2':
            print("\n" + "-"*50)
            print("          Cadastro de Novo Gênero")
            print("-"*50)
            id = input("Identificador do gênero: ")
            nome = input("Nome do gênero: ")
            sistema.cadastrar_genero(id, nome)

        elif escolha == '3':
            print("\n" + "-"*50)
            print("          Cadastro de Nova Plataforma")
            print("-"*50)
            id = input("Identificador da plataforma: ")
            nome = input("Nome da plataforma: ")
            sistema.cadastrar_plataforma(id, nome)

        elif escolha == '4':
            print("\n" + "-"*50)
            print("          Lista de Todos os Filmes")
            print("-"*50)
            filmes = sistema.listar_filmes()
            if filmes:
                for filme in filmes:
                    print(filme)
            else:
                print("Nenhum filme cadastrado.")
            input("\nPressione Enter para continuar...")

        elif escolha == '5':
            print("\n" + "-"*50)
            print("          Lista de Todos os Gêneros")
            print("-"*50)
            generos = sistema.listar_generos()
            if generos:
                for genero in generos:
                    print(genero)
            else:
                print("Nenhum gênero cadastrado.")
            input("\nPressione Enter para continuar...")

        elif escolha == '6':
            print("\n" + "-"*50)
            print("          Lista de Todas as Plataformas")
            print("-"*50)
            plataformas = sistema.listar_plataformas()
            if plataformas:
                for plataforma in plataformas:
                    print(plataforma)
            else:
                print("Nenhuma plataforma cadastrada.")
            input("\nPressione Enter para continuar...")

        elif escolha == '7':
            print("\n" + "-"*50)
            print("          Cadastro de Gêneros Preferidos")
            print("-"*50)
            genero = input("Digite o nome do gênero preferido: ")
            sistema.cadastrar_genero_preferido(genero)

        elif escolha == '8':
            print("\n" + "-"*50)
            print("          Recomendação de Filme")
            print("-"*50)
            filme_recomendado = sistema.recomendar_filme()
            if filme_recomendado:
                print(f"Filme recomendado: {filme_recomendado}")
            else:
                print("Nenhum filme disponível nos gêneros preferidos.")
            input("\nPressione Enter para continuar...")

        elif escolha == '9':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
