import re


def re_split(particula):
    re.sub(r"([A-Z])", r" \1", particula).split()


def ca_an(molecula, numero, parte_da_molecula, parte_da_molecula2):
    if len(molecula) == numero:
        cation = str(parte_da_molecula)
        anion = str(parte_da_molecula2)
        cation_list = re.sub(r"([A-Z])", r" \1", cation).split()
        anion_list = re.sub(r"([A-Z])", r" \1", anion).split()
    elif len(molecula) == numero + 1:
        cation = str(parte_da_molecula)
        anion = str(parte_da_molecula2)
        cation_list = re.sub(r"([A-Z])", r" \1", cation).split()
        anion_list = re.sub(r"([A-Z])", r" \1", anion).split()

    list = [cation, anion, cation_list, anion_list]
    return list


def text_num_split(atomo):
    for index, letter in enumerate(atomo, 0):
        if letter.isdigit():
            return [atomo[:index], atomo[index:]]


def artificio_tratar_molecula(atomo):
    for mol in atomo:
        if not mol.isalpha():
            mol_do_atomo = int(mol)
    return mol_do_atomo


def artificio_balanciamento(localizacao, atomo):
    for x in localizacao:
        if x == atomo:
            mol_at = 1
            break
        else:
            mol_at = 0
    return mol_at
