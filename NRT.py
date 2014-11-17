#!/usr//bin/python
# -*- coding: utf-8 -*-

import os

def repararMBR():
	try:
		print('>> Intentando restaurar el MBR del disco, aguarde un momento...\n')
		os.system('dd if=iso/grub-n201.iso of=/dev/sda bs=512 count=1 &> /dev/null/')
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
		os.system('cp src/grub/grub.cfg /mnt/boot/grub/')
		print('\n>> Se restauraron correctamente los parámetros de arranque del GRUB.')
		os.system('umount /dev/sda1')
		print('--> La partición (sda1) se desmontó correctamente.')
	except:
		print('>> ERROR. No se pudo copiar la configuración del GRUB al directorio destino.')
	input('\n>> Presione ENTER para continuar... \n')
	os.system('clear')
	return


def runCheck():
	try: ## VERIFICAR CON FSCK PARTICION DE RECU
		print('>> Chequeando integridad de la partción de recuperación...')
		os.system('fsck -a /dev/sda5')
		print('\n >> El sistema de archivos ha sido reparado.')
	except:
		print('>> ERROR. No se pudo realizar la verificación del sistema de archivos.')
	input('\n>> Presione ENTER para continuar... \n')
	os.system('clear')
	


def quitarPass(model):
	try:
		print('--> Intentando montar partición de Windows en /mnt...\n')
		if (model == '2013'):
			os.system('mount /dev/sda2 /mnt')
			print('--> Partición de Windows (sda2) montada correctamente.\n')
		elif (model == '2014'):
			os.system('mount /dev/sda5 /mnt')
			print('--> Partición de Windows (sda5) montada correctamente.\n')
		else:
			pass
		os.system('mv /mnt/Windows/System32/sethc.exe /mnt/Windows/System32/sethc.exe-BAK')
		print('--> Backup de "sethc.exe" creado correctamente.\n')
		os.system('cp /mnt/Windows/System32/cmd.exe /mnt/Windows/System32/sethc.exe')
		print('--> Los archivos correspondientes de modificaron correctamente.\n')
		if (model == '2013'):
			os.system('umount /dev/sda2')
		elif (model == '2014'):
			os.system('umount /dev/sda5')
		print('--> La partición de Windows se desmontó correctamente.')
		print('>>> Ya puede arrancar el SO Windows y al momento de iniciar sesión, presione 5 veces la tecla Mayus. En la Terminal CMD teclee lo siguiente:\n')
		print('# control userpasswords2\n')
	except:
		print('>> ERROR. No fue posible modificar los archivos necesarios.')
	input('\n>> Presione ENTER para continuar... \n')
	os.system('clear')
	return

def verifReboot():
	resp = str(input('\n>>> Está seguro de que desea reinciar?: [s/n]:'))
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


def evalSeguridad():
	resp = str(input('\n>> ¿Está seguro de haber seleccionado el modelo correcto? [s/n]: '))
	resp = resp.lower()
	if (resp == 's'):
		return True
	elif (resp == 'n'):
		return False
	while (resp != 's') or (resp != 'n'):
		if (resp == 's'):
			return True
		elif (resp == 'n'):
			return False
		else:
			resp = str(input('\n>> Sólo puede responder con "s" o "n", inténtelo nuevamente: '))
			resp = resp.lower()


def quitarCargador():
	try:
		print('--> Montando la partición de Recuperación (sda6)')
		os.system('mount /dev/sda6 /mnt/')
		print('--> Eliminando archivos duplicados...')
		os.system('rm -f /mnt/root/*.sh')
		print('--> Copiando archivos modificados...')
		os.system('cp src/restore/* /mnt/root/')
		print('--> Archivos copiados correctamente.')
		print('--> Desmontando partición de Recuperación.')
		os.system('umount /dev/sda6')
		print('--> Partición desmontada correctamente')
	except:
		print('>> ERROR. No fue posible modificar los archivos necesarios.')
	input('\n>> Presione ENTER para continuar... \n')
	os.system('clear')
	return



def menu(model):
	if (model == '2013'):
		os.system('clear')
		print('################# NETBOOK RECOVERY TOOL #################')
		print('################## NETBOOK MODELO 2013 ##################\n')
		print('\t1. Reparar imágen de GRUB en /dev/sda.')
		print('\t2. Restaurar configuración de GRUB.')
		print ('\t3. Verificar integridad de Partición de Recuperación.')
		print('\t4. Preparar reseteo de contraseña de Windows 7.')
		print('\t0. Menú anterior')
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
				quitarPass(model)
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
			print('\t0. Menú anterior.')
			print('\tR. Reiniciar')
			print()
			option = str(input('>> Opcion deseada: '))
	
	elif (model == '2014'):
		os.system('clear')
		print('################# NETBOOK RECOVERY TOOL #################')
		print('################## NETBOOK MODELO 2014 ##################\n')
		print('\t1. Preparar reseteo de contraseña de Windows 8.1.')
		print('\t2. Quitar verificación de cargador en sistema de restauración.')
		print('\t0. Menú anterior')
		print('\tR. Reiniciar')
		option = str(input('>> Opcion deseada: '))

		while (option != '0'):
			## Evaluo las opciones
			print()
			if (option == '1'):
				quitarPass(model)
			elif (option == '2'):
				quitarCargador()
			elif (option == 't'):
				print ('TEST OK')
				fun()
			else:
				print('>> ERROR. El carácter ingresado no es una opción válida.')
				os.system('clear')

			print('################# NETBOOK RECOVERY TOOL#################\n')
			print('\t1. Preparar reseteo de contraseña de Windows 8.1')
			print('\t0. Menú anterior.')
			print('\tR. Reiniciar')
			print()
			option = str(input('>> Opcion deseada: '))
	else:
		pass

	## Si ingresa 0, termina el programa.
		if (option == '0'):
			os.system('clear')
		if (option == 'R') | (option == 'r'):
			reboot(verifReboot())


def selectModel():
	print('################# NETBOOK RECOVERY TOOL#################')
	print('>> ¿Con qué modelo de netbook desea trabajar?\n')
	print('\t1. Modelo 2013 [Intel Atom N2600 + 2Gb]')
	print('\t2. Modelo 2014 [Intel Celeron N2806 + 4Gb]')
	print('\tQ. Salir')

	option = str(input('\n>> Opción deseada: '))
	option = option.lower()

	while (option != 'q'):
		if( option == '1'):
			#if (evalSeguridad() == True):
			model = str(2013)
			menu(model)
			#else:
			#	input('\n>> Presione ENTER y seleccione el modelo correcto...')
			#	os.system('clear')
		elif (option == '2'):
			#if (evalSeguridad() == True):
			model = str(2014)
			menu(model)
			#else:
			#	input('\n>> Presione ENTER y seleccione el modelo correcto...')
			#	os.system('clear')
		elif (option == 't'):
			print('>> TEST OK')
			fun()
		else:
			input('\n>> El caracter ingresado no es una opción válida, por favor inténtelo de nuevo...')
			os.system('clear')

		print('################# NETBOOK RECOVERY TOOL#################')
		print('>> ¿Con qué modelo de netbook desea trabajar?\n')
		print('\t1. Modelo 2013 [Intel Atom N2600 + 2Gb]')
		print('\t2. Modelo 2014 [Intel Celeron N2806 + 4Gb]')
		print('\tQ. Salir')

		option = str(input('\n>> Opción deseada: '))
		option = option.lower()

	if (option == 'q'):
		input('>> Presione una tecla para salir...')


## Programa principal
try:
	os.system('clear')
	selectModel()
## Si corto la ejecución con Ctrl + C, no veo el Traceback
except (KeyboardInterrupt):
	print('\n\n>> Programa finalizado.')
