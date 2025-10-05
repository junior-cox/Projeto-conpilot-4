# esse projeto e um ogo de forca normal 
# O
#/!\
#/ \
import random
import json

loop=True
pessoa=0
while(loop):
    aleatorio=random.randint(0,4)
    with open('palavras.json','r') as arquivo:
       print('----------------------------')
       res=json.load(arquivo)
       letras=["a","b","c","d","e"]
       letra_selecionada=letras[aleatorio]
       for a in range(5):
           re=res[aleatorio]['{}{}'.format(letra_selecionada,a)]
           print(re)
       resposta=res[aleatorio]["{}5".format(letra_selecionada)]
       print('----------------------------')
       print('com {} letras, 1 ja sei,3 desistir'.format(len(resposta)))
       entrada=input("ja sabe //")
       if  entrada==resposta:
          print('\033[92m====voce acerto ========\033[0m')
       else:
          print('\033[91m========voce errou=========\033[0m')
          pessoa+=1
       if pessoa==5:
          Loop=False
          print('\033[91m===================================\033[0m')
          print('\033[91m===============voce perdeu ========\033[0m')
          print('\033[91m===================================\033[0m')
          break