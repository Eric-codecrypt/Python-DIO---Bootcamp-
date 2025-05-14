from inspect import Traceback

print("BOOTCAMP - DIO(Python Developer)")

print("-----------------------------------------------------------------------------")
print("Primeira aula")

print("___")

print("built-in {")

print("types:")

print("text -> str.")
print("Number -> int, float, complex.")
print("Sequence -> list, tuple, range.")
print("Map -> dict")
print("Collection -> set, frozenset.")
print("Boolean -> bool.")
print("Binary -> bytes, bytearray, memoryview.")

print("}")

print("-----------------------------------------------------------------------------")

print("types of data:")

print("11 + 10 + 1000")

print(1.5 + 1 + 0.5)

print(True)

print(False)

print("Python")

print("-----------------------------------------------------------------------------")
print("Segunda aula")

print("-terminal interativo-")

print("dir(), dir(100)")
print("help(), help(100)")

print("-----------------------------------------------------------------------------")
print("Terceira aula")

print("-Variáveis-")

age = 23
name = 'Guilherme'
print(f'Meu nome é {name} e tenho {age} anos(s) de idade.')

age, name = (23, 'Guilherme')
print(f'Meu nome é {name} e tenho {age} anos(s) de idade.')

print("-Constantes-")

ABS_PATH = 'C:/Users/Turma 2/PyCharmMiscProject/'
DEBUG = True
STATES = [
    'SP',
    'RJ',
    'MG',
]
AMOUNT = 30.2


print("test_variable__>")

nome = "Guilherme"
idade = 28

nome, idade = ("Giovanna", 27)

print(nome, idade)

limite_saque_diario = 1000

BRAZILIAN_STATES = ['SP', 'RJ', 'SC', 'RS']

print(BRAZILIAN_STATES)

print("-----------------------------------------------------------------------------")
print("Quarta aula")

print("-Conversão de tipos-")

print("inteiro para float__>")

preco = 10
print(preco)

preco = float(preco)
print(preco)

preco = 10 / 2
print(preco)


print("Float para inteiro__>")

preco = 10.30
print(preco)

preco = int(preco)
print(preco)


print("Conversão por divisão__>")

preco = 10
print(preco)

print(preco / 2)

print("preco // 2")


print("Numérico para string__>")

preco = 10.50
idade = 28

print(str(preco))

print(str(idade))

texto = f"idade {idade} preco {preco}"
print(texto)


print("String para número__>")

preco = "10.50"
idade = "28"

print(float(preco))

print(int(idade))

#print("Erro de conversão__>")
#
# preco = "python"
# print(float(preco))


print("-Conversão de tipos(Continuação)-")

print(int(1.97348728))
print(int("10.10"))
print(float("10.10"))
print(float(100))

valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))

print(100 / 2)
print(100 // 2)


print("-----------------------------------------------------------------------------")
print("Quinta aula")

print("-Funções de entrada e saída-")

print("Exemplo__>")

nome = input("Informe seu nome: ")

print("Exemplo2__>")

nome = "Guilherme"
sobrenome = "Carvalho"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="#")

nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

print(nome, idade)
print(nome, idade, end="...\n")
print(nome, idade, sep="#", end="...\n")
print(nome, idade, sep="#")