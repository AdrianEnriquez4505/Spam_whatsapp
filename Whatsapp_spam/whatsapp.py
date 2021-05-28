import pyautogui as aut
import time
from tkinter import*

# Interfaz gráfica
root=Tk()
root.geometry("620x290")
root.title("Aplicación Spam")
root.resizable(0,0)
root.iconbitmap("whatsapp_img.ico")

#String var
msg=StringVar()

#Intvar
num=IntVar()

#Funciones
def enviar():
    time.sleep(7)

    for i in range(0,num.get()):
        aut.typewrite(msg.get())
        time.sleep(0.2)
        aut.press('enter')

etiqueta=Label(root, text="Ingrese el mensaje que desea enviar para spamear", bd=10)
etiqueta.place(x=160,y=40)

etiqueta1=Label(root, text="Ingrese el número de mensajes que desea enviar", bd=10)
etiqueta1.place(x=160,y=100)

num_msg=Entry(root, textvariable=num,bd=5)
num_msg.place(x=220, y=130)

mensaje=Entry(root, textvariable=msg, bd=5)
mensaje.place(x=220, y=70)

#Advertencia
etiqueta2=Label(root, text="¡Después de haber dado click a ENVIAR tiene exactamente 7 segundos para hacer click en la zona", bd=10, font=("Helvetica",8,"bold"))
etiqueta2.place(x=30,y=170)
etiqueta3=Label(root, text="de envío de mensajes de whatsapp web!", bd=10, font=("Helvetica",8,"bold"))
etiqueta3.place(x=200,y=194)

boton_enviar=Button(root, text="ENVIAR", bd=10, command=enviar)
boton_enviar.place(x=260, y=230)

root.mainloop()
