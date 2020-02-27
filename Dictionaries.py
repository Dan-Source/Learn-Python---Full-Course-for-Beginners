# Criando Dicionarios

monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "Octuber",
    "Nov": "November",
    "Dec": "December",
    10: "Voce também pode usar numeros como Chaves",
    
}

# Se voce quisar acessar um valor dentro do Dicionario
print(monthConversion["Nov"])
print(monthConversion["Dec"])
print(monthConversion["Jan"])

# Como o metodo get

print(monthConversion.get("Love", "Not a valid key"))