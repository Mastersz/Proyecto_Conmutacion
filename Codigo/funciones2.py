import ctypes

import serial
import time
import datetime
import paramiko


MAX_BUFFER = 65535
"""Permite obtener la hora y fecha del sistema en cadena de texto."""
def obtener_FechaYHora():
    info=datetime.datetime.now()
    fecha=str(info.day)+"-"+str(info.month)+"-"+str(info.year)
    if info.minute<10:
        minutos="0"+str(info.minute)
    else:
        minutos=str(info.minute)
    if info.second<10:
        segundos="0"+str(info.second)
    else:
        segundos=str(info.second)
    if info.hour<10:
        horas="0"+str(info.hour)
    else:
        horas=str(info.hour)
    hora=horas+"H"+minutos+"M"+segundos+"S"
    return fecha,hora

"""Permite inicializar una conexión por SSH utilizando la librería paramiko, dado por parámetro una dirección IP de
alguna de las interfaces del dispositivo, un usuario y contraseña correspondiente a una credencial de acceso para este
tipo de conexión del dispositivo objetivo. Se retorna dos objetos llamados remote_conn_pre y remote_conn, este último
es el que permite la interacción con la CLI de los dispositivos y es el que se envía por parámetro en todas las funciones
que interactúen con la CLI del dispositivo que se este configurando."""
def login_ssh(IP, username, password):
    # Crea instancia de un cliente SSH.
    remote_conn_pre = paramiko.SSHClient()
    # Agrega automáticamente hosts no confiables(asegúrese de que esté bien para la política de seguridad en su entorno).
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Inicia conexión SSH.
    remote_conn_pre.connect(IP, username=username, password=password, look_for_keys=False, allow_agent=False)
    # Permite una conexión interactiva con el host.
    remote_conn = remote_conn_pre.invoke_shell()
    # Leer 1000 bytes de la salida actual del host.
    output = remote_conn.recv(MAX_BUFFER)
    return remote_conn_pre, remote_conn

"""Permite eliminar cualquier texto adicional que se encuentre en la CLI del dispositvo en el que se encuentre haciendo
conexión SSH, de forma que se pueda leer la última parte del texto de la CLI con la que se interactúe."""
def disable_paging(remote_conn):
    '''Disable paging on a Cisco router'''
    remote_conn.send("terminal length 0\r\n")
    while(not remote_conn.recv_ready()):
        time.sleep(0.5)
    output = (remote_conn.recv(MAX_BUFFER)).decode()

"""Permite volver al modo de configuración privilegiado, con lo que se evita posibles malas configuraciones por
encontrarse en el modo de configuración incorrecto."""
def back_home(remote_conn):
    remote_conn.send("\n")
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)
    output = (remote_conn.recv(MAX_BUFFER)).decode()
    print(output)
    if('config' in output):
        remote_conn.send("end\n")
        remote_conn.send("\n")
        while (not remote_conn.recv_ready()):
            time.sleep(0.5)
        output = (remote_conn.recv(MAX_BUFFER)).decode()
        print("sal")

"""Permite leer todas las credenciales de acceso para el protocolo SSH del router objetivo, devolviendo una cadena
de texto con la información del nombre de usuario de dichas credenciales."""
def sh_usernames(remote_conn):
    list_users = ""
    remote_conn.send("show start | include username\n")
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)
    output = (remote_conn.recv(MAX_BUFFER)).decode()
    output = output.replace('\r\n', '\n').split('\n')
    print(output)
    for i in range(1, len(output) - 1):
        line = output[i].split(" ")
        if ("username" in line[0]):
            list_users += (line[1] + "\n")
    print("\n" + list_users)
    return list_users

"""Permite agregar la importación de rutas de una nueva VRF, de forma que se permita la comunicación entre dispositivos
de distintas VRF."""
def add_import(remote_conn, name_vrf, vlan):
    if(vlan.isnumeric()):
        remote_conn.send("conf t\n")
        remote_conn.send("ip vrf " + name_vrf + "\n")
        remote_conn.send("route-target import " + vlan + ":" + vlan + "\n")
        while (not remote_conn.recv_ready()):
            time.sleep(0.5)
        output = (remote_conn.recv(MAX_BUFFER)).decode()
        output = output.replace('\r\n', '\n')
        print("/////")
        print(output)
        if "please configure" in output:
            ctypes.windll.user32.MessageBoxW(0, "La VRF ingresada no tiene un route distinguisher asignado",
                                         "Error", 0)
        else:
            ctypes.windll.user32.MessageBoxW(0, "Configuración realizada con éxito",
                                             "Done", 0)
        back_home(remote_conn)
    else:
        ctypes.windll.user32.MessageBoxW(0, "VLAN incorrecta",
                                         "Error", 0)

"""Permite configurar el direccionamiento en una interfaz, dado la interfaz, la dirección IP y la
máscara de subred por parámetro para realizar esta configuración."""
def config_dir(remote_conn,interfaces, IPs, masks):
    remote_conn.send("conf t\n")
    remote_conn.send("int "+interfaces+ "\n")
    remote_conn.send("ip add "+IPs+" "+masks+ "\n")
    remote_conn.send("no sh\n")
    remote_conn.send("do wr\n")
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)
    back_home(remote_conn)

"""Permite configurar la plantilla básica de un enrutador, así como su nombre de dominio, servidores dns, hostname y
mensaje de bienvenido al conectarse al dispositivo."""
def conf_plantilla(remote_conn, hostname, domain_name, dns1, dns2):
    remote_conn.send("conf t\n")
    if(len(dns1)>0):
        remote_conn.send("ip name-server "+dns1+"\n")
    if (len(dns2)>0):
        remote_conn.send("ip name-server " + dns2+"\n")
    remote_conn.send("host "+hostname+"\n"+"ip domain-name "+domain_name+"\n"+
                "banner motd # ACCESO SOLO A PERSONAL AUTORIZADO#"+"\n"+
                "line vty 0 4"+"\n"+
                "transport input all"+"\n"+
                "login local"+"\n"+
                "exec-timeout 3 3"+"\n"+
                "logging synchronous"+"\n"+
                "line console 0"+"\n"+
                "transport output all"+"\n"+
                "login local"+"\n"+
                "exec-timeout 3 3"+"\n"+
                "logging synchronous"+"\n"+
                "do wr"+"\n")
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)
    back_home(remote_conn)

"""Permite agregar una nueva credencial de acceso SSH en un enrutador, dado un nombre de usuario, contraseña y privilegio
 de dicha credencial."""
def conf_credencial(remote_conn,user,password,privilegio):
    try:
        remote_conn.send("conf t" + "\n"+
                         "username "+user+" privilege "+privilegio+" secret "+password+'\n'+
                         "do wr" + '\n')
        while (not remote_conn.recv_ready()):
            time.sleep(0.5)
        back_home(remote_conn)
    except Exception:
        ctypes.windll.user32.MessageBoxW(0, "Ocurrio un error",
                                         "Error", 1)

"""Permite obtener todas las direcciones de red conectadas di rectamente a un enrutador, de forma que estas redes puedan
 ser anunciadas por OSPF."""
def get_dirs_red(remote_conn):
    list_dirs_red = []
    remote_conn.send("sh ip route connected | exclude /32\n")
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)
    time.sleep(3)
    output = (remote_conn.recv(MAX_BUFFER)).decode()
    output = output.replace('\r\n', '\n').split('\n')
    print(output)
    for i in range(8, len(output) - 1):
        if ("connected" in output[i] and "/" in output[i] and not("ip" in output[i])):
            line = output[i].split(" ")
            print(" OSPF")
            for j in range(0, len(line)):
                if ("/" in line[j]):
                    list_dirs_red.append(line[j])
                    break
    back_home(remote_conn)
    return list_dirs_red

"""Permite obtener las wildcards de una lista de redes dadas por parámetro."""
def get_wildcard(list_dirs_red):
    list_wildcards = []
    for k in range(0, len(list_dirs_red)):
        line = list_dirs_red[k].split('/')
        mask = 32 - int(line[1])
        wildcard = [0, 0, 0, 0]
        octeto = 3
        while (mask > 8):
            wildcard[octeto] = 2 ** 8 - 1
            octeto -= 1
            mask -= 8
        wildcard[octeto] = 2 ** mask - 1
        list_wildcards.append(
            str(wildcard[0]) + '.' + str(wildcard[1]) + '.' + str(wildcard[2]) + '.' + str(wildcard[3]))
    return list_wildcards

"""Permite obtener una lista con todas las interfaces que tiene un enrutador, esta información comprende el nombre de las
interfaces, su estado (up/down) y la dirección IP asignada a la misma."""
def get_ip_interfaz(remote_conn):
    print("int")
    back_home(remote_conn)
    info_interfaz=[]
    remote_conn.send("sh ip int b\n")
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)
    output = (remote_conn.recv(MAX_BUFFER)).decode()
    output = output.replace('\r\n', '\n').split('\n')
    for i in range(1, len(output)-1):
        line = output[i].split()
        print(line)
        if not("#" in line[0]) and "/" in line[0]:
            if(len(line[0].split("."))==1):
                interfaz = [line[0], line[4], line[1]]
                if line[4]!="up":
                    interfaz[1]="down"
                info_interfaz.append(interfaz)
    back_home(remote_conn)
    return info_interfaz

"""Permite obtener los vecinos de OSPF, lo cual permite configurar el protocolo iBGP y MP-BGP entre los dispositivos PE."""
def get_ospf_neig(remote_conn):
    loopback_rd=""
    back_home(remote_conn)
    remote_conn.send("show ip interface brief | include Loopback\n")
    time.sleep(3)
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)
    output = (remote_conn.recv(MAX_BUFFER)).decode()
    output = output.replace('\r\n', '\n').split('\n')
    for i in range(0, len(output)):
        line = output[i].split()
        if "Loopback" in line[0]:
            print(line[0])
            loopback_rd = (line[1])
    neighbors=[]
    list_neig=[]
    print("---" + loopback_rd)
    remote_conn.send("sh ip ospf database network | include Attached Router\n")
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)
    output = (remote_conn.recv(MAX_BUFFER)).decode()
    output = output.replace('\r\n', '\n').split('\n')
    for i in range(1, len(output)):
        print(output[i])
        if('Attached Router' in output[i]):
            list_neig.append((output[i].split(":"))[1])
    for j in range(0, len(list_neig)):
        dir = list_neig[j][1:]
        if not(dir in neighbors) and dir!=loopback_rd:
            neighbors.append(dir)
    print(neighbors)
    back_home(remote_conn)
    return neighbors

"""Permite configurar el protocolo OSPF en el AS 1 y en el área de backbone 0. Para esto se obtienen todas las direcciones
de redes conectadas directamente de un enrutador, posteriormente la wildcard de cada una de estas redes y son anunciadas
por el protocolo ya mencionado."""
def config_OSPF(remote_conn):
    list_dirs_red = get_dirs_red(remote_conn)
    list_wildcards = get_wildcard(list_dirs_red)
    print(list_dirs_red)
    print(list_wildcards)
    remote_conn.send("conf t\n")
    remote_conn.send("router ospf 1\n")
    for i in range(0,len(list_dirs_red)):
        remote_conn.send("network "+list_dirs_red[i].split('/')[0]+" "+list_wildcards[i]+" area 0"+"\n")
        while (not remote_conn.recv_ready()):
            time.sleep(0.5)
    back_home(remote_conn)

"""Permite habilitar mpls en todas las interfaces habilitadas (estado up) y que no sean las interfaces Loopback.
Para esto se obtiene primero todas las interfaces disponibles del enrutador con la función get_ip_interfaz."""
def conf_mpls_interfaces(remote_conn):
    back_home(remote_conn)
    interfaces = get_ip_interfaz(remote_conn)
    print(interfaces)
    remote_conn.send("conf t\n")
    for i in range(0,len(interfaces)):
        if (interfaces[i][1]=="up" and not("Loopback" in interfaces[i][0])):
            print(i)
            remote_conn.send("int "+interfaces[i][0]+"\n")
            remote_conn.send("mpls ip\n")
            remote_conn.send("exit\n")
            while (not remote_conn.recv_ready()):
                time.sleep(0.5)
    time.sleep(5)
    print("out")

"""Se configura el protocolo CEF, LDP y MPLS."""
def config_cef_mpls_ldp(remote_conn):
    remote_conn.send("conf t\n")
    remote_conn.send("ip cef\n")
    remote_conn.send("mpls label protocol ldp\n")
    remote_conn.send("mpls ldp router-id loopback0\n")
    remote_conn.send("mpls ip\n")
    print("2.0")
    conf_mpls_interfaces(remote_conn)
    back_home(remote_conn)

"""Se crea una VRF con su respectiva router distinguisher, exportación e importación de sus rutas."""
def config_vrf(remote_conn, name_vrf, AS, vlan):
    remote_conn.send("conf t\n")
    remote_conn.send("ip vrf "+name_vrf+"\n")
    remote_conn.send("rd "+AS+":"+vlan+"\n")
    remote_conn.send("route-target export "+vlan+":"+vlan+"\n")
    remote_conn.send("route-target import " + vlan + ":" + vlan + "\n")
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)

"""Se agrega una interfaz a una VRF, para lo cual se requiere el nombre de la VRF, la VLAN del cliente, la interfaz por
la que se conectará el cliente y el direccionamiento de la interfaz por donde se conectará el cliente. Esto se configura
en un dispositivo tipo PE."""
def config_add_interfaz_vrf(remote_conn, name_vrf, vlan, interfaz, ip, mascara):
    remote_conn.send("interface "+interfaz+"\n")
    remote_conn.send("no sh\n")
    remote_conn.send("no mpls ip\n")
    remote_conn.send("interface "+interfaz+"."+vlan+"\n")
    remote_conn.send("encapsulation dot1Q "+ vlan + "\n")
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)
    remote_conn.send("ip vrf forwarding " + name_vrf + "\n")
    remote_conn.send("ip add "+ip+" "+mascara+ "\n")
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)
    back_home(remote_conn)

"""Permite configurar una ruta que le permite comunicarse por su respectiva cliente a un cliente, recibiendo como parámetro
el nombre de la VRF y la red de la LAN del cliente."""
def config_route_PE_CE(remote_conn, name_vrf, red_CE, mascara_CE, int_salida):
    remote_conn.send("conf t\n")
    remote_conn.send("ip route vrf "+name_vrf+" "+red_CE+" "+mascara_CE+" "+int_salida+"\n")
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)
    back_home(remote_conn)

"""Permite redistribuir las rutas aprendidas de un dispositivo CE por las rutas estáticas, al proceso MP-BGP usando el
address-family de la respectiva VRF dada por parámetro."""
def redistribute_vrf(remote_conn, name_vrf):
    remote_conn.send("conf t\n")
    remote_conn.send("router bgp 1\n")
    remote_conn.send("address-family ipv4 vrf "+name_vrf+"\n")
    remote_conn.send("redistribute static\n")
    remote_conn.send("do wr\n")
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)
    back_home(remote_conn)

"""Se configura una ruta estática que le permite comunicarse al router del cliente con su respectivo router PE. Se
desactiva el protocolo OSPF ya que se configura previamente al establecer el direccionamiento en el enrutador."""
def conf_route_CE(remote_conn, ip_salida):
    remote_conn.send("conf t\n")
    remote_conn.send("no router ospf 1\n")
    remote_conn.send("ip route 0.0.0.0 0.0.0.0 "+ip_salida+" \n")
    remote_conn.send("do wr\n")
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)
    back_home(remote_conn)

"""Permite configurar el protocolo iBGP entre los dispositivos PE. Para esto, se lee las ip de loopback de los dispositivos P
con la función read_file de un archivo de texto, ya que se agregará como vecinos iBGP a los vecinos OSPF, siendo los dispositivos
P vecinos OSPF pero no pueden ser vecinos iBGP. Por lo que de esta manera se evita establecer a un dispositivo P como vecino iBGP."""
def config_iBGP(remote_conn):
    bgp_neigh = get_ospf_neig(remote_conn)
    rd_p = read_file()
    remote_conn.send("conf t\n")
    remote_conn.send("router bgp 1\n")
    for i in range (0, len(bgp_neigh)):
        if not(bgp_neigh[i] in rd_p):
            remote_conn.send("neighbor "+bgp_neigh[i]+" remote-as 1\n")
            remote_conn.send("neighbor " + bgp_neigh[i] + " update-source loopback0\n")
            remote_conn.send("neighbor " + bgp_neigh[i] + " next-hop-self\n")
            remote_conn.send("no auto-summary\n")
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)
    back_home(remote_conn)

"""Permite configurar el protocolo MP-BGP entre los dispositivos PE. Para esto, se lee las ip de loopback de los dispositivos P
con la función read_file de un archivo de texto, ya que se agregará como vecinos MP-BGP a los vecinos OSPF, siendo los dispositivos P 
vecinos OSPF, pero no pueden ser vecinos MP-BGP. Por lo que de esta manera se evita establecer a un dispositivo P como vecino MP-BGP."""
def config_MP_BGP(remote_conn):
    bgp_neigh = get_ospf_neig(remote_conn)
    rd_p = read_file()
    remote_conn.send("conf t\n")
    remote_conn.send("router bgp 1\n")
    remote_conn.send("address-family vpnv4\n")
    print("en BGP ")
    print(bgp_neigh)
    for i in range(0, len(bgp_neigh)):
        if not (bgp_neigh[i] in rd_p):
            remote_conn.send("neighbor " + bgp_neigh[i] + " activate\n")
            remote_conn.send("neighbor " + bgp_neigh[i] + " send-community extended\n")
            while (not remote_conn.recv_ready()):
                time.sleep(0.5)
    remote_conn.send("exit-address-family\n")
    remote_conn.send("end\n")
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)
    back_home(remote_conn)

"""Permite obtener la salida del comando show vrf, el cual es mostrado si se realiza con éxito toda la configuración
correspondiente a un enrutador tipo PE."""
def show_res(remote_conn):
    copy = False
    salida = ""
    remote_conn.recv(1000)
    remote_conn.send("show vrf\n")
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)
    time.sleep(1)
    output = (remote_conn.recv(MAX_BUFFER)).decode()
    output = output.split('\r\n')
    for i in range(0, len(output)):
        if("show vrf" in output[i]):
            copy = True
        if (copy == True):
            salida+=(output[i]+"\r\n")
    print("iiii")
    print(output)
    return salida

"""Permite guardar en un archivo de texto la dirección ip de la interfaz loopback de un enrutador, esto se hace en los P
y es considerado en la configuración de los protocolos iBGP y MP-BGP como ya se explicó en sus respectivas funciones de configuración."""
def save_ID(remote_conn):
    back_home(remote_conn)
    remote_conn.send("show ip interface brief | include Loopback\n")
    while (not remote_conn.recv_ready()):
        time.sleep(0.5)
    output = (remote_conn.recv(MAX_BUFFER)).decode()
    output = output.replace('\r\n', '\n').split('\n')
    for i in range(0,len(output)):
        line = output[i].split()
        if "Loopback" in line[0]:
            write_file(line[1])
    back_home(remote_conn)

"""Permite escribir en el archivo de texto rd_p.txt la información dada por parámetro, la cual corresponde a la dirección IP
de loopback de un enrutador tipo P."""
def write_file(dir_id):
    archivo = open('rd_P.txt', 'a')
    archivo.write(dir_id+'\n')
    archivo.close()

"""Permite leer el archivo rd_p.txt, obteniendo así la dirección IP de loopback de todos los enrutadores tipo P de la red."""
def read_file():
    rd_p = []
    archivo = open('rd_P.txt', 'r')
    lines = archivo.readlines()
    for i in range (0, len(lines)):
        rd_p.append(lines[i][:-1])
    print(rd_p)
    return rd_p