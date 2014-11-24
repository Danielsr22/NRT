#!/bin/sh
MENU="2"
#Copyright 2010, 2011 EXO S.A.

while [ $MENU != '0' ] 
do
	dialog --nocancel --ok-label "Aceptar" \
	--default-item "2" --backtitle "SISTEMA DE RESTAURACION" --title "AVISO IMPORTANTE" \
	--menu  "No se encontro cargador conectado, por favor conecte el equipo a la red electrica para continuar"  0 0 2\
		"1" "Reintentar"  \
		"2" "Salir" 2> /tmp/seleccion

	OPCION=$(cat /tmp/seleccion)

	case $OPCION in
		1 )  sh /root/restore.sh	;;
		2 )  sh /root/salir.sh ;;
	esac
	
done
