#!/usr/bin/python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
# Libreria: terminal_caca.py
# Funciones de mierda que me van surgiendo , me invento y luego utilizo
# Enrique Sola, 2016 - <kikeelasturianu@gmail.com>.
# ------------------------------------------------------------------------------
from terminal import *
#Utilizo la libreria de Javi para mis propias funciones
#-------------------------------------------------------------------------------
#Devuelve un valor de True o False para detectar si un número es primo y luego
#incrementa el contador para llevar la cuenta de números primos en una secuencia
#previamente dada (intervalo)
def esPrimo(n):
	contador = 2
	esprimo = True
	while esprimo == True and contador <= n**0.5:
		prueba = n%contador
		if prueba == 0 :
			esprimo = False
			break
		else:
			contador += 1
	return esprimo
#-------------------------------------------------------------------------------
#Pone en la terminal un título to flama
def tituloPrograma(texto , sub_texto):
	clrscr()
	longitud_texto = len(texto)
	posicion_texto = (TERMWIDTH-longitud_texto)/2
	longitud_sub_texto = len(sub_texto)
	posicion_sub_texto = (TERMWIDTH-longitud_sub_texto)/2
	if longitud_texto > longitud_sub_texto:
		drawbox((posicion_texto - 2 ) , 1 , (longitud_texto + 4) , 4 ) 
	else:
		drawbox((posicion_sub_texto - 2 ) , 1 , (longitud_sub_texto + 4) , 4 )
	gotoxy(posicion_texto,2)
	print texto
	gotoxy(posicion_sub_texto ,3)
	print sub_texto
#-------------------------------------------------------------------------------
#Pone otro título pero mucho mas ARCADE por decirlo de algún modo
def titulosencillo(texto):
	clrscr()
	longitud_texto = len(texto)
	x = (TERMWIDTH/2) - longitud_texto
	y = TERMHEIGHT/2
	gotoxy(x,y)
	print texto
#-------------------------------------------------------------------------------
def Menu_6opciones(titulo , sub_titulo , op1 , op2 , op3 , op4 , op5 , op6 , op7 ):
	clrscr()
	longitud_titulo = len(titulo)
	posicion_titulo = (TERMWIDTH-longitud_titulo)/2
	longitud_sub_titulo = len(sub_titulo)
	posicion_sub_titulo = (TERMWIDTH-longitud_sub_titulo)/2
	longitud_op1 = len(op1)
	posicion_op1 = (TERMWIDTH-longitud_op1)/2
	longitud_op2 = len(op2)
	posicion_op2 = (TERMWIDTH-longitud_op2)/2
	longitud_op3 = len(op3)
	posicion_op3 = (TERMWIDTH-longitud_op3)/2
	longitud_op4 = len(op4)
	posicion_op4 = (TERMWIDTH-longitud_op4)/2
	longitud_op5 = len(op5)
	posicion_op5 = (TERMWIDTH-longitud_op5)/2
	longitud_op6 = len(op6)
	posicion_op6 = (TERMWIDTH-longitud_op6)/2
	longitud_op7 = len(op7)
	posicion_op7 = (TERMWIDTH-longitud_op7)/2
	
	drawbox((posicion_titulo - 18 ) , 1 , 42 , 12 ) 
	
	gotoxy(posicion_titulo,2)
	print titulo
	gotoxy(posicion_sub_titulo ,3)
	print sub_titulo
	gotoxy(posicion_op1,4)
	print op1
	gotoxy(posicion_op1,5)
	print op2
	gotoxy(posicion_op1,6)
	print op3
	gotoxy(posicion_op1,7)
	print op4
	gotoxy(posicion_op1,8)
	print op5
	gotoxy(posicion_op1,9)
	print op6
	gotoxy(posicion_op1,10)
	print op7
#-------------------------------------------------------------------------------
def Menu_4opciones(titulo , op1 , op2 ):
	clrscr()
	longitud_titulo = len(titulo)
	posicion_titulo = (TERMWIDTH-longitud_titulo)/2
	longitud_op1 = len(op1)
	posicion_op1 = (TERMWIDTH-longitud_op1)/2
	longitud_op2 = len(op2)
	posicion_op2 = (TERMWIDTH-longitud_op2)/2
	
	drawbox((posicion_titulo - 3 ) , 1 , 15 , 7 ) 
	
	gotoxy(posicion_titulo,2)
	print titulo
	gotoxy(posicion_op1,4)
	print op1
	gotoxy(posicion_op1,5)
	print op2
#-------------------------------------------------------------------------------
def explosion(x,y):
	gotoxy(x-4 , y-2)
	print "OINK!"
	gotoxy(x-2 , y-1)
	print "\ | /"
	gotoxy(x-2,y)
	print "- X -"
	gotoxy(x-2, y+1)
	print "/ | \ "
	time.sleep(2)
#-------------------------------------------------------------------------------
def IncrementoGusano(x,y):
	cuerpo = [[x,y]]+cuerpo
#-------------------------------------------------------------------------------
def DibujarCuerpo(x,y):
	longitud = len(cuerpo)
	cola = cuerpo[longitud-1]
	gotoxy(cuerpo[0][0] , cuerpo[0][1])
	print "O"
	i = 1 
	while i < longitud:
		gotoxy(cuerpo[i][0] , cuerpo[i][1])
		print "X"
		i += 1
#-------------------------------------------------------------------------------
def TerminalAhorcado():
	drawbox(1,1,TERMWIDTH,TERMHEIGHT)
	x_f = TERMWIDTH/4
	y_f = int(TERMHEIGHT/3)
	gotoxy(x_f,y_f)

