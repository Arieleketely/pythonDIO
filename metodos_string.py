
### 1. **capitalize()**

#Coloca a primeira letra da string em maiúscula e o restante em minúscula.


texto = "python é incrível"
print(texto.capitalize())
# Saída: "Python é incrível"

### 2. **count()**

#Conta quantas vezes um trecho aparece dentro da string.


frase = "banana"
print(frase.count("a"))
# Saída: 3


### 3. **endswith()**

#Verifica se a string termina com um determinado sufixo (retorna True ou False).


arquivo = "relatorio.pdf"
print(arquivo.endswith(".pdf"))
# Saída: True


### 4. **join()**

#Junta elementos de uma lista (ou iterável) em uma única string, usando o separador definido.


palavras = ["Python", "é", "legal"]
print(" ".join(palavras))
# Saída: "Python é legal"


### 5. **split()**

#Divide a string em uma lista, usando como base o separador (por padrão, espaço).


frase = "Python é muito bom"
print(frase.split())
# Saída: ['Python', 'é', 'muito', 'bom']


### 6. **startswith()**

#Verifica se a string começa com um determinado prefixo.

mensagem = "Olá, mundo!"
print(mensagem.startswith("Olá"))
# Saída: True

### 7. **replace()**

#Substitui partes da string por outra.

frase = "Eu gosto de Java"
print(frase.replace("Java", "Python"))
# Saída: "Eu gosto de Python"
