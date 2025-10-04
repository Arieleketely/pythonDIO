texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# imprime apenas as vogais do texto
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # quebra de linha depois de imprimir as vogais

# imprime de 0 até 50, de 5 em 5
for numero in range(0, 51, 5):
    print(numero, end=" ")
