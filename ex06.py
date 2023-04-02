nome = input("digite seu nome")
peso = float(input("digite seu peso"))
altura = float(input("digite sua altura"))

imc = peso/(altura*altura)
print(nome)
print(peso)
print(altura)
print(imc)


listaprodutos = ["iphine","ipad","notebook"]
listapreços = [1500,5000,600]

for preços in listapreços:
    print(preços *2)

for produto in listaprodutos:
    print(produto)

    for i in range(10):
        print("lol")