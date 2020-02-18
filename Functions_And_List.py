friends = ['Julia', 'Tailane', 'Karina']

lucky_numbers = [10, 20, 30, 40, 50, 60]

# permite a uniao das duas lista
friends.extend(lucky_numbers)
print(friends)

# permite adicionar um item no final da lista
friends.append("Joao")
print(friends)

# esta outra funcao recebe dois parametros 
friends.insert(1, "Clarencio")
print(friends)

# se eu quiser remover

friends.remove(20)
print(friends)

# todos o elementos
#friends.clear()
# print(friends)

# localizar um elemento na lista

print(friends.index('Julia'))

# para reordenar a lista utilizamos
lucky_numbers.sort()
print(lucky_numbers)


# para reverter a lista utilizamos
lucky_numbers.reverse()
print(lucky_numbers)

# para copiar uma lista
copylist = lucky_numbers.copy()
print(copylist)