# 2d list

number_grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# como acessar um valor dentro de uma grade de numeros

print(number_grid[0][0])

# acessando os valores com loops aninhados

for row in number_grid:
    for col in row:
        print(col)