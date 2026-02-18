class Lancamento:
    def __init__(self, Descricao, Categoria, Data, Valor, FormaDePagamento, **kwargs):

        self.Descricao = Descricao
        if self.Descricao == '':
            raise Exception('Descrição vazia')

        self.Data = Data
        if self.Data == '':
          raise Exception('Data vazia')

        self.Valor = Valor
        if self.Valor == '':
          raise Exception('Valor vazio')

        self.FormaDePagamento = FormaDePagamento
        if self.FormaDePagamento == '':
          raise Exception('Forma de Pagamento vazia')

        Lista_FormaDePagamento = ['dinheiro', 'débito', 'crédito', 'PIX', 'Dinheiro', 'Débito', 'Crédito', 'pix']
        if self.FormaDePagamento not in Lista_FormaDePagamento:
            raise Exception('Forma de Pagamento Inválida')

        self.Categoria = Categoria
        if self.Categoria == '':
            raise Exception('Categoria vazia')

        Lista_Categorias = {'receita': Receita, 'Receita': Receita, 'despesa': Despesa, 'Despesa': Despesa}
        if self.Categoria not in Lista_Categorias:
            raise Exception('Categoria inválida')

    def novo(self):
      print(f'Descrição: {self.Descricao}\nCategoria: {self.Categoria}\nData: {self.Data}\nValor: {self.Valor}\nForma de Pagamento: {self.FormaDePagamento}\n')
      print('Criado com sucesso')

class Receita(Lancamento):
    def __init__(self, Descricao, Categoria, Data, Valor, FormaDePagamento):
        super().__init__(Descricao, Categoria, Data, Valor, FormaDePagamento)

    def nova_receita(self):
      print(f'Descrição: {self.Descricao}\nCategoria: {self.Categoria}\nData: {self.Data}\nValor: {self.Valor}\nForma de Pagamento: {self.FormaDePagamento}\n')
      print(f'+{self.Valor} <{self.Descricao}>\n')
      print(f'Nova {self.Categoria} criada')

class Despesa(Lancamento):
    def __init__(self, Descricao, Categoria, Data, Valor, FormaDePagamento):
        super().__init__(Descricao, Categoria, Data, Valor, FormaDePagamento)
        self.Valor = float(self.Valor)
        if self.Valor > 500.00:
            print('Valor Alto')

    def nova_despesa(self):
      print(f'Descrição: {self.Descricao}\nCategoria: {self.Categoria}\nData: {self.Data}\nValor: {self.Valor}\nForma de Pagamento: {self.FormaDePagamento}\n')
      print(f'-{self.Valor} <{self.Descricao}>\n')
      print(f'Nova {self.Categoria} criada')


class Categoria_Receita(Receita):
    def __init__(self, nome, tipo, Descricao, limite_mensal, **kwards):
        
        self.tipo = super().__init__(categoria)
        lista_tipos = {'receita': Receita, 'Receita': Receita, 'despesa': Despesa, 'Despesa': Despesa}
        
        if self.Tipo == 'receita' or self.Tipo == 'Receita':
          self.limite_mensal = 0
          Receita().__init__(Descricao)
          self.nome = input(nome)

        elif self.Tipo == 'despesa' or self.Tipo == 'Despesa':
          self.limite_mensal = input(limite_mensal)
          Despesa().__init__(Descricao)
          self.nome = input(nome)

        else:
            raise Exception('Categoria inválida')

    def criar_e_exibir_categoria(self):
      print(f'-Categoria_{self.tipo}- \nNome: {self.nome}, \nTipo: {self.tipo}, \nDescrição: {self.descricao}')
       

    def adicionar_categoria(self):
        lista_despesa = []
        if self.nome in lista_despesa:
            print(f'Despesa {self.nome} já existe!')
        else:
            lista_despesa.append(f'Categoria_Despesa \nNome: {self.nome}, \nTipo: {self.tipo}, \nDescrição: {self.descricao}')
            print(f'Despesa {self.nome} Adicionada!')

    def editar_categoria(self, novo_nome, nova_descricao):
      pass

    def excluir_categoria(self):
      pass

class Categoria_Despesa(Despesa):
    def __init__(self, nome, tipo, Descricao, limite_mensal, **kwards):
        self.tipo = tipo
        self.tipo = super().__init__(categoria)
        lista_tipos = {'receita': Receita, 'Receita': Receita, 'despesa': Despesa, 'Despesa': Despesa}
        
        if self.Tipo == 'receita' or self.Tipo == 'Receita':
          self.limite_mensal = 0
          Receita().__init__(Descricao)
          self.nome = input(nome)

        elif self.Tipo == 'despesa' or self.Tipo == 'Despesa':
          self.limite_mensal = input(limite_mensal)
          Despesa().__init__(Descricao)
          self.nome = input(nome)

        else:
            raise Exception('Categoria inválida')

    def criar_e_exibir_categoria(self):
      print(f'-Categoria_{self.tipo}- \nNome: {self.nome}, \nTipo: {self.tipo}, \nDescrição: {self.descricao}')
       

    def adicionar_categoria(self):
        lista_despesa = []
        if self.nome in lista_despesa:
            print(f'Despesa {self.nome} já existe!')
        else:
            lista_despesa.append(f'Categoria_Despesa \nNome: {self.nome}, \nTipo: {self.tipo}, \nDescrição: {self.descricao}')
            print(f'Despesa {self.nome} Adicionada!')

    def editar_categoria(self, novo_nome, nova_descricao):
      pass

    def excluir_categoria(self):
      pass

lancamento1 = Lancamento('Salário ', 'Receita', '05/02 ', '2500 ', 'pix')
lancamento1.novo()

lancamento2 = Lancamento('Conta de Luz', 'Despesa', '05/02 ', '100 ', 'dinheiro')
lancamento2.novo()
