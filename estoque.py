def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco_texto = input("Digite o preço do produto: ")
    preco = float(preco_texto.replace(",", "."))
    quantidade = int(input("Digite a quantidade do produto: "))
    produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
    produtos.append(produto)
    print(f"Produto '{nome}' cadastrado com sucesso!")

def listar_produtos():
    print("\n=== Produtos em Estoque ===")
    for produto in produtos:
        print(f"{produto['nome']} - R${produto['preco']:.2f} - Qtd: {produto['quantidade']}")

def registrar_entrada():
    nome_busca = input("Digite o nome do produto que recebeu reposição: ").strip()
    for produto in produtos:
        if produto["nome"].strip().lower() == nome_busca.lower():
            try:
                quantidade_entrada = int(input("Quantidade recebida: "))
                produto["quantidade"] = produto["quantidade"] + quantidade_entrada
                print(f"Estoque atualizado! {produto['nome']} agora tem {produto['quantidade']} unidades.")
            except ValueError:
                print("Quantidade inválida! Digite apenas números.")
            return
    print("Produto não encontrado. Cadastre-o primeiro.")

def comprar_produto():
    total_compra = 0
    comprando = True

    while comprando:
        nome_busca = input("\nDigite o nome do produto (ou 'fim' para finalizar): ").strip()
        if nome_busca.lower() == "fim":
            comprando = False
        else:
            encontrado = False
            for produto in produtos:
                if produto["nome"].strip().lower() == nome_busca.lower():
                    encontrado = True
                    try:
                        quantidade_desejada = int(input("Quantidade: "))
                        if quantidade_desejada <= produto["quantidade"]:
                            produto["quantidade"] = produto["quantidade"] - quantidade_desejada
                            subtotal = produto["preco"] * quantidade_desejada
                            total_compra = total_compra + subtotal
                            print(f"Adicionado: {quantidade_desejada}x {produto['nome']} - Subtotal: R${subtotal:.2f}")
                        else:
                            print("Estoque insuficiente para essa quantidade.")
                    except ValueError:
                        print("Quantidade inválida! Digite apenas números.")
            if not encontrado:
                print("Produto não encontrado.")

    print(f"\n=== Total da compra: R${total_compra:.2f} ===")

produtos = []
continuar = True

while continuar:
    print("\n=== Sistema de Loja ===")
    print("1. Cadastrar Produto")
    print("2. Ver Estoque")
    print("3. Comprar (Saída)")
    print("4. Registrar Entrada")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        comprar_produto()
    elif opcao == "4":
        registrar_entrada()
    elif opcao == "5":
        print("Saindo do sistema...")
        continuar = False
    else:
        print("Opção inválida")