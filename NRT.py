#!/bin/python
# -*- coding: utf-8 -*-

import os

def repararMBR():
	try:
		print('>> Intentando restaurar el MBR del disco, aguarde un momento...\n')
		os.system('dd if=iso/grub-n201.iso of=/dev/sda bs=512 count=1')
		print()
		print('>> La imágen de GRUB se ha restaurado correctamente.')
	except:
		print('>> ERROR. No se pudo escribir la imágen de MBR al disco.\n')
	input('\n>> Presione ENTER para continuar... \n')
	os.system('clear')

def repararGRUB():
	try:
		os.system('mount /dev/sda1 /mnt')
		print('\n--> Creando backup de la configuración actual del GRUB...')
		os.system('mv /mnt/boot/grub/grub.cfg /mnt/boot/grub/grub.cfg-BAK')
		print('\n--> Copiando archivo de configuración nuevo...')
		os.system('cp src/grub.cfg /mnt/boot/grub/')
		print('\n>> Se restauraron correctamente los parámetros de arranque del GRUB.')
	except:
		print('>> ERROR. No se pudo copiar la configuración del GRUB al directorio destino.')
	input('\n>> Presione ENTER para continuar... \n')
	os.system('clear')


def runCheck():
	try: ## VERIFICAR CON FSCK PARTICION DE RECU
		print('>> Chequeando integridad de la partción re recuperación...')
		os.system('fsck -a /dev/sda5')
		print('\n >> El sistema de archivos ha sido reparado.')
	except:
		print('>> ERROR. No se pudo realizar la verificación del sistema de archivos.')
	input('\n>> Presione ENTER para continuar... \n')
	os.system('clear')
	


def quitarPass():
	try:
		print('--> Intentando montar partición de Windows en /mnt...\n')
		os.system('mount /dev/sda2 /mnt')
		print('--> Partición de Windows (sda2) montada correctamente.\n')
		os.system('mv /mnt/Windows/System32/sethc.exe /mnt/Windows/System32/sethc.exe-BAK')
		print('--> Backup de "sethc.exe" creado correctamente.\n')
		os.system('cp /mnt/Windows/System32/cmd.exe /mnt/Windows/System32/sethc.exe')
		print('--> Los archivos correspondientes de modificaron correctamente.\n')
		print('>>> Ya puede arrancar el SO Windows y al momento de iniciar sesión, presione 5 veces la tecla Mayus. En la Terminal CMD teclee lo siguiente:\n')
		print('# control userpasswords2\n')
	except:
		print('>> ERROR. No fue posible modificar los archivos necesarios.')
	input('\n>> Presione ENTER para continuar... \n')
	os.system('clear')

def verifReboot():
	resp = input('\n>>> Está seuro de que desea reinciar?: [s/n]:')
	resp = resp.lower()
	if (resp == 's'):
		return True
	elif (resp == 'n'):
		return False
	else:
		print('>>> ERROR, El caracter ingresado no es válido, intente nuevamente...')
		verifReboot()

def reboot():
	input('>>> Presione ENTER para reinicir el sistema...')
	os.system('reboot')


def fun():
	input('TEST FUN, VUELVE')
	os.system('clear')

def menu():
	print('################# NETBOOK RECOVERY TOOL#################\n')
	print('\t1. Reparar imágen MBR de /dev/sda.')
	print('\t2. Restaurar configuración de GRUB.')
	print ('\t3. Verificar integridad de Partición de Recuperación.')
	print('\t4. Preparar restauración de contraseña de Windows 7.')
	print('\t0. Salir')
	print('\tR. Reiniciar')
	print('\t t. test')
	option = str(input('>> Opcion deseada: '))

	while (option != '0'):
		## Evaluo las opciones
		print()
		if (option == '1'):
			repararMBR()
		elif (option == '2'):
			repararGRUB()
		elif (option == '3'):
			runCheck()
		elif (option == '4'):
			quitarPass()
		elif (option == 't'):
			print ('TEST OK')
			fun()
		else:
			print('>> ERROR. El carácter ingresado no es una opción válida.')
			os.system('clear')

		print('################# NETBOOK RECOVERY TOOL#################\n')
		print('\t1. Reparar imágen MBR.')
		print('\t2. Restaurar configuración de GRUB.')
		print ('\t3. Verificar integridad de Partición de Recuperación.')
		print('\t4. Preparar restauración de contraseña de Windows 7.')
		print('\t0. Salir')
		print('\tR. Reiniciar')
		print()
		option = str(input('>> Opcion deseada: '))


	## Si ingresa 0, termina el programa.
	if (option == '0'):
		input('>> Presione una tecla para salir...')
	if (option == 'R') | (option == 'r'):
		reboot(verifReboot())


## Programa principal
try:
	os.system('clear')
	menu()
## Si corto la ejecución con Ctrl + C, no veo el Traceback
except (KeyboardInterrupt):
	print('\n\n>> Programa finalizado.')
