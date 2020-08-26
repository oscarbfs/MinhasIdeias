# Equação de neutralização com acidos e bases de Arrhenius

mols = input('Informe o numero de mols da primeira molecula: ')
atomo0 = input('Informe o primeiro atomo da primeira molecula (todos diferentes de H ou OH considerere como se todos juntos fossem um atomo só): ')
atomo0_1 = input('Informe o segundo atomo da primeira molecula (todos diferentes de H ou OH considerere como se todos juntos fossem um atomo só): ')
mols1 = input('Informe o numero de mols da segunda molecula: ')
atomo1 = input('Informe o primeiro atomo da segunda molecula (todos diferentes de H ou OH considerere como se todos juntos fossem um atomo só): ')
atomo1_1 = input('Informe o segundo atomo da segunda molecula (todos diferentes de H ou OH considerere como se todos juntos fossem um atomo só): ')

estrutura = mols + atomo0 + atomo0_1
estrutura1 = mols1 + atomo1 + atomo1_1


class Molecula:

    def __init__(self, *tipo, tipo1=None, formula=estrutura, formula1=estrutura1):
        self.tipo = tipo
        self.tipo1 = tipo1
        self.formula = formula
        self.formula1 = formula1
        self.formula_pura = self.formula.replace(mols, '')
        self.formula_pura1 =  self.formula1.replace(mols1, '')

        if self.formula_pura.find('H') == 0:
            self.tipo = 'acido'
        elif self.formula_pura1.find('H') == 0:
            self.tipo1 = 'acido'
        else:
            raise Exception('Deve haver pelo menos um ácido!')

        if self.formula_pura.find('OH') != -1:
            self.tipo = 'base'
        elif self.formula_pura1.find('OH') != -1:
            self.tipo1 = 'base'
        else:
            raise Exception('Deve haver pelo menos uma base!')

    def balanciar(self):
        pass


    def reacao_quimica(self):

        if self.tipo == 'acido':
            newformula = self.formula_pura.replace('H', '')
        elif self.tipo == 'base':
            newformula1 = self.formula_pura.replace('OH', '')

        if self.tipo1 == 'acido':
            newformula = self.formula_pura1.replace('H', '')
        elif self.tipo1 == 'base':
            newformula1 = self.formula_pura1.replace('OH', '')

        sal = newformula1 + newformula
        reagentes = f'{self.formula} + {self.formula1}'
        produto = f'{sal} + H2O'

        if self.tipo == 'acido' and self.tipo1 == 'base' or self.tipo == 'base' and self.tipo1 == 'acido':
            print(f'Equação não balanciada da reação quimica: {reagentes} = {produto}')
            print(f'O sal formado foi: {sal}')

    def informar_o_tipo(self):
        if self == estrutura:
            return self.tipo
        elif self == estrutura1:
            return self.tipo1

estrutura = Molecula(formula=estrutura)
estrutura1 = Molecula(formula1=estrutura1)
print('A primeira molucela é um(a): ' + Molecula.informar_o_tipo(estrutura))
print('A segunda molucela é um(a): ' + Molecula.informar_o_tipo(estrutura1))
Molecula.reacao_quimica(estrutura)


#  H2SO4 + 2KOH  -> K2SO4 +2H2O
# 2HCN + Zn(OH)2 -> ZN(CN)2 + 2H2O