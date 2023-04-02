print("1. Idoso")
print("2. gestante")
print("3. Cadeirante")
print("4. Nenhum destes")

respostas = int(input("voce é: "))

if (respostas==1) or (respostas==2) or (respostas==3):
  print("voce tem direito")
else:
  print("voce nao tem direito")



  banda = input('qual a banda certa')

  if not banda=='rush':
      print('herege')
  else: 
     print('Correto é rush')  