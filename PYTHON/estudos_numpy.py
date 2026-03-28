import numpy as np

array = array * 2

print(array)

print(type(array))


# Momento 2: DIMENSÕES
# 0 dimensões
array_0 = np.array("A")
print(array_0.ndim)

# 1 dimensão
array_1 = np.array(["A", "B", "C"])
print(array_1.ndim)


# 2 dimensões
array_2 = np.array([["A", "B", "C"],
                 ["D", "E", "F"], 
                 ["G", "H", "I"]])
print(array_2.ndim)

# 3 dimensões
array_3 = np.array([[["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
                    [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
                    [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", " "]]])
print(array_3.ndim)

print(array_3.shape)

# CHAIN INDEXING
# Letra A
print(array_3[0][0][0])
 # Letra N
print(array_3[1][1][1])
#Letra V
print(array_3[2][1][0])

# MULTIDIMENSIONAL INDEXING
print(array_3[0, 0 ,0])
 # Letra N
print(array_3[1, 1, 1])
#Letra V
print(array_3[2, 1, 0])

# Exercício concatenando
word = array_3[0, 0, 0] + array_3[2, 0, 0]+ array_3[2, 0, 1]
print(word)

# momento 3: SLICING
array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8],
                  [9, 10, 11, 12], 
                  [13, 14, 15, 16]])

# array[start:end:step] 
# o array[:, :] o primeiro espaço representa linha e o sgundo - após a virgula- a coluna
#linha
print(array[1:4])
print(array[0:4:2])
#negativo
print(array[::-1])
print(array[::-2])

#coluna
print(array[:, 3])
print(array[:,-1])
print(array[:, 1::2])
print(array[:, ::-2])

# os dois
print(array[0:2, 0:2])
print(array[0:2, 2:])
print(array[2:, 0:2])
print(array[2:, 2:])


# MOMENTO 4 : ARITHMETICS
# 
# #SCALAR ARITHMETIC

array = np.array([1, 2, 3])

#soma
print(array + 1)
#subtração
print(array - 2)
#multiplicação
print(array * 3)
#divisão
print(array / 4)
#potência
print(array ** 5)

# VECTORIZED MATH FUNCTIONS
array = np.array([1.01, 2.5, 3.99])

#raíz quadrada
print(np.sqrt(array))
#arrendondamento
print(np.round(array))
print(np.floor(array))
print(np.ceil(array))

#exercicio area de circulo
radii = np.array([1, 2, 3])
#formula area do circulo = pi vezes r ao quadrado
print(np.pi * radii ** 2)

# ELEMENTE-WISE ARITHMETIC

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

#soma
print(array1 + array2)
#subtração
print(array1 - array2)
#multiplicação
print(array1 * array2)
#divisão
print(array1 / array2)
#potência
print(array1 ** array2)

# COMPARISON OPERATORS

scores = np.array([91, 55, 100, 73, 82, 64])

print(scores == 100)
print(scores >= 60)
print(scores <= 60)

scores[scores <= 60] = 0
print(scores)


# MOMENTO 5: BROADCASTING
# tem que ser igual ou 1
array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)

# exemplo do jeito que não funciona

array3 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])

print(array3 * array2)

#versão do exemplo que funciona
array4 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

print(array4 * array2)

#exemplo 2

array1 = np.array([[1, 2, 3, 4, 5,6 , 7, 8, 9, 10]])
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)


# MOMENTO 6: AGGREGATE FUNCTIONS
array = np.array([[1, 2, 3, 4, 5], 
                  [ 6, 7, 8, 9, 10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.var(array))
print(np.min(array))
print(np.max(array))
print(np.argmin(array)) #retorna o indice do valor minimo
print(np.argmax(array)) #retorna o indice do valor máximo

print(np.sum(array, axis=0))  #soma as linhas
print(np.sum(array, axis=1))  # soma as colunas

# MOMENTO 7: FILTERING
ages = np.array([[21, 17,19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages < 18]
print(teenagers)

adults = ages[(ages >= 18) & (ages < 65)]
print(adults)

seniors = ages[ages >= 65]
print(seniors)

evens = ages[ages % 2 == 0]
print(evens)

odds = ages[ages % 2 != 0]
print(odds)

# teste
teste = ages[(ages < 18) | (ages >= 65)]
print(teste)

# Se quiser presevar o formato:
adults = np.where(ages >= 18, ages, 0)
print(adults)


# MOMENTO 8: RANDOM NUMBERS

rng = np.random.default_rng(seed=1)

print(rng.integers(low = 1, high = 101, size = (3, 2)))

np.random.seed(seed=1)
print(np.random.uniform(low =  -1, high = 1, size= 3))

rng = np.random.default_rng()
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)

fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])
fruits = rng.choice(fruits, size = (3, 2))
print(fruits)


