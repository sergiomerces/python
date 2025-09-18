# importar biblioteca matpltlib
import matplotlib.pyplot as plt

# base de dados
x = [1, 2, 3, 4 , 4]
y = [2, 4, 1,  3, 5]

# criar um gráfico de linha
plt.plot(x, y)

# adicionar rótulos aos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# adicionar um título ao gráfico
plt.title('Exemplo de Gráfico de Linha')

# mostrar o gráfico
plt.show()