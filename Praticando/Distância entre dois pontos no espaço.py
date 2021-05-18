# Pontos
p1 = [4, -8, -9]
p2 = [2, -3, -5]

# Criando listas para receber as subtrações e os quadrados
subtracao = []
quadrado = []

# Resolvendo as subtrações da eqauação
for i in range(0, len(p2)):
    subtracao.append(p2[i] - p1[i])

# Resolvendo os quadrados da equção
for i in range(0, len(subtracao)):
    quadrado.append(float(subtracao[i])**2)

# Efetuando a soma dos quadrados
soma_quadrados = sum(quadrado)

# Tirando a raiz da soma
raiz = soma_quadrados ** (1/2)

# Mostrando a distancia dos dois pontos no espaço
d = raiz
print(d)
