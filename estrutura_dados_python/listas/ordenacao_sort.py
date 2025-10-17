# Cria uma lista com várias linguagens de programação
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista em ordem alfabética (A → Z)
linguagens.sort()  
# Resultado: ["c", "csharp", "java", "js", "python"]


# Cria novamente a lista original
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista em ordem alfabética reversa (Z → A)
linguagens.sort(reverse=True)  
# Resultado: ["python", "js", "java", "csharp", "c"]


# Cria novamente a lista original
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista pelo tamanho das palavras (da menor para a maior)
linguagens.sort(key=lambda x: len(x))  
# Resultado: ["c", "js", "java", "python", "csharp"]


# Cria novamente a lista original
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordena a lista pelo tamanho das palavras (da maior para a menor)
linguagens.sort(key=lambda x: len(x), reverse=True)  
# Resultado: ["python", "csharp", "java", "js", "c"]
