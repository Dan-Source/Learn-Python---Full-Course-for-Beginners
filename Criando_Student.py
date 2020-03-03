# Importando o Objetos que Criamos
from Classes_and_Objetos import Student

# Estamos criando objetos diferentes
student1 = Student("Daniel", "ADS", 8.7, False)
student2 = Student("Julia", "ADS", 9.7, False)
student3 = Student("Thailane", "ADS", 10, False)
student4 = Student("Karina", "ADS", 8.7, False)

# Acessando as informações contidas no objetos
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

# Comparando um valor dentro da classe Student

print(student1.on_honor_hall())
print(student2.on_honor_hall())
print(student3.on_honor_hall())
print(student4.on_honor_hall())