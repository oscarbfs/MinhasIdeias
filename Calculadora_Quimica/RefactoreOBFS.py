import re

print("Respeite a colocação dos parenteses e letras maiusculas")
a = input('informe a molecula do acido: ')
b = input('informe a molecuça da base: ')


class Molecula:
    def __init__(self, m_a, m_b):
        self.m_a = m_a
        self.m_b = m_b

    def text_num_split(self):
        for index, letter in enumerate(self, 0):
            if letter.isdigit():
                return [self[:index], self[index:]]

    def tratar_moleculas_dos_reagentes(self):

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
            m_d_a_1 = mt(m_d_a[1])
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
        m_d_b = re.sub(r"([A-Z])", r" \1", m_b_new_1).split()

        # Se a molecula basica tiver 3 atomos
        if len(m_d_b) == 3:

            # mol do cation
            m_d_b_0 = mt(m_d_b[0])
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

    def formacao_produtos(self):
        mtr = Molecula.tratar_moleculas_dos_reagentes

        # pegar o anion do acido
        mtr.m_d_a.reverse()
        an = mtr.m_d_a[:-1]
        if len(an) == 1:
            quant_an = 1
        else:
            quant_an = 2
        an.reverse()
        mtr.m_d_a.reverse()
        an = "".join(an)
        if quant_an == 2:
            an = "(" + an + ")"
        # pegar cation da base
        ca = mtr.m_d_b[:-2]
        if len(an) == 1:
            quant_ca = 1
        else:
            quant_ca = 2
        ca = "".join(ca)
        if quant_ca == 2:
            ca = "(" + ca + ")"
        # formando sal e agua
        if mtr.mol_h_a == 1:
            ca = ca.replace(")", "(")
            ca = ca.replace("(", "")
        if mtr.mol_oh == 1:
            an = an.replace(")", "(")
            an = an.replace("(", "")
        sal = ca + str(mtr.mol_h_a) + an + str(mtr.mol_oh)
        sal = sal.replace("1", '')
        agua = "H2O"


    def balanciamento(self):
        mtr = Molecula.tratar_moleculas_dos_reagentes

        mol_ac = 1
        mol_ba = 1
        mol_sal = 1
        mol_ag = 1

        for x in mtr.m_d_b:
            if x == mtr.m_d_a[1]:
                mol_an_ab = 'y' # usa oq fiz pra achar o mol o cl ou mg
                break
            else:
                mol_an_ab = 0

    def reacao_balanciada(self):
        pass


exe = Molecula(m_a=a, m_b=b)
Molecula.reacao_balanciada(exe)

