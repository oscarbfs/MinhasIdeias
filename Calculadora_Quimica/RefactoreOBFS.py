MO_MA = int(input('mols da molecula do acido: '))  # mols da molecula acida
MO_H = int(input('mols do hirigenio: '))  # mols o hidrogenio
A = input('molecula do acido: ')
MO_A = int(input('mols do atomo do acido: '))  # mols do atomo do  acido

MO_MB = int(input('mols a molecula da base: '))  # mols a molecula basica
MO_OH = int(input('mols do hidroxila: '))  # mols da hidroxila
B = input('molecula da base: ')
MO_B = int(input('mols do atomo da base: '))  # mols do atomo da base


class Reacao:
    def __init__(self, AC, BA):
        self.AC = AC
        self.BA = BA
        self.Hidrog = 'H'
        self.Hidrox = 'OH'
        self.M_A = str(MO_MA) + self.Hidrog + str(MO_H) + self.AC + str(MO_A)
        self.M_B = str(MO_MB) + self.BA + str(MO_B) + self.Hidrox + str(MO_OH)

    def balanciar(self):
        # 2HCL + MGOH2 --> MG1CL2 + 2H2O
        # HCL + MGOH2 --> MGCL2 + H2O

        C_S = self.BA + str(MO_H)
        A_S = self.AC + str(MO_OH)
        self.M_S = C_S + A_S

        N_H = (MO_MA * MO_H) + (MO_MB * MO_OH)
        M_AG = int(N_H / 2)
        self.AGUA = str(M_AG) + 'H2O'

    def reagir(self):
        Reacao.balanciar(self)
        M_A = self.M_A.replace('1', '')
        M_B = self.M_B.replace('1', '')
        M_S = self.M_S.replace('1', '')
        AGUA = self.AGUA.replace('1', '')

        reagentes = f'{M_A} + {M_B}'
        produtos = f'{M_S} + {AGUA}'

        print(reagentes + ' --> ' + produtos)


X = Reacao(AC=A, BA=B)
X.reagir()