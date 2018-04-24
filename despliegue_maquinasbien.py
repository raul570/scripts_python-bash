import os, sys, shlex, subprocess, commands
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--maquina",
        required=True, help="Nombre de la maquina")
parser.add_argument("-op", "--opcion",
        required=True, help="Opcion a realizar")
parser.add_argument("-p", "--puertossh",
        required=True, help="Puerto SSH deseado")
args = parser.parse_args()

maquina = args.maquina
opcion = args.opcion
puertossh = args.puertossh

if os.geteuid() != 0:
    print 'Debes tener privilegios root para este script.'
    sys.exit(1)
else:
    print 'Bienvenido usuario root'
    t =  args.maquina
    print ('El nombre de la maquina es: ' + t)
    c = args.opcion
    print "Has elegido ", c
    print "Opciones a realizar: 1.Crear usuarios, 2. Generar claves"
    miArray = ["juanan","alberto","raul","guille","jose"]
    if (c=="1"):
        #INSTALAR SSH
        os.system('apt-get install ssh -y > /dev/null')
        print 'SSH ya esta o estaba instalado'
        #SUSTITUIR

        ###################################################
        ####El programa de pedir el nuevo puerto de ssh####
        ###################################################
        puerto = args.puertossh
        os.system("sed -i s/22/" + puerto + "/g /etc/ssh/sshd_config > /dev/null")
        os.system("sed -i s/#Port/Port/g /etc/ssh/sshd_config > /dev/null")
        print "Puerto sustituido y linea descomentada"
        #REINICIAR SSH
        os.system('/etc/init.d/ssh start')
        print 'El servicio SSH a sido reiniciado e inicializado'
        #CREACION DE USUARIOS CON ARRAY
        for i in miArray:
            os.system('useradd -m -p pa3GrE2eHuydo -s /bin/bash ' + i)
            with open('/etc/sudoers', 'a') as file:
                file.write(i + " ALL=(ALL:ALL) ALL\n")
            print ("Usuario " + i + " ha sido creado")
            if(i == "juanan"):
                f = open("/home/juanan/authentication_keys","w")
                f.write( 'clave_juanan_' + t  )
                f.close()
            if(i == "alberto"):
                file = open("/home/alberto/authentication_keys","w")
                file.write( 'clave_alberto_' + t  )
                file.close()
            if(i == "raul"):
                file = open("/home/raul/authentication_keys","w")
                file.write( 'clave_raul_' + t  )
                file.close()
            if(i == "guille"):
                file = open("/home/guille/authentication_keys","w")
                file.write( 'clave_guille_' + t  )
                file.close()
            if(i == "jose"):
                file=open("/home/jose/authentication_keys", "w")
                file.write( 'clave_jose_' + t  )
                file.close()

    if (c=="2"):
        for i in miArray:
        #GENERAR CLAVES PUBLICAS
            if not os.path.exists("/home/" + i + "/.ssh"):
                os.makedirs("/home/" + i + "/.ssh")
            os.system("ssh-keygen -N GonetFPI999 -f /home/" + i + "/.ssh/id_ed25519 -t ed25519")
            os.system("sed -i 's/root/" + i + "/g' /home/" + i + "/.ssh/id_ed25519.pub")
        #GUARDAR CLAVE PUBLICA DE CADA USUARIO EN SU VARIABLE CORRESPONDIENTE
            if(i == "juanan"):

                # sh: 1: Syntax error: Unterminated quoted string
                # Traceback (most recent call last):
                # File "Escritorio/a/despliegue_maquinasbien.py", line 62, in <module>
                # file=open('/home/juanan/clave.pub','r')
                # IOError: [Errno 2] No such file or directory: '/home/juanan/clave.pub'

                file=open('/home/juanan/.ssh/id_ed25519.pub','r')
                var=file.read()
                file.close()
                f=open("/home/claves.txt","a")
                f.write('clave_juanan_' + t + '= \"' + var + '\" \n')
                f.close()
            if(i == "alberto"):
                file=open('/home/alberto/.ssh/id_ed25519.pub','r')
                var=file.read()
                file.close()
                f=open("/home/claves.txt","a")
                f.write('clave_alberto_' + t + '= \"' + var + '\" \n')
                f.close()
            if(i == "raul"):
                file=open('/home/raul/.ssh/id_ed25519.pub','r')
                var=file.read()
                file.close()
                f=open("/home/claves.txt","a")
                f.write('clave_raul_' + t + '= \"' + var + '\" \n')
                f.close()
            if(i == "guille"):
                file=open('/home/guille/.ssh/id_ed25519.pub','r')
                var=file.read()
                file.close()
                f=open("/home/claves.txt","a")
                text=f.write('clave_guille_' + t + '= \"' + var + '\"')
                f.write('\n')
                f.close()
            if(i == "jose"):
                file=open('/home/jose/.ssh/id_ed25519.pub','r')
                var=file.read()
                file.close()
                f=open("/home/claves.txt","a")
                f.write('clave_jose_' + t + '= \"' + var + '\" ')

	os.system("scp -P str(args.puertossh) root@192.168.1.153: /home/juanan/claves.txt /home")
	os.system("scp -P str(args.puertossh) root@192.168.1.153: /home/alberto/claves.txt /home")
	os.system("scp -P str(args.puertossh) root@192.168.1.153: /home/raul/claves.txt /home")
	os.system("scp -P str(args.puertossh) root@192.168.1.153: /home/guille/claves.txt /home")
	os.system("scp -P str(args.puertossh) root@192.168.1.153: /home/jose/claves.txt /home")
		#poner valor variable str para arreglar|
		#sh: 1: Syntax error: "(" unexpected 
		#sh: 1: Syntax error: "(" unexpected
		#sh: 1: Syntax error: "(" unexpected
		#sh: 1: Syntax error: "(" unexpected
		#sh: 1: Syntax error: "(" unexpected


#       os.system('scp' + args.puertossh + ' root@192.168.1.153:/#home/claves.txt root@192.168.1.184:/home/claves.txt')
		
#-------------------------------------------------------------------------------
