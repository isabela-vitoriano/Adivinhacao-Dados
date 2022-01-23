# Importando as bibliotecas
from time import sleep
from random import randint

# Escolhendo o modo do jogo
dif = '0'
while dif != '1' and dif !='2':
  dif = str(input("""Vamos jogar um jogo de adivinhação! A cada rodada, pensarei em um número, o qual você deve adivinhar.

  [ 1 ] Modo fácil
  [ 2 ] Modo difícil
  
Escolha o modo:
  """)).strip()
  if dif != '1' and dif !='2':
    print('Digite apenas "1" ou "2", sem aspas.\n')

# Modo fácil
# Computador escolhendo um número
if dif == '1':
  print('.',end='')
  sleep(0.5)
  print('.',end='')
  sleep(0.5)
  print('.',end='')
  sleep(0.5)
  num = str(randint(1,5))
  print('EU PENSEI EM UM NÚMERO ENTRE 1 E 5...')
  sleep(1)

# Usuário escolhendo um número
  cont = 1
  adv = '0'
  while adv != num:
    adv = str(input('\nQual o número você adivinha?: \n')).strip()

    if adv == num: #se ele acertar
      print(f"""\033[0;32m\nParabéns! Você precisou de {cont} tentativa(s) pra ganhar!
Porém, pra ser um adivinho de verdade, tente fazer o mesmo no nível difícil, com mais possibilidades!""". format(num,adv))
    else: #se ele errar
      cont += 1
      print("""\033[0;31m
Não foi dessa vez :(
\033[0;34mVamos tentar de novo!\033[0;0m""".format(adv,num) )

# Modo difícil
# Computador escolhendo um número
else:
  print('.',end='')
  sleep(0.5)
  print('.',end='')
  sleep(0.5)
  print('.',end='')
  sleep(0.5)
  num = str(randint(1,10))
  print('EU PENSEI EM UM NÚMERO ENTRE 1 E 10...')
  sleep(1)

# Usuário escolhendo um número
  cont = 1
  adv = '0'
  while adv != num:
    adv = str(input('\nQual o número você adivinha?: \n')).strip()

    if adv == num: #se ele acertar
      print(f"""\033[0;32mParabéns! Você precisou de {cont} tentativa(s) pra ganhar!""". format(num,adv))
    else: #se ele errar
      cont += 1
      print("""\033[0;31m
Não foi dessa vez :(
\033[0;34mVamos tentar de novo!\033[0;0m""".format(adv,num) )