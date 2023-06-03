class Acao:
    def __init__(self, codigo, nome, preco_atual, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco_atual = preco_atual
        self.quantidade = quantidade

    def atualizar_preco(self, novo_preco):
        self.preco_atual = novo_preco

    def calcular_valor_total(self):
        return self.preco_atual * self.quantidade


# Criar algumas ações de exemplo
acao1 = Acao("AAPL", "Apple Inc.", 135.50, 10)
acao2 = Acao("GOOGL", "Alphabet Inc.", 2500.75, 5)
acao3 = Acao("MSFT", "Microsoft Corporation", 300.00, 8)

# Atualizar o preço de uma ação
acao1.atualizar_preco(140.25)

# Calcular o valor total de uma ação
valor_total_acao2 = acao2.calcular_valor_total()

# Imprimir informações das ações
print(f"Ação 1: {acao1.nome} ({acao1.codigo}), Preço: {acao1.preco_atual}, Quantidade: {acao1.quantidade}")
print(f"Ação 2: {acao2.nome} ({acao2.codigo}), Preço: {acao2.preco_atual}, Quantidade: {acao2.quantidade}")
print(f"Ação 3: {acao3.nome} ({acao3.codigo}), Preço: {acao3.preco_atual}, Quantidade: {acao3.quantidade}")
print(f"Valor total da Ação 2: {valor_total_acao2}")
