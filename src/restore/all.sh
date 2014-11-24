#!/bin/sh
#Copyright 2010, 2011 EXO S.A.

dialog --backtitle "SISTEMA DE RESTAURACION" \
--title "RESTAURAR Windows 8.1 y GNU/LINUX" --yesno "Se restauraran los Sistemas Operativos Windows 8.1 y GNU/Linux a la imagen original de fabrica. La información que se encuentre en la partición de DATOS no sera modificada. Desea continuar?" 10 40 
	if [ $? = "0" ] ; then
	sh /root/restore-seven.img ; sh /root/restore-gnu.img ; sh /root/salir.sh
	fi
