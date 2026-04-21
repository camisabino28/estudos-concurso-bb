import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Gráfico 1
# x = np.array([2023, 2024, 2025, 2026])
# y1 = np.array([15, 25, 30, 20])
# y2 = np.array([17, 23, 38, 5])
# y3 = np.array([13, 15, 20, 30])

# line_style = dict(marker=".",
#                markersize=30,
#                markerfacecolor = "#1cd3fc",
#                markeredgecolor = "#1cd3fc",
#                linestyle="solid",
#                linewidth=4)

# marker = "" -> . = ponto; o = circulo, v = triangulo, * = *, etc
#linestyle -> dashed = tracejada, dotted = pontilhada, dashdot = combinação dos dois, none = sem linha, solid = solida
# plt.title("Class size", fontsize=25,
#                         family="Arial",
#                         fontweight="bold",
#                         color="#2d4cfc")
# plt.xlabel("Year", fontsize=20,
#                    family="Arial",
#                    fontweight="bold",
#                    color="#2dbefc")
# plt.ylabel("Students", fontsize=20,
#                    family="Arial",
#                    fontweight="bold",
#                    color="#2dbefc")

# plt.tick_params(axis="both", #x, y ou os dois (both)
#                 colors="#2dbefc")
# plt.plot(x, y1,color="#1c5bfc", **line_style)
# plt.plot(x, y2,color="#1cfc45", **line_style)
# plt.plot(x, y3,color="#fc1c1c", **line_style)

# plt.xticks(x)

# plt.show()

# Gráfico 2 - Grid
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([5, 10, 15, 20, 25])

# plt.grid(axis="y",
#          linewidth=2,
#          color="lightgray",
#          linestyle="dashed")

# plt.plot(x, y)
# plt.show()

# Gráfico 3 - Barras
# categories = np.array(["Grains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweets"])
# values = np.array([4, 3, 2, 5, 3, 1])

# # Barras verticais
# plt.bar(categories, values, color="skyblue")

# # Barras horizontais
# #plt.barh(categories, values, color="skyblue")

# plt.title("Daily Consumption")
# plt.xlabel("Food")
# plt.ylabel("Quantity")
# plt.show()

# Gráfico 4 - Pizza
# categories = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
# values = np.array([300, 250, 275, 225])
# colors = ["red", "yellow", "blue", "green"]

# plt.pie(values, labels=categories,
#                 autopct="%1.1f%%",
#                 colors=colors,
#                 explode=[0, 0, 0, 0.1], # separa uma fatia)
#                 shadow=True,
#                 startangle=90)

# plt.title("X College")

# plt.show()

# Gráfico 5 - Correlação
# x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8]) # Hours studied
# y1 = np.array([55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87]) # Grades

# x2 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8]) # Hours studied
# y2 = np.array([50, 58, 65, 70, 72, 78, 83, 88, 92, 95, 97]) # Grades

# plt.scatter(x1, y1, color="skyblue",
#                     alpha=0.5, #transparencia das bolas
#                     s= 200,  # tamanho da bola
#                     label="Class A")

# plt.scatter(x2, y2, color="red",
#                   alpha=0.5, #transparencia das bolas
#                   s= 200,  # tamanho da bola
#                   label="Class B")

# plt.title("Test Scores")
# plt.xlabel("Hours Studied")
# plt.ylabel("Grade")
# plt.legend()

# plt.show()

# Gráfico 6 - Histogramas
# scores = np.random.normal(loc=80, scale=20, size=100)
# scores = np.clip(scores, 0, 100) # basicamente valores minimo e maximo

# plt.hist(scores, bins=10,
#                 color="lightgreen",
#                 edgecolor="black")
# plt.title("Exam Scores")
# plt.xlabel("Score")
# plt.ylabel("Number of Students")
# plt.show()

# Gráfico 7 - Subplots
# Ax = um plot

# x = np.array([1, 2, 3, 4, 5])

# figure, axes = plt.subplots(2,2) #linha e coluna

# axes[0, 0].bar(x, x*2, color = "red")
# axes[0, 0].set_title("x*2")

# axes[0, 1].plot(x, x**2, color = "blue")
# axes[0, 1].set_title("x**2")

# axes[1, 0].plot(x, x**3, color="green")
# axes[1, 0].set_title("x**3")

# axes[1, 1].plot(x, x**4, color="purple")
# axes[1, 1].set_title("x**4")

# plt.tight_layout()
# plt.show()

# Gráfico 8

df = pd.read_csv(r"C:\Users\camis\OneDrive\Anexos de email\Área de Trabalho\ESTUDOS PROGRAMAÇÃO\PYTHON\DATA\No,Name,Type1,Type2,Height,Weight,L.csv")

type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values, color="darkred",
                                              edgecolor="black")

plt.title("Number of Pokemon by Primary Type")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()
plt.show()

