import re


def ca_an(molecula, numero, parte_da_molecula, parte_da_molecula2, parte_da_molecula1_1, parte_da_molecula2_1):
    if len(molecula) == numero:
        cation = parte_da_molecula
        anion = parte_da_molecula2
        cation_list = re.sub(r"([A-Z])", r" \1", cation).split()
        anion_list = re.sub(r"([A-Z])", r" \1", anion).split()
    elif len(molecula) == numero + 1:
        cation = parte_da_molecula1_1
        anion = parte_da_molecula2_1
        cation_list = re.sub(r"([A-Z])", r" \1", cation).split()
        anion_list = re.sub(r"([A-Z])", r" \1", anion).split()

    list = [cation, anion, cation_list, anion_list]
    return list


def text_num_split(atomo):
    for index, letter in enumerate(atomo, 0):
        if letter.isdigit():
            return [atomo[:index], atomo[index:]]


def artificio_balanciamento(localizacao, atomo):
    global mol_at
    for x in localizacao:
        if x == atomo:
            mol_at = 1
            break
        else:
            mol_at = 0
    return mol_at