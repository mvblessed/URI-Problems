while True: 
    try:
       angulo = float(input())
       minutos = angulo*4
       horas = int((minutos//60)+6)
       minutos = int(minutos%60)
       if 6 <= horas < 12:
           print('Bom Dia!!\n',f'{horas:02}',':',f'{minutos:02}',':00',sep = '')
       elif 12 <= horas < 18:
           print('Boa Tarde!!\n',f'{horas:02}',':',f'{minutos:02}',':00',sep = '') 
       elif 18 <= horas < 24:
           print('Boa Noite!!\n',f'{horas:02}',':',f'{minutos:02}',':00',sep = '')
       else:
           horas = horas-24
           print('De Madrugada!!\n',f'{horas:02}',':',f'{minutos:02}',':00',sep = '')
    except EOFError:
       break
