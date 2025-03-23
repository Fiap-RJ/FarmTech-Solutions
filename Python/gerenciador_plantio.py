from gerenciador_fazenda import alterar_fazenda

culturas = {
    "cana_de_acucar": {
        "l_s_ha": 0.099,  # l/s/ha (litros/segundo/hectare) # Agua necessária para a cultura de cana-de-açúcar
        "nitrogenio": 150,  # Nitrogênio necessário por hectare
        "fosforo": 45,  # Fósforo necessário por hectare
        "potassio": 115,  # Potássio necessário por hectare
    },
    "tomate": {
        "l_s_ha": 0.075,  # l/s/ha (litros/segundo/hectare) # Agua necessária para a cultura de tomate
        "nitrogenio": 125,  # Nitrogênio necessário por hectare
        "fosforo": 65,  # Fósforo necessário por hectare
        "potassio": 125,  # Potássio necessário por hectare
    },
}


def inserir_plantio(id_fazenda, fazenda):
    """
    Função que insere os dados de plantio de uma fazenda.
    """
    ruas = int(input("Número de ruas: "))
    tamanho_rua = float(input("Tamanho da rua (m): "))

    tamanho_das_ruas = ruas * tamanho_rua
    area_plantio = tamanho_das_ruas * fazenda["largura"]

    if (fazenda["comprimento"] > fazenda["largura"]):
        area_plantio = tamanho_das_ruas * fazenda["comprimento"]

    print(f'Comprimento da fazenda: {fazenda["comprimento"]} m\n'
          f'Largura da fazenda: {fazenda["largura"]} m\n'
          f'Número de ruas da plantação: {ruas}\n'
          f'Tamanho da rua da plantação: {tamanho_rua} m\n'
          f'Área de plantio: {area_plantio} m²')

    print("Selecione a cultura plantada:")
    print("1. Cana-de-açúcar")
    print("2. Tomate")

    opcao = input("Opção: ")

    if opcao == "1":
        cultura = "cana_de_acucar"
    elif opcao == "2":
        cultura = "tomate"
    else:
        print("Opção inválida!")
        return

    dados_cultura = culturas[cultura]

    plantio = {
        "cultura": cultura,
        "area_plantio": area_plantio,
        "quantidade_ruas": ruas,
        "tamanho_rua": tamanho_rua,
        "agua_necessaria": dados_cultura["l_s_ha"] * area_plantio,
        "nitrogenio_necessario": dados_cultura["nitrogenio"] * area_plantio,
        "fosforo_necessario": dados_cultura["fosforo"] * area_plantio,
        "potassio_necessario": dados_cultura["potassio"] * area_plantio,
    }

    fazenda["plantio"] = plantio
    alterar_fazenda(id_fazenda, fazenda)
    print(f"Dados de plantio inseridos com sucesso! \n {plantio}")


def exibir_plantio(fazenda):
    """
    Função que exibe os dados de plantio de uma fazenda.
    """
    plantio = fazenda.get("plantio")
    if not plantio:
        print("\nNenhum dado de plantio encontrado.")
    else:
        print("\nDados de plantio:")
        print(f"Cultura: {plantio['cultura']}")
        print(f"Quantidade de ruas: {plantio['quantidade_ruas']}")
        print(f"Tamanho da rua: {plantio['tamanho_rua']} m")
        print(f"Área de plantio: {plantio['area_plantio']} m²")
        print(f"Água necessária: {plantio['agua_necessaria']} litros/segundos")
        print(f"Nitrogênio necessário: {plantio['nitrogenio_necessario']} kg")
        print(f"Fósforo necessário: {plantio['fosforo_necessario']} kg")
        print(f"Potássio necessário: {plantio['potassio_necessario']} kg")

    print("-" * 30 + "\n")
    input("Pressione Enter para continuar...")


def alterar_plantio(id_fazenda, fazenda):
    print("Selecione o que deseja alterar:")
    print("1. Número de ruas")
    print("2. Tamanho da rua")
    print("3. Cultura plantada")

    opcao = input("Opção: ")

    if opcao == "1":
        ruas = int(input("Novo número de ruas: "))
        area_total = fazenda["area"]
        tamanho_rua = fazenda["plantio"]["tamanho_rua"]
        nova_area_plantio = area_total - (ruas * tamanho_rua)
        fazenda["plantio"]["quantidade_ruas"] = ruas
        fazenda["plantio"]["area_plantio"] = nova_area_plantio
        alterar_fazenda(id_fazenda, fazenda)

    elif opcao == "2":
        tamanho_rua = float(input("Novo tamanho da rua (m): "))
        area_total = fazenda["area"]
        ruas = fazenda["plantio"]["quantidade_ruas"]
        nova_area_plantio = area_total - (ruas * tamanho_rua)
        fazenda["plantio"]["tamanho_rua"] = tamanho_rua
        fazenda["plantio"]["area_plantio"] = nova_area_plantio
        alterar_fazenda(id_fazenda, fazenda)

    elif opcao == "3":
        print("Selecione a nova cultura plantada:")
        print("1. Cana-de-açúcar")
        print("2. Tomate")

        opcao = input("Opção: ")

        if opcao == "1":
            cultura = "cana_de_acucar"
        elif opcao == "2":
            cultura = "tomate"
        else:
            print("Opção inválida!")
            return

        dados_cultura = culturas[cultura]

        area_plantio = fazenda["plantio"]["area_plantio"]

        fazenda["plantio"]["cultura"] = cultura
        fazenda["plantio"]["agua_necessaria"] = dados_cultura["l_s_ha"] * area_plantio
        fazenda["plantio"]["nitrogenio_necessario"] = (
            dados_cultura["nitrogenio"] * area_plantio
        )
        fazenda["plantio"]["fosforo_necessario"] = (
            dados_cultura["fosforo"] * area_plantio
        )
        fazenda["plantio"]["potassio_necessario"] = (
            dados_cultura["potassio"] * area_plantio
        )
        alterar_fazenda(id_fazenda, fazenda)


def remover_plantio(id_fazenda, fazenda):
    fazenda["plantio"] = {}
    alterar_fazenda(id_fazenda, fazenda)
    print("Dados de plantio removidos com sucesso!")
