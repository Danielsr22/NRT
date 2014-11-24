#!/bin/sh
MENU="2"
#Copyright 2010, 2011 EXO S.A.



while [ $MENU != '0' ] 
do
	dialog --nocancel --ok-label "Aceptar" \
	--default-item "2" --backtitle "SISTEMA DE RESTAURACION" --title "AVISO IMPORTANTE" \
	--menu  "Mediante esta herramienta Usted puede restaurar las particiones de los Sistemas Operativos a las imagenes oririginales de fabrica. La informacion que se encuentre en la particion de DATOS no sera modificada. Sin embargo cualquier dato que haya sido salvado en las particiones de los Sistemas Operativos se perdera definitivamente. Desea continuar?"  0 0 2\
		"1" "Aceptar"  \
		"2" "Salir" 2> /tmp/seleccion

	OPCION=$(cat /tmp/seleccion)

	case $OPCION in
		1 )  sh /root/menu.sh	;;
		2 )  sh /root/salir.sh ;;
	esac
	
done
