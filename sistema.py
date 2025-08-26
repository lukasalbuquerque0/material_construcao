class Config:
    __DESCONTO_PADRAO = 0.105  # 10,5%

    @staticmethod
    def get_desconto():
        return Config.__DESCONTO_PADRAO


desconto = Config.get_desconto()


materiais = [
    {
        "nome": "Cimento",
        "unidade": "saco (50kg)",
        "preco": 35.90,
        "estoque": 50
    },
    {
        "nome": "Tijolo",
        "unidade": "milheiro",
        "preco": 750.00,
        "estoque": 10
    },
    {
        "nome": "Areia",
        "unidade": "m³",
        "preco": 120.00,
        "estoque": 20
    }
]


def validar_string(valor):
    return isinstance(valor, str) and valor.strip() != ""


def validar_preco(valor):
    try:
        preco = float(valor)
        if preco > 0 and isinstance(preco, float):
            return preco
        else:
            return None
    except ValueError:
        return None


def validar_estoque(valor):
    try:
        estoque = int(valor)
        if estoque >= 0 and isinstance(estoque, int):
            return estoque
        else:
            return None
    except ValueError:
        return None


def cadastrar_material():
    print("\n=== Cadastro de Material ===")

    nome = input("Nome do material: ")
    while not validar_string(nome):
        print("Nome inválido. Tente novamente.")
        nome = input("Nome do material: ")

    unidade = input("Unidade do material (ex: m³, milheiro, quilo): ")
    while not validar_string(unidade):
        print("Unidade inválida. Tente novamente.")
        unidade = input("Unidade do material: ")

    preco = validar_preco(input("Preço do material (ex: 49.90): "))
    while preco is None:
        print("Preço inválido. Digite um valor numérico positivo.")
        preco = validar_preco(input("Preço do material: "))

    estoque = validar_estoque(input("Quantidade em estoque: "))
    while estoque is None:
        print("Quantidade inválida. Digite um número inteiro positivo ou zero.")
        estoque = validar_estoque(input("Quantidade em estoque: "))

    novo_material = {
        "nome": nome.strip(),
        "unidade": unidade.strip(),
        "preco": preco,
        "estoque": estoque
    }

    materiais.append(novo_material)
    print(f"\nMaterial '{nome}' cadastrado com sucesso!\n")


def listar_materiais():
    print("\n=== Lista de Materiais Cadastrados ===")

    if not materiais:
        print("Nenhum material cadastrado.\n")
        return

    for i, material in enumerate(materiais):
        print(f"[{i}] {material['nome']} - Unidade: {material['unidade']}")
        print(f"     Preço unitário: R${material['preco']:.2f}")
        print(f"     Estoque: {material['estoque']} unidades\n")


def realizar_venda():
    print("\n=== Venda de Material ===")

    if not materiais:
        print("Nenhum material cadastrado. Impossível realizar venda.\n")
        return

    listar_materiais()

    try:
        indice = int(input("Digite o índice do material que deseja comprar: "))
        if indice < 0 or indice >= len(materiais):
            print("Índice inválido.\n")
            return
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.\n")
        return

    material = materiais[indice]

    try:
        quantidade = int(input(f"Quantas unidades de '{material['nome']}' deseja comprar? "))
        if quantidade <= 0:
            print("Quantidade inválida. Digite um valor maior que zero.\n")
            return
        if quantidade > material["estoque"]:
            print(f"Estoque insuficiente. Só temos {material['estoque']} unidades disponíveis.\n")
            return
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.\n")
        return


    valor_bruto = material["preco"] * quantidade

    if valor_bruto > 100:
        valor_desconto = valor_bruto * Config.get_desconto()
        valor_final = valor_bruto - valor_desconto
        desconto_aplicado = True
    else:
        valor_desconto = 0
        valor_final = valor_bruto
        desconto_aplicado = False

    material["estoque"] -= quantidade

    print("\n=== Resumo da Venda ===")
    print(f"Material: {material['nome']} (Unidade: {material['unidade']})")
    print(f"Quantidade: {quantidade}")
    print(f"Valor unitário: R${material['preco']:.2f}")
    print(f"Valor bruto: R${valor_bruto:.2f}")
    if desconto_aplicado:
        print(f"Desconto aplicado ({Config.get_desconto()*100:.2f}%): -R${valor_desconto:.2f}")
    print(f"Valor final a pagar: R${valor_final:.2f}")
    print(f"Estoque restante: {material['estoque']} unidades\n")


def menu():
    while True:
        print("=== Sistema de Gerenciamento de Materiais de Construção ===")
        print("1. Cadastrar material")
        print("2. Listar materiais")
        print("3. Realizar venda")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_material()
        elif opcao == "2":
            listar_materiais()
        elif opcao == "3":
            realizar_venda()
        elif opcao == "0":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    menu()
