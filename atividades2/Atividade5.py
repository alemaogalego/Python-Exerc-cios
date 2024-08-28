# Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. 
# Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano.
# Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.


class Pessoa:
    def __init__(self, nome, idade, profissao) -> None:
        self.nome = nome.title()
        self.idade = idade
        self.profissao = profissao.title()

    def __str__(self) -> str:
        return f'{self.nome} | {self.idade} | {self.profissao}'

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá eu sou {self.nome}, e minha profissao é {self.profissao}'
        else:
            return f'Ola Sou, {self.nome} '
    def aniversario(self):
        self.idade += 1

pessoa1 = Pessoa('benzema', 18, 'jogador')
pessoa2 = Pessoa('joelma', 25, 'cuzinheira')

print(pessoa1)
print(pessoa2)
pessoa1.aniversario()
print('Pos aniversario: ')
print(pessoa1)
print(pessoa1.saudacao)
print(pessoa2)
print(pessoa2.saudacao)
