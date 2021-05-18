import re

print("Respeite a colocação dos parenteses e letras maiusculas")
a = str(input('informe a molecula do acido de Arrhenius: '))
b = str(input('informe a molecuça da base Arrhenius: '))


# noinspection PyUnreachableCode
class Molecula:
    def __init__(self, m_a, m_b):
        self.m_a = m_a
        self.m_b = m_b

    def text_num_split(self, atomo):
        for index, letter in enumerate(atomo, 0):
            if letter.isdigit():
                return [atomo[:index], atomo[index:]]

    def tratar_moleculas_dos_reagentes(self):

        global mol_h_a, mol_an, mol_an_2, mol_ca, mol_ca_2, mol_oh
        mt = Molecula.text_num_split

        # Mols dos atomos da molecula acida
        m_d_a = re.sub(r"([A-Z])", r" \1", self.m_a).split()

        # Se a molecula de acido tiver 2 atomos
        if len(m_d_a) == 2:

            # mol do hidrogenio
            if len(m_d_a[0]) == 1:
                mol_h_a = 1
            elif len(m_d_a[0]) == 2:
                mol_h_a = int(m_d_a[0][1])

            # mol dos anions
            m_d_a_1 = mt(self, m_d_a[1])
            if m_d_a_1 is None:
                mol_an = 1
            elif len(m_d_a_1) == 2:
                mol_an = int(m_d_a_1[1])

        # Se a molecula de acido tiver 3 atomos
        elif len(m_d_a) == 3:

            # mol do hidrogenio
            if len(m_d_a[0]) == 1:
                mol_h_a = 1
            elif len(m_d_a[0]) == 2:
                mol_h_a = int(m_d_a[0][1])

            # mol do anion 1
            m_d_a_1 = mt(m_d_a[1])
            if m_d_a_1 is None:
                mol_an = 1
            elif len(m_d_a_1) == 2:
                mol_an = int(m_d_a_1[1])

            # mol do anion 2
            m_d_a_2 = mt(m_d_a[2])
            if m_d_a_2 is None:
                mol_an_2 = 1
            elif len(m_d_a_2) == 2:
                mol_an_2 = int(m_d_a_2[1])

        # Mols dos atomos da molecula basica
        m_b_new = self.m_b.replace(")", "(")
        m_b_new_1 = m_b_new.replace("(", "", 2)
        m_d_b = re.sub(r'([A-Z])', r" \1", m_b_new_1).split()

        # Se a molecula basica tiver 3 atomos
        if len(m_d_b) == 3:

            # mol do cation
            m_d_b_0 = mt(self, m_d_b[0])
            if m_d_b_0 is None:
                mol_ca = 1
            elif len(m_d_b_0) == 2:
                mol_ca = int(m_d_b_0[1])

            # MOLS DA MOLECULA DE HIDROXILA
            if len(m_d_b[2]) == 1:
                mol_oh = 1
            elif len(m_d_b[2]) == 2:
                mol_oh = int(m_d_b[2][1])

        # Se a molecula basica tiver 4 atomos
        elif len(m_d_b) == 4:

            # mol do cation 1
            m_d_b_0 = mt(m_d_b[0])
            if m_d_b_0 is None:
                mol_ca = 1
            elif len(m_d_b_0) == 2:
                mol_ca = int(m_d_b_0[1])

            # mol do cation 2
            m_d_b_1 = mt(m_d_b[1])
            if m_d_b_1 is None:
                mol_ca_2 = 1
            elif len(m_d_b_1) == 2:
                mol_ca_2 = int(m_d_b_1[1])

            # MOLS DA MOLECULA DE HIDROXILA
            if len(m_d_b[2]) == 1:
                mol_oh = 1
            elif len(m_d_b[2]) == 2:
                mol_oh = int(m_d_b[2][1])

        lista = [m_d_a, mol_h_a, mol_an, mol_an_2, m_d_b, mol_ca, mol_ca_2, mol_oh]

        return lista

    def formacao_produtos(self):

        Molecula.tratar_moleculas_dos_reagentes(self)
        mtr = Molecula.tratar_moleculas_dos_reagentes

        m_d_a = mtr()[0]
        m_d_b = mtr()[4]

        # pegar o anion do acido
        m_d_a.reverse()
        an = m_d_a[:-1]
        if len(an) == 1:
            quant_an = 1
        else:
            quant_an = 2
        an.reverse()
        m_d_a.reverse()
        an_str = "".join(an)
        if quant_an == 2:
            an_str = "(" + an_str + ")"

        # pegar cation da base
        ca = m_d_b[:-2]
        if len(ca) == 1:
            quant_ca = 1
        else:
            quant_ca = 2
        ca_str = "".join(ca)
        if quant_ca == 2:
            ca_str = "(" + ca_str + ")"

        # formando sal e agua
        if mtr.mol_h_a == 1:
            ca_str = ca_str.replace(")", "(")
            ca_str = ca_str.replace("(", "")
        if mtr.mol_oh == 1:
            an_str = an_str.replace(")", "(")
            an_str = an_str.replace("(", "")
        sal = ca_str + str(mtr.mol_h_a) + an_str + str(mtr.mol_oh)
        sal = sal.replace("1", '')
        agua = "H2O"

        return sal, agua, an, ca, an_str, ca_str

    def artificio_balanciamento(self, localizacao, atomo):
        global mol_at
        for x in localizacao:
            if x == atomo:
                mol_at = 1
                break
            else:
                mol_at = 0
        return mol_at

    def balanciamento(self):
        mtr = Molecula.tratar_moleculas_dos_reagentes
        mf = Molecula.formacao_produtos
        ma = Molecula.artificio_balanciamento

        mol_ac = 1
        mol_ba = 1
        mol_sal = 1
        mol_ag = 1

        if len(mtr.m_d_a) == 2 and len(mtr.m_d_b) == 3:
            # obter os mols de hidrogenio no anion do acido e no cation da base
            mol_h_an = ma(mf.an, "H")
            mol_h_ca = ma(mf.ca, "H")

            # obter mols do oxigenio
            mol_o_an = ma(mf.an, "O")
            mol_o_ca = ma(mf.ca, "O")

            # obter mols do anion do acido no cation da base
            mol_an = ma(mf.ca, mf.an)  # ajeitar como descubrir o numero de mols

            # obter mols do cation da base no anon do acido
            mol_ca = ma(mf.an, mf.ca)

        elif len(mtr.m_d_a) == 2 and len(mtr.m_d_b) == 4:
            # obter os mols de hidrogenio no anion do acido e no cation da base
            mol_h_an = ma(mf.an, "H")
            mol_h_ca = ma(mf.ca, "H")

            # obter mols do oxigenio
            mol_o_an = ma(mf.an, "O")
            mol_o_ca = ma(mf.ca, "O")

            # obter mols do anion do acido no cation da base
            mol_an = ma(mf.ca, mf.an)  # ajeitar como descubrir o numero de mols

            # obter mols do cation da base no anon do acido
            mol_ca = ma(mf.an, mf.ca)

        elif len(mtr.m_d_a) == 3 and len(mtr.m_d_b) == 3:
            # obter os mols de hidrogenio no anion do acido e no cation da base
            mol_h_an = ma(mf.an, "H")
            mol_h_ca = ma(mf.ca, "H")

            # obter mols do oxigenio
            mol_o_an = ma(mf.an, "O")
            mol_o_ca = ma(mf.ca, "O")

            # obter mols do anion do acido no cation da base
            mol_an = ma(mf.ca, mf.an)  # ajeitar como descubrir o numero de mols

            # obter mols do cation da base no anon do acido
            mol_ca = ma(mf.an, mf.ca)

        elif len(mtr.m_d_a) == 3 and len(mtr.m_d_b) == 4:
            # obter os mols de hidrogenio no anion do acido e no cation da base
            mol_h_an = ma(mf.an, "H")
            mol_h_ca = ma(mf.ca, "H")

            # obter mols do oxigenio
            mol_o_an = ma(mf.an, "O")
            mol_o_ca = ma(mf.ca, "O")

            # obter mols do anion do acido no cation da base
            mol_an = ma(mf.ca, mf.an)  # ajeitar como descubrir o numero de mols

            # obter mols do cation da base no anon do acido
            mol_ca = ma(mf.an, mf.ca)

        return mol_ac, mol_ba, mol_sal, mol_ag

    def reacao_balanciada(self):
        mf = Molecula.formacao_produtos
        mb = Molecula.balanciamento

        Molecula.formacao_produtos(self)
        Molecula.balanciamento(self)

        reacao_balanciada = f'{mb.mol_ac + self.m_a} + {mb.mol_ba + self.m_b} -->' \
                            f' {mb.mol_sal + mf.sal} + {mb.mol_ag + mf.agua}'
        print('Reação balanciada: ' + reacao_balanciada)


exe = Molecula(a, b)
exe.reacao_balanciada()
