
# 📘 Bootcamp DIO - Python Developer

## 🧑‍🏫 Primeira Aula

### 🔹 Tipos built-in

```python
types:
    text       -> str
    number     -> int, float, complex
    sequence   -> list, tuple, range
    map        -> dict
    collection -> set, frozenset
    boolean    -> bool
    binary     -> bytes, bytearray, memoryview
```

### 🔹 Exemplos de tipos de dados

```python
11 + 10 + 1000        # operação numérica
1.5 + 1 + 0.5         # resultado: 3.0
True                  # booleano
False                 # booleano
"Python"              # string
```

## 🧑‍💻 Segunda Aula

### 🔹 Terminal interativo

```python
dir()
dir(100)
help()
help(100)
```

## 📚 Terceira Aula

### 🔹 Variáveis

```python
age = 23
name = 'Guilherme'
print(f'Meu nome é {name} e tenho {age} anos(s) de idade.')

age, name = (23, 'Guilherme')
print(f'Meu nome é {name} e tenho {age} anos(s) de idade.')
```

### 🔹 Constantes

```python
ABS_PATH = 'C:/Users/Turma 2/PyCharmMiscProject/'
DEBUG = True
STATES = ['SP', 'RJ', 'MG']
AMOUNT = 30.2
```

### 🔹 Teste de variáveis

```python
nome, idade = ("Giovanna", 27)
print(nome, idade)

limite_saque_diario = 1000
BRAZILIAN_STATES = ['SP', 'RJ', 'SC', 'RS']
print(BRAZILIAN_STATES)
```

## 🔁 Quarta Aula

### 🔹 Conversão de Tipos

#### 🔸 Inteiro → Float

```python
preco = 10
preco = float(preco)
preco = 10 / 2
```

#### 🔸 Float → Inteiro

```python
preco = 10.30
preco = int(preco)
```

#### 🔸 Divisão

```python
preco = 10
preco / 2      # divisão real
preco // 2     # divisão inteira
```

#### 🔸 Numérico → String

```python
preco = 10.50
idade = 28
texto = f"idade {idade} preco {preco}"
```

#### 🔸 String → Número

```python
preco = "10.50"
idade = "28"
float(preco)
int(idade)

# float("python") → ValueError
```

#### 🔸 Continuação

```python
int(1.97348728)
# int("10.10") → ValueError
float("10.10")
float(100)

valor = 10
valor_str = str(valor)
type(valor)
type(valor_str)

100 / 2     # 50.0
100 // 2    # 50
```

## 📥 Quinta Aula

### 🔹 Entrada e Saída de Dados

#### Exemplo com `input()`:

```python
nome = input("Informe seu nome: ")
```

#### Exemplo com `print()`:

```python
nome = "Guilherme"
sobrenome = "Carvalho"

print(nome, sobrenome)
print(nome, sobrenome, end="...
")
print(nome, sobrenome, sep="#")
```

#### Outro exemplo:

```python
nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

print(nome, idade)
print(nome, idade, end="...
")
print(nome, idade, sep="#", end="...
")
print(nome, idade, sep="#")
```
