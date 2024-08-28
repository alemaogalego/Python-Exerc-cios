# Exercícios
# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.


# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de carro.
class Carro():
    carros = []
    def __init__(self, modelo='', cor='', ano=0):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'
    
    def listar_carro():
        for carro in Carro.carros:
            print(f'Modelos: {carro.modelo} | Cor: {carro.cor} | Ano: {carro.ano}')

uno = Carro('Quadrado', 'Preto', '1998')
gol = Carro('Bola', 'Vermelha', '2010')

Carro.listar_carro()

print('*'*50)
# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

class Restaurante():
    rest = []
    def __init__(self, nome='', categoria='', ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        Restaurante.rest.append(self)
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'
    
    def listar_rest():
        for rest in Restaurante.rest:
            print(f'nome: {rest.nome} | categoria: {rest.categoria} | Ativo: {rest.ativo}')

shufler = Restaurante('Shufler', 'Gourmet')
stars = Restaurante('Stars', 'Doce')

Restaurante.listar_rest()

print('*'*50)

# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Cliente:
    clientes = []
    def __init__(self, nome='', idade=0, email='', telefone=''):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        Cliente.clientes.append(self)
    def listar_clientes():
        for clientes in Cliente.clientes:
            print(f'nome: {clientes.nome} | idade: {clientes.idade} | email: {clientes.email} | telefone: {clientes.telefone}')

cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')

Cliente.listar_clientes()
