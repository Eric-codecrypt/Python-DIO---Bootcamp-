

# 🐍 Bootcamp DIO - Python Developer

Este README contém um resumo com explicações e exemplos práticos das aulas introdutatórias do Bootcamp Python Developer da DIO.

---

## Aula 1: Tipos de Dados Built-in

### ✅ Tipos Padrão (`built-in types`)

```python
# Texto
texto = "Olá, mundo!"         # str

# Números
inteiro = 10                  # int
decimal = 3.14                # float
complexo = 1 + 2j             # complex

# Sequência
lista = [1, 2, 3]             # list
tupla = (1, 2, 3)             # tuple
faixa = range(5)              # range

# Map
dicionario = {"nome": "Ana"} # dict

# Coleção
conjunto = {1, 2, 3}          # set
conjunto_imutavel = frozenset([1, 2, 3])

# Booleano
verdadeiro = True            # bool
falso = False

# Binário
b = bytes(4)
ba = bytearray(4)
mv = memoryview(bytes(4))
```

---

## Aula 2: Terminal Interativo

### 🔍 Comandos úteis

```python
dir()        # Lista nomes no escopo atual
dir(100)     # Lista os atributos de um objeto (int)

help()       # Acessa o sistema de ajuda
help(str)    # Ajuda sobre strings
```

---

## Aula 3: Variáveis e Constantes

### 💡 Declaração de Variáveis

```python
idade = 23
nome = "Guilherme"
print(f"Meu nome é {nome} e tenho {idade} anos.")
```

### 📌 Múltiplas atribuições

```python
idade, nome = 23, "Guilherme"
```

### ✅ Convenção para constantes (tudo em maiúsculo)

```python
DEBUG = True
LIMITE_SAQUE = 1000
```

---

## Aula 4: Conversão de Tipos

### 🔄 Inteiro → Float

```python
preco = 10
preco = float(preco)
print(preco)  # 10.0
```

### 🔄 Float → Inteiro

```python
preco = 10.75
preco = int(preco)
print(preco)  # 10
```

### 🔄 Numérico → String

```python
preco = 10.50
print(str(preco))  # '10.5'
```

### 🔄 String → Numérico

```python
preco = "10.50"
print(float(preco))  # 10.5

idade = "28"
print(int(idade))    # 28
```

### ❌ Erro de conversão

```python
# float("python") -> ValueError
```

---

## Aula 5: Entrada e Saída

### 📥 Entrada de Dados

```python
nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")
```

### 📤 Saída de Dados

```python
print(nome, idade)
print(nome, idade, sep="#", end="...\n")
```

---

## Aula 6: Estruturas Condicionais

### 🔀 `if`, `elif`, `else`

```python
idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 12:
    print("Você é adolescente.")
else:
    print("Você é criança.")
```

### ➕ Operadores de Comparação

| Operador | Significado      |
| -------- | ---------------- |
| `==`     | Igual a          |
| `!=`     | Diferente de     |
| `>`      | Maior que        |
| `<`      | Menor que        |
| `>=`     | Maior ou igual a |
| `<=`     | Menor ou igual a |

---

## Aula 7: Laços de Repetição

### 🔁 `while`

```python
contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1
```

### 🔁 `for` com `range`

```python
for i in range(5):
    print(f"Iteração {i}")
```

### 📜 Iterando listas

```python
nomes = ["Ana", "João", "Pedro"]

for nome in nomes:
    print(f"Olá, {nome}!")
```

### ⛔ `break` e `continue`

```python
for i in range(10):
    if i == 3:
        continue  # pula o 3
    if i == 7:
        break     # interrompe no 7
    print(i)
```

---

## Exemplos Adicionais

### 🧲 Operadores

```python
print(5 // 2)  # 2 (divisão inteira)
print(5 / 2)   # 2.5
```

### 🔍 Tipagem e Conversão

```python
valor = 10
valor_str = str(valor)
print(type(valor))       # <class 'int'>
print(type(valor_str))   # <class 'str'>
```

---

## 🧠 Por que usar tipos de dados?

Tipos definem o comportamento dos dados:

* `int`: armazena números inteiros
* `str`: manipula texto
* `bool`: representa verdadeiro/falso

Eles ajudam na organização, segurança e clareza do código.

---

## ✅ Exercício

```python
# Faça um programa que peça nome e idade e mostre:
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Olá {nome}, você tem {idade} anos.")
```

---

## Aula 8: Funções

### 🔢 Declaração de funções

```python
def saudacao():
    print("Olá, mundo!")

saudacao()
```

### 👥 Parâmetros e argumentos

```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Maria")
```

### 🌐 Funções com retorno

```python
def somar(a, b):
    return a + b

resultado = somar(2, 3)
print(resultado)
```

### 🧪 Exercício Prático

Crie uma função chamada `apresentar` que recebe dois parâmetros: `nome` e `idade`. A função deve imprimir uma mensagem formatada apresentando a pessoa.

```python
def apresentar(nome, idade):
    print(f"Olá, meu nome é {nome} e tenho {idade} anos.")

# Teste da função
apresentar("Carlos", 25)
```

```python
def saudacao():
    print("Olá, mundo!")

saudacao()
```

### 👥 Parâmetros e argumentos

```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Maria")
```

### 🌐 Funções com retorno

```python
def somar(a, b):
    return a + b

resultado = somar(2, 3)
print(resultado)
```

---

## Aula 9: Listas

### 📂 Criando listas

```python
frutas = ["maçã", "banana", "laranja"]
```

### ➕ Operando listas

```python
frutas.append("uva")
frutas.remove("banana")
print(frutas[0])
print(len(frutas))
```

### 📅 Iterando listas

```python
for fruta in frutas:
    print(fruta)
```

---

## Aula 10: Dicionários

### 💰 Criando dicionários

```python
pessoa = {"nome": "João", "idade": 30}
```

### ➕ Operando dicionários

```python
print(pessoa["nome"])
pessoa["idade"] = 31
pessoa["cidade"] = "SP"

# Usando get() para evitar erro ao acessar chave inexistente
print(pessoa.get("email", "Chave não encontrada"))
```

### 📗 Iterando dicionários

```python
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
```

### 🎓 Exercício Prático

Crie um dicionário com informações de um produto (nome, preço, estoque). Em seguida, exiba as informações formatadas.

```python
produto = {
    "nome": "Notebook",
    "preco": 3500.00,
    "estoque": 12
}

print(f"Produto: {produto['nome']}")
print(f"Preço: R${produto['preco']}")
print(f"Estoque: {produto['estoque']} unidades")
```

```python
pessoa = {"nome": "João", "idade": 30}
```

### ➕ Operando dicionários

```python
print(pessoa["nome"])
pessoa["idade"] = 31
pessoa["cidade"] = "SP"
```

### 📗 Iterando dicionários

```python
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
```


