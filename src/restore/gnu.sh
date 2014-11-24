#!/bin/sh
#Copyright 2010, 2011 EXO S.A.

dialog --backtitle "SISTEMA DE RESTAURACION" \
--title "RESTAURAR GNU/LINUX" --yesno "Se restaurara el Sistema Operativo GNU/Linux a la imagen original de fabrica. La información que se encuentre en la partición de DATOS no sera modificada. Desea continuar?" 10 40 
	if [ $? = "0" ] ; then
	sh /root/restore-gnu.img ; sh /root/salir.sh 
	fi
