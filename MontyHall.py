# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 16:13:20 2021

@author: Erik Trincado
"""
from tkinter import*
import tkinter as tk
import random

ventana= Tk()
ventana.title("Problema de Monty Hall")
ventana.config(bd=20)
ventana.geometry("240x240")
ventana.resizable(0,0)

#comando de elección
global primer_eleccion, puerta
primer_eleccion = []
def puerta_1():
    primer_eleccion.clear()
    primer_eleccion.append(1)
    P_eleccion = DoubleVar()
    P_eleccion.set(primer_eleccion)
    pantalla1= Entry(ventana, textvariable=P_eleccion, width=3,state="disable")
    pantalla1.place(x=145, y=90)
    return primer_eleccion
    
def puerta_2():
    primer_eleccion.clear()
    primer_eleccion.append(2)
    P_eleccion = DoubleVar()
    P_eleccion.set(primer_eleccion)
    pantalla1= Entry(ventana, textvariable=P_eleccion, width=3,state="disable")
    pantalla1.place(x=145, y=90)
def puerta_3():
    primer_eleccion.clear()
    primer_eleccion.append(3)
    P_eleccion = DoubleVar()
    P_eleccion.set(primer_eleccion)
    pantalla1= Entry(ventana, textvariable=P_eleccion, width=3,state="disable")
    pantalla1.place(x=145, y=90)
    
#Entrega un esenario aleatorio del juego
def revelar():
    l = ["CABRA", "CABRA", "AUTO"]
    random.shuffle(l)
    print(l)
    eleccion = primer_eleccion[0] -1
    
    def revelar2():
        ventana4 = tk.Toplevel(ventana)
        ventana4.title("Resultado del juego")
        ventana4.geometry("240x180")
        ventana4.resizable(0,0)
        cambio = cambiar.get()
        
        puerta_1 = StringVar()
        puerta_2 = StringVar()
        puerta_3 = StringVar()
        puerta_1.set(l[0])
        puerta_2.set(l[1])
        puerta_3.set(l[2])
        
        etiqueta3= Label(ventana4, text="Contenido de las puertas:")
        etiqueta3.place(x=10,y=10)
        
        pantalla1= Entry(ventana4, textvariable= puerta_1, width=8,state="disable")
        pantalla1.place(x=20, y=50)
        pantalla2= Entry(ventana4, textvariable= puerta_2, width=8,state="disable")
        pantalla2.place(x=90, y=50)
        pantalla3= Entry(ventana4, textvariable= puerta_3, width=8,state="disable")
        pantalla3.place(x=160, y=50)
        
        etiqueta4= Label(ventana4, text="Tu elección es la puerta:")
        etiqueta4.place(x=20,y=90)
        
        print(primer_eleccion[0])
        print(cambio)
        
        if cambio == "NO":
            segunda_eleccion = primer_eleccion[0]
            eleccion_2 = DoubleVar()
            eleccion_2.set(segunda_eleccion)
            pantalla1= Entry(ventana4, textvariable=eleccion_2, width=3,state="disable")
            pantalla1.place(x=155, y=90)
            
            if l[segunda_eleccion -1] == "AUTO":
                    etiqueta4= Label(ventana4, text="FELICIDADES GANASTE UN AUTO!!!")
                    etiqueta4.place(x=20,y=110)
            else:
                etiqueta4= Label(ventana4, text="GANASTE UNA CABRA :(")
                etiqueta4.place(x=30,y=120)
                
        if cambio == "SI":
            if borrar == 0 and primer_eleccion[0] == 2:
                segunda_eleccion = 3
                print(primer_eleccion[0])
                eleccion_2 = DoubleVar()
                eleccion_2.set(segunda_eleccion)
                pantalla1= Entry(ventana4, textvariable=eleccion_2, width=3,state="disable")
                pantalla1.place(x=155, y=90)
                if l[segunda_eleccion -1] == "AUTO":
                    etiqueta4= Label(ventana4, text="FELICIDADES GANASTE UN AUTO!!!")
                    etiqueta4.place(x=20,y=120)
                else:
                    etiqueta4= Label(ventana4, text="GANASTE UNA CABRA :(")
                    etiqueta4.place(x=30,y=120)
                    
            elif borrar == 0 and primer_eleccion[0] == 3:
                segunda_eleccion = 2
                print(primer_eleccion[0])
                eleccion_2 = DoubleVar()
                eleccion_2.set(segunda_eleccion)
                pantalla1= Entry(ventana4, textvariable=eleccion_2, width=3,state="disable")
                pantalla1.place(x=155, y=90)
                if l[segunda_eleccion -1] == "AUTO":
                    etiqueta4= Label(ventana4, text="FELICIDADES GANASTE UN AUTO!!!")
                    etiqueta4.place(x=20,y=120)
                else:
                    etiqueta4= Label(ventana4, text="GANASTE UNA CABRA :(")
                    etiqueta4.place(x=30,y=120)
                    
            elif borrar == 1 and primer_eleccion[0] == 1:
                segunda_eleccion = 3
                print(primer_eleccion[0])
                eleccion_2 = DoubleVar()
                eleccion_2.set(segunda_eleccion)
                pantalla1= Entry(ventana4, textvariable=eleccion_2, width=3,state="disable")
                pantalla1.place(x=155, y=90)
                if l[segunda_eleccion -1] == "AUTO":
                    etiqueta4= Label(ventana4, text="FELICIDADES GANASTE UN AUTO!!!")
                    etiqueta4.place(x=20,y=120)
                else:
                    etiqueta4= Label(ventana4, text="GANASTE UNA CABRA :(")
                    etiqueta4.place(x=30,y=120)
                    
            elif borrar == 1 and primer_eleccion[0] == 3:
                segunda_eleccion = 1
                print(primer_eleccion[0])
                eleccion_2 = DoubleVar()
                eleccion_2.set(segunda_eleccion)
                pantalla1= Entry(ventana4, textvariable=eleccion_2, width=3,state="disable")
                pantalla1.place(x=155, y=90)
                if l[segunda_eleccion -1] == "AUTO":
                    etiqueta4= Label(ventana4, text="FELICIDADES GANASTE UN AUTO!!!")
                    etiqueta4.place(x=20,y=120)
                else:
                    etiqueta4= Label(ventana4, text="GANASTE UNA CABRA :(")
                    etiqueta4.place(x=30,y=120)
                    
            elif borrar == 2 and primer_eleccion[0] == 1:
                segunda_eleccion = 2
                print(primer_eleccion[0])
                eleccion_2 = DoubleVar()
                eleccion_2.set(segunda_eleccion)
                pantalla1= Entry(ventana4, textvariable=eleccion_2, width=3,state="disable")
                pantalla1.place(x=155, y=90)
                if l[segunda_eleccion -1] == "AUTO":
                    etiqueta4= Label(ventana4, text="FELICIDADES GANASTE UN AUTO!!!")
                    etiqueta4.place(x=20,y=120)
                else:
                    etiqueta4= Label(ventana4, text="GANASTE UNA CABRA :(")
                    etiqueta4.place(x=30,y=120)
                    
            elif borrar == 2 and primer_eleccion[0] == 2:
                segunda_eleccion = 1
                print(primer_eleccion[0])
                eleccion_2 = DoubleVar()
                eleccion_2.set(segunda_eleccion)
                pantalla1= Entry(ventana4, textvariable=eleccion_2, width=3,state="disable")
                pantalla1.place(x=155, y=90)
                if l[segunda_eleccion -1] == "AUTO":
                    etiqueta4= Label(ventana4, text="FELICIDADES GANASTE UN AUTO!!!")
                    etiqueta4.place(x=20,y=120)
                else:
                    etiqueta4= Label(ventana4, text="GANASTE UNA CABRA :(")
                    etiqueta4.place(x=30,y=120)

    ventana3 = tk.Toplevel(ventana)
    ventana3.title("Resultado del juego")
    ventana3.geometry("240x240")
    ventana3.resizable(0,0)
        
    etiqueta4= Label(ventana3, text="Tu elección es la puerta:")
    etiqueta4.place(x=20,y=90)
    etiqueta4= Label(ventana3, text="¿Deseas cambiar la puerta? (SI/NO)")
    etiqueta4.place(x=10,y=120)
        
    eleccion_1 = DoubleVar()
    eleccion_1.set(primer_eleccion[0])
        
    pantalla1= Entry(ventana3, textvariable=eleccion_1, width=3,state="disable")
    pantalla1.place(x=155, y=90)
    cambiar = StringVar()
    cambiar.set("")
    pantalla1= Entry(ventana3, textvariable=cambiar, width=4)
    pantalla1.place(x=200, y=120)
        
    #Boton REVELAR2
    Puerta_4= Button(ventana3, text="REVELAR RESULTADO", width=20, command = revelar2)
    Puerta_4.place(x=40, y=160)
        
    if l[0] == "CABRA" and primer_eleccion[0] != 1:
        borrar = 0
        puerta_1 = StringVar()
        puerta_2 = StringVar()
        puerta_3 = StringVar()
        puerta_1.set(l[0])
        puerta_2.set("PUERTA 2")
        puerta_3.set("PUERTA 3")
        etiqueta3= Label(ventana3, text="Contenido de las puertas:")
        etiqueta3.place(x=10,y=10)
        pantalla1= Entry(ventana3, textvariable= puerta_1, width=9,state="disable")
        pantalla1.place(x=20, y=50)
        pantalla2= Entry(ventana3, textvariable= puerta_2, width=9,state="disable")
        pantalla2.place(x=90, y=50)
        pantalla3= Entry(ventana3, textvariable= puerta_3, width=9,state="disable")
        pantalla3.place(x=160, y=50)
            
    elif l[1] == "CABRA" and primer_eleccion[0] != 2:
        borrar = 1
        puerta_1 = StringVar()
        puerta_2 = StringVar()
        puerta_3 = StringVar()
        puerta_1.set("PUERTA 1")
        puerta_2.set(l[1])
        puerta_3.set("PUERTA 3")
        etiqueta3= Label(ventana3, text="Contenido de las puertas:")
        etiqueta3.place(x=10,y=10)
        pantalla1= Entry(ventana3, textvariable= puerta_1, width=9,state="disable")
        pantalla1.place(x=20, y=50)
        pantalla2= Entry(ventana3, textvariable= puerta_2, width=9,state="disable")
        pantalla2.place(x=90, y=50)
        pantalla3= Entry(ventana3, textvariable= puerta_3, width=9,state="disable")
        pantalla3.place(x=160, y=50)
            
    elif l[2] == "CABRA" and primer_eleccion[0] != 3:
        borrar = 2
        puerta_1 = StringVar()
        puerta_2 = StringVar()
        puerta_3 = StringVar()
        puerta_1.set("PUERTA 1")
        puerta_2.set("PUERTA 2")
        puerta_3.set(l[2])
        etiqueta3= Label(ventana3, text="Contenido de las puertas:")
        etiqueta3.place(x=10,y=10)
        pantalla1= Entry(ventana3, textvariable= puerta_1, width=9,state="disable")
        pantalla1.place(x=20, y=50)
        pantalla2= Entry(ventana3, textvariable= puerta_2, width=9,state="disable")
        pantalla2.place(x=90, y=50)
        pantalla3= Entry(ventana3, textvariable= puerta_3, width=9,state="disable")
        pantalla3.place(x=160, y=50)
    
    
#Creación de Botones
Puerta_1= Button(ventana, text="PUERTA 1", width=8, command = puerta_1)
Puerta_1.place(x=0, y=50)
Puerta_2= Button(ventana, text="PUERTA 2", width=8, command = puerta_2)
Puerta_2.place(x=70, y=50)
Puerta_3= Button(ventana, text="PUERTA 3", width=8, command = puerta_3)
Puerta_3.place(x=140, y=50)
Puerta_4= Button(ventana, text="REVELAR RESULTADO", width=20, command = revelar)
Puerta_4.place(x=30, y=140)

#Labbel
etiqueta1= Label(ventana, text="Tu elección es la puerta: ")
etiqueta1.place(x=10,y=90)
etiqueta2= Label(ventana, text="!Escoge una puerta! ")
etiqueta2.place(x=50,y=10)

#Mostrar elección
if primer_eleccion == "":
    P_eleccion = StringVar()
    P_eleccion.set(primer_eleccion)
    pantalla1= Entry(ventana, textvariable=P_eleccion, width=3,state="disable")
    pantalla1.place(x=145, y=90)


ventana.mainloop()