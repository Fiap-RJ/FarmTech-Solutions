fazendas = []


def adicionar_fazenda(nome: str, area: float, comprimento, largura):
    fazendas.append({"nome": nome, "area": area, "comprimento": comprimento, "largura": largura})
    id_fazenda = len(fazendas) - 1
    print(
        f"Fazenda cadastrada com sucesso!\nID: {id_fazenda}\nNome: {nome}\nComprimento: {comprimento}\nLargura: {largura}\nÁrea: {area} m²"
    )


def obter_fazenda(id_fazenda: int):
    if 0 <= id_fazenda < len(fazendas):
        return fazendas[id_fazenda]
    print("Fazenda não encontrada.")
    return None


def listar_fazendas():
    if not fazendas:
        print("Nenhuma fazenda cadastrada.")
    else:
        print("Fazendas cadastradas:")
        for index, fazenda in enumerate(fazendas):
            print(f"[{index}] {fazenda['nome']}: {fazenda['area']} m²")


def remover_fazenda(id_fazenda: int):
    if 0 <= id_fazenda < len(fazendas):
        fazenda = fazendas.pop(id_fazenda)
        print(f"Fazenda {fazenda['nome']} removida com sucesso!")
    else:
        print("Fazenda não encontrada.")


def alterar_fazenda(id_fazenda: int, fazenda: dict):
    if 0 <= id_fazenda < len(fazendas):
        fazendas[id_fazenda] = fazenda
        print("Fazenda alterada com sucesso!")
    else:
        print("Fazenda não encontrada.")
