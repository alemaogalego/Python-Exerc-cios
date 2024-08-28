# Exercícios
# Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_big da classe Restaurante.
# Acesse o valor do atributo nome da instância restaurante_big da classe Restaurante.
# Verifique o valor inicial do atributo ativo para a instância restaurante_big e exiba uma mensagem informando se o restaurante está ativo ou inativo.
# Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
# Altere o valor do atributo nome para 'Bistrô'.
# Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
# Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
# Mude o estado da instância restaurante_pizza para ativo.
# Imprima no console o nome e a categoria da instância restaurante_big.

##############################################################################################################################################################
# Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_big da classe Restaurante.
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_big = Restaurante()
restaurante_big.nome = 'Big'
restaurante_big.categoria = 'Italiana'
# Acesse o valor do atributo nome da instância restaurante_big da classe Restaurante.
print(restaurante_big.nome)

# Verifique o valor inicial do atributo ativo para a instância restaurante_big e exiba uma mensagem informando se o restaurante está ativo ou inativo.
if restaurante_big.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')

# Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
categoria = Restaurante.categoria

# Altere o valor do atributo nome para 'Bistrô'.
restaurante_big.nome = 'Bistrô'

# Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

# Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')

# Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True

# Imprima no console o nome e a categoria da instância restaurante_big.
print(f'Restaurante : {restaurante_big.nome} categoria: {restaurante_big.categoria}!')

