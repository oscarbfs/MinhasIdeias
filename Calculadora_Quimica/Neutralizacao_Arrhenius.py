import re

# definindo acido e base
print("Respeite a colocação dos parenteses e letras maiusculas")
acido = str(input('informe a molecula do acido de Arrhenius: '))
base = str(input('informe a molecuça da base Arrhenius: '))

# dividindo a molecula de acido
molecula_dividida_do_acido = re.sub(r"([A-Z])", r" \1", acido).split()

if len(molecula_dividida_do_acido) == 2:
    cation_do_acido = molecula_dividida_do_acido[0]
    anion_do_acido = molecula_dividida_do_acido[1]
elif len(molecula_dividida_do_acido) == 3:
    cation_do_acido = molecula_dividida_do_acido[0]
    anion_do_acido = molecula_dividida_do_acido[1] + molecula_dividida_do_acido[2]

# dividindo a molecula da basse
base = base.replace(")", "(")
base = base.replace("(", "", 2)
molecula_dividida_da_base = re.sub(r'([A-Z])', r" \1", base).split()

if len(molecula_dividida_da_base) == 3:
    cation_da_base = molecula_dividida_da_base[0]
    anion_da_base = molecula_dividida_da_base[1] + molecula_dividida_da_base[2]
elif len(molecula_dividida_da_base) == 4:
    cation_da_base = molecula_dividida_da_base[0] + molecula_dividida_da_base[1]
    anion_da_base = molecula_dividida_da_base[2] + molecula_dividida_da_base[3]


def text_num_split(self, atomo):
    for index, letter in enumerate(atomo, 0):
        if letter.isdigit():
            return [atomo[:index], atomo[index:]]


class Molecula:
    def __init__(self, cation, anion):
        self.cation = cation
        self.anion = anion

    def tratar_molecula(self):
        """ Contar a quantitidade de mols de cada atomo no anion e cation """
        pass


class Reacao:
    def __init__(self, molecula1, molecula2):
        self.acido = molecula1
        self.base = molecula2

    def formacao_dos_produtos(self):
        pass

    def balanciamneto(self):
        pass

    def reagir(self):
        pass


acido = Molecula(cation_do_acido, anion_do_acido)
base = Molecula(cation_da_base, anion_da_base)
reacao = Reacao(acido, base)
reacao.reagir()
