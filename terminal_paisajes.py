#!/usr/bin/python
# -*- coding: utf-8 -*-

from terminal import *
import random

#-------------------------------------------------------------------------------
# BLOQUE IZQUIERDO
# Bloque de "()" generado de forma random en la coordenada x definida.
def BloqueAleatorio(x, suelo):
	altura_bloque = random.randint(0,20)
	i = 0
	while i<altura_bloque:
		y = suelo - altura_bloque + i
		gotoxy(x,y)
		print "#"*20
		i = i + 1
	return altura_bloque
#-------------------------------------------------------------------------------
# Suelo
def Suelo(caracter, suelo) :
	gotoxy(1,suelo)
	print caracter * 80
#-------------------------------------------------------------------------------
#Celdas estilo buscaminas
def buscaminas(filas,columnas):
	clrscr()
	n = 0
	x = 4
	y = 2
	t = 0
	while n<filas:
		gotoxy(x,y)
		print "[   " * columnas
		y += 1
		gotoxy(x,y)
		print " ---" * columnas
		y += 1 
		n += 1 
	x = (4*columnas)+4
	m = 0
	y = 2
	while m<filas:
		gotoxy(x,y)
		print "]"
		y += 1 
		gotoxy(x,y)
		print " "
		y += 1
		m += 1 
#-------------------------------------------------------------------------------
