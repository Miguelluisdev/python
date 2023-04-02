from random import choice
#objetivo principal
objetivo1 = 'matar o monstros que invadiram uma vila'
objetivo2 = 'invadir uma masmorra'
objetivo3 = 'proteger a cidade de hobgoblins'
lista =[objetivo1,objetivo2,objetivo3]
objetivo_prinvipal = choice(lista)
print('o objetivo principal da missão é {}'.format(objetivo_prinvipal))
#viloes
vilao1 = 'uma esfinge'
vilao2 = 'necromancer'
vilao3 = 'goblin xamã'
liste = [vilao1,vilao2,vilao3]
lista_vilao = choice(liste)
print(' o vilão da missao atual é {}'.format(lista_vilao))
#agora local
local1 = 'catacumbas e esgotos abaixo da capital do sol nascente'
local2 = 'vila dos pescadores'
local3 = 'fallgrim'
lista_local = [local1,local2,local3]
local_missao = choice(lista_local)
print('o local da missão é {}'.format(local_missao))