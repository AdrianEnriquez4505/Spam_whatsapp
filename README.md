# Spam_whatsapp
Envía mensajes masivos en Whatsapp

Usando esta aplicación desarrollada con el lenguaje de programación Python en su versión 3.9.7 y usando las librerías pyautogui y Tkinter se puede realizar spam a una persona enviando el mismo mensaje una cantidad de veces dada por el usuario.

## Instalación de dependencias

Las dependencias que se usa para esta aplicación se encuentran en el archivo *requirements.txt*, las cuales pueden ser instaladas mediante el comando `pip install -r requirements.txt`. Se recomienda instalarlas en un entorno virtual de Python.

## Formas de enviar mensajes

Existen dos formas de enviar los mensajes.
  - Un mensaje dado por el usuario.
  - Un archivo de texto con los mensajes a enviar.
  
Para la segunda opción a forma de ejemplo se recopilan varias frases de motivación recopiladas de la página web <https://frases-positivas.com> mediante técnicas de web scraping. Para generar el archivo de texto con estas frases se debe ejecutar el script `web_scrap_frases.py`

## Advertencia

- Usar esta aplicación bajo su responsabilidad, ya que puede ocacionar un colapso en el dispositivo del que va a recibir el ataque spam.
