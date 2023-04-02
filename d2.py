produtos = ["ABC123","abd012", "ABS111", "AbB222" ]
texto = "abs012"


#funçao

def tratar_texto(texto):
    texto = texto.upper()
    texto = texto.strip()
    print(texto)
    return texto
texto = "abd012"
texto = tratar_texto(texto)
print(texto)

for i, produtos in enumerate(produtos):
    produtos[i] = tratar_texto(produtos)
print(produtos)

#deu erro n sei pq mas ta ai como cria uma funçao com def

# para devolver o texto em uma funçao usa return