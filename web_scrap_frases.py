from bs4 import BeautifulSoup
import requests as rq

# url de la cual se saca las frases

url="https://frases-positivas.com"

# Descargo contenido de la página

contenido_pg=rq.get(url)

#Transformo a formato soup

soup_pg=BeautifulSoup(contenido_pg.content, "html.parser")


frases=soup_pg.find_all('li', class_="")

#transformo en formato text
lista_frases=[i.text for i in frases]

#Exporto a un txt
f=open("frases_motivacion.txt","w",encoding='utf8')
f.write('Frases de Motivación\n')
for i in lista_frases:
    f.write(i+"\n")

f.close()



