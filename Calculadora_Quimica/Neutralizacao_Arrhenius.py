from Calculadora_Quimica import funcoes

ft = funcoes.text_num_split
fca = funcoes.ca_an
frs = funcoes.re_split

# definindo acido e base
print("Respeite a colocação dos parenteses e letras maiusculas")
acido = str(input('informe a molecula do acido de Arrhenius: '))
base = str(input('informe a molecuça da base Arrhenius: '))

# dividindo a molecula de acido
molecula_dividida_do_acido = frs(acido)  # re.sub(r"([A-Z])", r" \1", acido).split()

ca_an_do_acido = fca(
    molecula_dividida_do_acido, 2, molecula_dividida_do_acido[0],
    molecula_dividida_do_acido[1],
    molecula_dividida_do_acido[0],
    molecula_dividida_do_acido[1] + molecula_dividida_do_acido[2]
)

cation_do_acido = ca_an_do_acido[0]
anion_do_acido = ca_an_do_acido[1]
cation_do_acido_num_split = ft(ca_an_do_acido[2])
anion_do_acido_num_split = ft(ca_an_do_acido[3])

# dividindo a molecula da basse
base = base.replace(")", "(")
base = base.replace("(", "", 2)
molecula_dividida_da_base = frs(base)  # re.sub(r'([A-Z])', r" \1", base).split()

ca_an_do_base = fca(
    molecula_dividida_da_base, 3, molecula_dividida_da_base[0],
    molecula_dividida_da_base[1] + molecula_dividida_da_base[2],
    molecula_dividida_da_base[0] + molecula_dividida_da_base[1],
    molecula_dividida_da_base[2] + molecula_dividida_da_base[3]
)

cation_da_base = ca_an_do_acido[0]
anion_da_base = ca_an_do_acido[1]
cation_da_base_num_split = ft(ca_an_do_base[2])
anion_da_base_num_split = ft(ca_an_do_base[3])


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
