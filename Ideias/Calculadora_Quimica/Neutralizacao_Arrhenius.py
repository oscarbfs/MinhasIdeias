from Calculadora_Quimica import funcoes
import re

ft = funcoes.text_num_split
fca = funcoes.ca_an
frs = funcoes.re_split
fatm = funcoes.artificio_tratar_molecula

# definindo acido e base
print("Respeite a colocação dos parenteses e letras maiusculas")
acido = str(input('informe a molecula do acido de Arrhenius: '))
base = str(input('informe a molecuça da base Arrhenius: '))

# dividindo a molecula de acido
molecula_dividida_do_acido = re.sub(r"([A-Z])", r" \1", acido).split()

if len(molecula_dividida_do_acido) == 2:
    ca_an_do_acido = fca(
        molecula_dividida_do_acido, 2, molecula_dividida_do_acido[0],
        molecula_dividida_do_acido[1],
    )
elif len(molecula_dividida_do_acido) == 3:
    ca_an_do_acido = fca(
        molecula_dividida_do_acido, 2,
        molecula_dividida_do_acido[0],
        molecula_dividida_do_acido[1] + molecula_dividida_do_acido[2]
    )

cation_do_acido = ca_an_do_acido[0]
anion_do_acido = ca_an_do_acido[1]

cation_do_acido_list = ca_an_do_acido[2]
anion_do_acido_list = ca_an_do_acido[3]

cation_do_acido_num_split = ft(cation_do_acido)
anion_do_acido_num_split = ft(anion_do_acido)

# dividindo a molecula da basse
base = base.replace(")", "(")
base = base.replace("(", "", 2)
molecula_dividida_da_base = re.sub(r'([A-Z])', r" \1", base).split()

if len(molecula_dividida_do_acido) == 2:
    ca_an_da_base = fca(
        molecula_dividida_da_base, 3, molecula_dividida_da_base[0],
        molecula_dividida_da_base[1] + molecula_dividida_da_base[2],
    )
elif len(molecula_dividida_do_acido) == 3:
    ca_an_da_base = fca(
        molecula_dividida_da_base, 3,
        molecula_dividida_da_base[0] + molecula_dividida_da_base[1],
        molecula_dividida_da_base[2] + molecula_dividida_da_base[3]
    )

cation_da_base = ca_an_do_acido[0]
anion_da_base = ca_an_do_acido[1]

cation_da_base_list = ca_an_da_base[2]
anion_da_base_list = ca_an_da_base[3]

cation_da_base_num_split = ft(cation_da_base)
anion_da_base_num_split = ft(anion_da_base)


class Molecula:
    def __init__(self, cation, anion, cation_list, anion_list, cation_num_split, anion_num_split):
        self.cation = cation
        self.anion = anion
        self.cation_list = cation_list
        self.anion_list = anion_list
        self.cation_num_split = cation_num_split
        self.anion_num_split = anion_num_split

    def tratar_molecula(self):
        """ Contar a quantitidade de mols de cada atomo no anion e cation """
        mol_do_cation = fatm(self.cation_num_split)
        mol_do_anion = fatm(self.anion_num_split)
        list_mol = [mol_do_cation, mol_do_anion]
        return list_mol


class Reacao:
    def __init__(self, molecula1, molecula2):
        self.acido = molecula1
        self.base = molecula2

    def formacao_dos_produtos(self):
        sal = self.base.cation + self.acido.anion
        agua = "H2O"
        produtos = f"{sal} + {agua}"
        return produtos

    def balanciameto(self):
        pass

    def reagir(self):
        produtos = self.formacao_dos_produtos()
        reagentes = f'{self.acido} + {self.base}'
        equacao = f'{reagentes} --> {produtos}'
        print(equacao)
        print(reagentes)


acido = Molecula(
    cation_do_acido, anion_do_acido,
    cation_do_acido_list, anion_do_acido_list,
    cation_do_acido_num_split, anion_do_acido_num_split
)
base = Molecula(
    cation_da_base, anion_da_base,
    cation_da_base_list, anion_da_base_list,
    cation_da_base_num_split, anion_da_base_num_split
)
reacao = Reacao(acido, base)
reacao.reagir()
