lista = [input() for _ in range(3)]
if 'invertebrado' in str(lista):
   if 'inseto' in str(lista):
      if 'hematofago' in str(lista):
          print('pulga')
      elif 'herbivoro' in str(lista):
          print('lagarta')
   elif 'anelideo' in str(lista):
      if 'hematofago' in str(lista):
          print('sanguessuga')
      elif 'onivoro' in str(lista):
          print('minhoca')
elif 'vertebrado' in str(lista):
   if 'ave' in str(lista):
      if 'carnivoro' in str(lista):
          print('aguia')
      elif 'onivoro' in str(lista):
          print('pomba')
   elif 'mamifero' in str(lista):
      if 'onivoro' in str(lista):
          print('homem')
      elif 'herbivoro' in str(lista):
          print('vaca')
