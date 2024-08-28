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

usuario_modelos = input('Digite seu modelo: ')
usuario_cor = input('Digite sua cor: ')
usuario_ano = input('Digite o ano: ')

if usuario_ano.isdigit():
    usuario_int = int(usuario_ano)
else:
    print("Número inválido!")


uno = Carro(usuario_modelos, usuario_cor, usuario_int)
gol = Carro('Bola', 'Vermelha', '2010')

Carro.listar_carro()