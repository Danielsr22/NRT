#!/bin/python

import os

def repararMBR():
	try:
		print('>> Intentando restaurar el MBR del disco, aguarde un momento...\n')
		print('os.system(dd if=iso/grub-n201.iso of=/dev/sda bs=512 count=1)')
		print()
		print('>> La imágen de GRUB se ha restaurado correctamente.')
	except:
		print('>> ERROR. No se pudo escribir la imágen de MBR al disco.\n')
	print('\n>> Presione ENTER para continuar... \n')
	input()
	os.system('clear')
	menu()

def repararGRUB():
	try:
		print('os.system(mount /dev/sda1 /mnt)')
		print('\n--> Creando backup de la configuración actual del GRUB...')
		print('os.system(mv /mnt/boot/grub/grub.cfg /mnt/boot/grub/grub.cfg-BAK)')
		print('\n--> Copiando archivo de configuración nuevo...')
		print('os.system(cp src/grub.cfg /mnt/boot/grub/)')
		print('\n>> Se restauraron correctamente los parámetros de arranque del GRUB.')
	except:
		print('>> ERROR. No se pudo copiar la configuración del GRUB al directorio destino.')
	print('\n>> Presione ENTER para continuar... \n')
	input()
	os.system('clear')
	menu()


def runCheck():
	try: ## VERIFICAR CON FSCK PARTICION DE RECU
		print('>> Chequeando integridad de la partción re recuperación...')
		print('os.system(fsck -a /dev/sda5)')
		print('\n >> El sistema de archivos ha sido reparado.')
	except:
		print('>> ERROR. No se pudo realizar la verificación del sistema de archivos.')
	print('\n>> Presione ENTER para continuar... \n')
	input()
	os.system('clear')
	menu()
	


def quitarPass():
	try:
		print('--> Intentando montar partición de Windows en /mnt...\n')
		os.system('mount /dev/sda2 /mnt')
		print('--> Partición de Windows (sda2) montada correctamente.\n')
		os.system('mv /mnt/Windows/System32/sethc.exe /mnt/Windows/System32/sethc.exe-BAK')
		os.system('cp /mnt/Windows/System32/cmd.exe /mnt/Windows/System32/sethc.exe')
		print('--> Los archivos correspondientes de modificaron correctamente.\n')
		print('>>> Ya puede arrancar el SO Windows y al momento de iniciar sesión, presione 5 veces la tecla Mayus. En la Terminal CMD teclee lo siguiente:\n')
		print('# control userpasswords2\n')
	except:
		print('>> ERROR. No fue posible modificar los archivos necesarios.')
	print('\n>> Presione ENTER para continuar... \n')
	input()
	os.system('clear')
	menu()




	## Mover CMD.EXE a SETHC.EXE
	print('MODIFICACIONES REALIZADAS CON EXITO, ARRANQUE CON WINDOWS Y PRESIONE 5 VECES "SHIFT", EN LA CONSOLA TECLEE "control userpasswords2" PARA SETEAR LA NUEVA CONTRASEÑA.')
	

def menu():
	print('################# NETBOOK RECOVERY TOOL#################\n')
	print('\t1. Reparar imágen GRUB.')
	print('\t2. Reparar arranque de Partición de Recuperación.')
	print ('\t3. Verificar integridad de Partición de Recuperación.')
	print('\t4. Preparar restauración de contraseña de Windows 7.')
	print('\t0. Salir')
	print('\tR. Reiniciar')
	print()
	op = str(input('>> Opcion deseada: '))
	print()

	## Testeo las opciones
	if (op != '0'):
		if (op == '1'):
			repararMBR()
		elif (op == '2'):
			repararGRUB()
		elif (op == '3'):
			runCheck()
		elif (op == '4'):
			quitarPass()
		else:
			print('>> ERROR. El carácter ingresado no es una opción válida.')
			os.system('clear')
			menu()
	## Si ingresa 0, termina el programa.
	if (op == '0'):
		input('>> Presione una tecla para salir...')
	if (op == 'R') | (op == 'r'):
		input('>> Presione ENTER para reinicar el equipo...')
		print('os.system(reboot)')




## Programa principal
try:
	os.system('clear')
	menu()
## Si corto la ejecución con Ctrl + C, no veo el Traceback
except (KeyboardInterrupt):
	print('\n\n>> Programa finalizado.')
