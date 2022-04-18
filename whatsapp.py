import pyautogui as aut
import time
from tkinter import*
import numpy as np
import pandas as pd
from tkinter import messagebox as mb

# Interfaz gráfica
root=Tk()
root.geometry("620x360")
root.title("Aplicación Spam")
root.resizable(0,0)
root.iconbitmap("whatsapp_img.ico")

#String var
msg=StringVar()
fras=StringVar()

#Intvar
num=IntVar()

#Funciones
def enviar():
    if fras.get()=='' and msg.get()!='':
        if num.get()>0:
            time.sleep(7)
            for i in range(0,num.get()):
                aut.typewrite(msg.get())
                aut.press('enter')
        else:
            mb.showerror('Error','La cantidad de mensajes a enviar debe ser un número mayor a cero.')

    else:
        if msg.get()=='' and fras.get()!='':
            if num.get()>0:
                time.sleep(7)

                # abrir contenido del archivo en formato txt
                file = fras.get()
                if '.txt' in file[-4:]:
                    a=pd.read_table('{}'.format(file), encoding='utf8')
                else:
                    a=pd.read_table('{}.txt'.format(file))

                #genero números aleatorios
                num_alea=np.random.randint(0,len(a)-1,num.get())

                for i in num_alea:
                    aut.typewrite(a.iloc[i,0])
                    time.sleep(0.1)
                    aut.press("enter")
            else:
                mb.showerror('Error','La cantidad de mensajes a enviar debe ser un número mayor a cero.')
        if msg.get()=='' and fras.get()=='':
            mb.showerror("Error","Se debe llenar una de las dos entradas para saber que mensaje enviar.")
        else:
            mb.showerror("Error","Se debe llenar solo una de las dos entradas para saber que mensaje enviar.")
#etiqueta pata msg
etiqueta=Label(root, text="Ingrese el mensaje que desea enviar para spamear", bd=10)
etiqueta.place(x=160,y=40)

#Etiqueta para frase_amor
etiqueta_am=Label(root, text="O ingrese el nombre del archivo en que se encuentran sus frases para enviar", bd=10)
etiqueta_am.place(x=140,y=100)

#etiqueta para num de mensajes a enviar
etiqueta1=Label(root, text="Ingrese el número de mensajes que desea enviar", bd=10)
etiqueta1.place(x=160,y=150)


#input número de mensajes
num_msg=Entry(root, textvariable=num,bd=5)
num_msg.place(x=220, y=180)

#input dirección 
dir_frases=Entry(root, textvariable=fras, bd=5)
dir_frases.place(x=220, y=130)

# input mensaje
mensaje=Entry(root, textvariable=msg, bd=5)
mensaje.place(x=220, y=70)

#Advertencia
etiqueta2=Label(root, text="¡Después de haber dado click a ENVIAR tiene exactamente 7 segundos para hacer click en la zona", bd=10, font=("Helvetica",8,"bold"))
etiqueta2.place(x=30,y=210)
etiqueta3=Label(root, text="de envío de mensajes de whatsapp web!", bd=10, font=("Helvetica",8,"bold"))
etiqueta3.place(x=200,y=235)

boton_enviar=Button(root, text="ENVIAR", bd=10, command=enviar)
boton_enviar.place(x=260, y=280)

root.mainloop()
