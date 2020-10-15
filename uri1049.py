lista = [input() for _ in range(3)]
if 'invertebrado' in lista:
   if 'inseto' in lista:
      if 'hematofago' in lista:
          print('pulga')
      else:
          print('lagarta')
   else:
      if 'hematofago' in lista:
          print('sanguessuga')
      else:
          print('minhoca')
else:
   if 'ave' in lista:
      if 'carnivoro' in lista:
          print('aguia')
      else:
          print('pomba')
   else:
      if 'onivoro' in lista:
          print('homem')
      else:
          print('vaca')
