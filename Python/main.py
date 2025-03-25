from gerenciador_fazenda import (
    remover_fazenda,
    adicionar_fazenda,
    listar_fazendas,
    obter_fazenda,
    alterar_fazenda,
)
from gerenciador_plantio import (
    inserir_plantio,
    exibir_plantio,
    alterar_plantio,
    remover_plantio,
)


def menu_principal():
    """
    Função que exibe o menu principal do programa.
    O usuário pode escolher entre as opções de cadastrar uma fazenda, gerenciar uma fazenda ou sair do programa.
    """
    while True:
        print("\n=== Menu Principal ===")
        print("1. Cadastrar Fazenda")
        print("2. Gerenciar Fazenda")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            nome = input("Nome da fazenda: ")
            largura = float(input("Largura do terreno (m): "))
            comprimento = float(input("Comprimento do terreno (m): "))
            area = largura * comprimento
            adicionar_fazenda(nome, area, largura, comprimento)
        elif escolha == "2":
            gerenciar_fazenda()
        elif escolha == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")


def gerenciar_fazenda():
    """
    Função que exibe o menu de gerenciamento de fazendas.
    O usuário pode escolher entre visualizar a fazenda, remover a fazenda ou voltar ao menu principal.
    """
    while True:
        print("\n=== Gerenciar fazenda ===")
        listar_fazendas()
        id_fazenda = input(
            "Informe o identificador da fazenda (ou digite 'voltar' para retornar): "
        )
        if id_fazenda.lower() == "voltar":
            return
        id_fazenda = int(id_fazenda)
        fazenda = obter_fazenda(id_fazenda)
        if not fazenda:
            print("fazenda não encontrada.")
            continue

        while True:
            print("\n=== Opções de Gerenciamento ===")
            print("1. Alterar nome da Fazenda")
            print("2. Alterar área da Fazenda")
            print("3. Inserir dados de plantio")
            print("4. Exibir dados de plantio")
            print("5. Alterar dados de plantio")
            print("6. Remover dados de plantio")
            print("7. Remover Fazenda")
            print("0. Voltar")

            escolha = input("Escolha uma opção: ")
            if escolha == "1":
                fazenda["nome"] = input("Novo nome da fazenda: ")
                alterar_fazenda(id_fazenda, fazenda)
                print("Nome da fazenda alterado com sucesso!")
            elif escolha == "2":
                largura = float(input("Nova largura do terreno (m): "))
                comprimento = float(input("Novo comprimento do terreno (m): "))
                fazenda["comprimento"] = comprimento
                fazenda["largura"] = largura
                fazenda["area"] = largura * comprimento
                alterar_fazenda(id_fazenda, fazenda)
                print("Fazenda alterada com sucesso!")

                remover_plantio(id_fazenda, fazenda)
                print("\nAgora, insira os dados de plantio da fazenda.")
                inserir_plantio(id_fazenda, fazenda)
                return
            elif escolha == "3":
                inserir_plantio(id_fazenda, fazenda)
            elif escolha == "4":
                exibir_plantio(fazenda)
            elif escolha == "5":
                alterar_plantio(id_fazenda, fazenda)
            elif escolha == "6":
                remover_plantio(id_fazenda, fazenda)
                print("Dados de plantio removidos com sucesso!")
            elif escolha == "7":
                remover_fazenda(id_fazenda)
                print("Fazenda removida com sucesso!")
                return
            elif escolha == "0":
                break
            else:
                print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu_principal()
