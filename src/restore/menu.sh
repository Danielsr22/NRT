#!/bin/sh
MENU="4"
#Copyright 2010, 2011 EXO S.A.
while [ $MENU != '0' ] 
do

	dialog --nocancel --ok-label "Aceptar" \
	--default-item "4" --backtitle "SISTEMA DE RESTAURACION" --title "Elija la tarea a realizar" \
	--menu  "" 14 50  4\
	"1" "Restaurar Microsoft Windows 8.1"  \
	"2" "Restaurar GNU/linux" \
	"3" "Restaurar ambos Sistemas Operativos"  \
	"4" "Salir" 2> /tmp/seleccion

	OPCION=$(cat /tmp/seleccion)

	 case $OPCION in
	1 )  sh /root/seven.sh	;;
	2 )  sh /root/gnu.sh	;;
	3 )  sh /root/all.sh	;;
	4 )  sh /root/salir.sh ;;
	esac
done
