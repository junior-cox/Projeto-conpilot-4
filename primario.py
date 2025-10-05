# esse projeto e um ogo de forca normal 
import random
import json

loop=True

while(loop):
    aleatorio=random.randint(0,2)
    with open('palavras.json','r') as arquivo:
       seletor=['a','b','c']
       se=seletor[aleatorio]
       print(aleatorio,se,aleatorio)
       per=json.load(arquivo)
       por=per[aleatorio]["{}{}".format(se,aleatorio)]
       print('====================')
       print(por,aleatorio)
       entrada=input("-")