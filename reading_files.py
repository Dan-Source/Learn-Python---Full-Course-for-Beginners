
# abrindo o arquivo
file = open("file.txt", "r")
# verifiando se o arquivo e legivel
print(file.readable())
# inserindo o aquivo em uma lista
print(file.readlines())

# lendo o arquivo
print(file.read())
# lendo o arquivo por linhas
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())


# fechando o arquivo
file.close()

