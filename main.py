#!/usr/bin/python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------#
#	Enrique Sola Gayoso , <ike_soga@hotmail.com> , ANGRY BIRDS (ALPHA)			 #
#------------------------------------------------------------------------------#
import random
from terminal import *
from terminal_caca import *
from terminal_paisajes import *
import string
import math
#------------------------------------------------------------------------------#
# Elementos gráficos
pajaro = "*"
cerdo = "@"
g = 9.8
#------------------------------------------------------------------------------#
#Portada de entrada
clrscr()
print (" _____      _ _                       _                          ")    
print ("|  __ \    | | |                     | |                          ")   
print ("| |__) |__ | | | ___  ___    ___ __ _| |__  _ __ ___  __ _  ___  ___ ")
print ("|  ___/ _ \| | |/ _ \/ __|  / __/ _` | '_ \| '__/ _ \/ _` |/ _ \/ __|")
print ("| |  | (_) | | | (_) \__ \ | (_| (_| | |_) | | |  __/ (_| | (_) \__ \ ")
print ("|_|   \___/|_|_|\___/|___/  \___\__,_|_.__/|_|  \___|\__,_|\___/|___/ ")

titulo = "Bienvenido a mi versión especial del clásico Angry Birds"
titulo = titulo.center(TERMWIDTH)
print titulo
getch()
clrscr()
#------------------------------------------------------------------------------#
#Dificultad
Menu_4opciones("  MENÚ  ", "(1) START" , "(2) EXIT")
print "\n"
print "Seleccione una opción:\n"
opcion = int(raw_input(">>>"))
#------------------------------------------------------------------------------#
if opcion == 1 :
	clrscr()
#Paisaje
###########SUELO
	suelo = 24
	Suelo(";",suelo)
###########ALTURA DE LOS BLOQUES
	h_bloque1 = BloqueAleatorio(1,suelo)
	h_bloque2 = BloqueAleatorio(61,suelo)
###########ELEMENTOS
#Pájaro
	x_p = 10
	y_p = 25 - (h_bloque1 + 2)
	gotoxy(x_p,y_p)
	print "*"
#Cerdo
	x_c = random.randint(61,80)
	y_c = 25 - (h_bloque2 + 2)
	gotoxy(x_c, y_c)
	print "@"
	gotoxy(1,25)
#------------------------------------------------------------------------------#
#Bucle de lanzamiento del pájaro
	datos = True	
	while datos:
		gotoxy(1,1)
		a = float(raw_input("Ángulo:"))
		a = math.radians(a)
		v = float(raw_input("Velocidad(m/s):"))
		Vox = v*(math.cos(a))
		Voy = v*(math.sin(a))
		gotoxy(1,1)
		t = 0.0
		g = 9.8
		x = x_p
		y = y_p
		mov_pajaro = True
		#Movimiento del ave
		while mov_pajaro:
			if x > 0 and x <= 80 and y > 0 and y <= 25:
				gotoxy(x,y)
				print " "
			x= x_p + int(Vox * t) + 1
			y= y_p - int((Voy * t) - (1/2.0*g*(t**2)))
			gotoxy(1,1)
			#Trayectoria del ave dentro del mapa
			if x >=1 and x < 80 and y >=1 and y < 24 : 
				gotoxy(x,y)
				print "*"
			#Condición de impacto
			if x == x_c and y == y_c :
				explosion(x_c,y_c)
				clrscr()
				titulo = "Enhorabuena! Has ganado!"
				titulo = titulo.center(TERMWIDTH)
				print titulo
				datos = False
				getch()
				break
			t = t + 0.05
			time.sleep(0.1)
			#Control del ave dentro del mapa traduciendo la salida como derrota
			if x >= 80 or y >= 24 :
				mov_pajaro = False
	getch()
#TODO CONTROL DE IMPACTO COMPLETO

