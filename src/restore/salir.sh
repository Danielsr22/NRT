#!/bin/sh

#Copyright 2010, 2011 EXO S.A.

dialog --backtitle "SISTEMA DE RESTAURACION" \
--title "RESTAURACIÓN COMPLETADA" --msgbox "SE VUELVE AL MENÚ PRINCIPAL" 5 35
	if [ $? = "0" ] ; then
	reset; exit;clear
	fi
