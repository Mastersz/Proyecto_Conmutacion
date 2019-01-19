import time
import datetime
import paramiko
import serial

MAX_BUFFER = 65535
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

def disable_paging(remote_conn):
    '''Disable paging on a Cisco router'''
    remote_conn.send("terminal length 0\r\n")
    time.sleep(1)
    output = (remote_conn.recv(MAX_BUFFER)).decode()

def back_home(remote_conn):
    remote_conn.send("\n")
    time.sleep(1)
    output = (remote_conn.recv(MAX_BUFFER)).decode()
    if('config' in output):
        remote_conn.send("end\n")
        time.sleep(1)
        output = (remote_conn.recv(MAX_BUFFER)).decode()

def config_dir(remote_conn,interfaces, IPs, masks):
    remote_conn.send("conf t\n")
    remote_conn.send("int "+interfaces+ "\n")
    remote_conn.send("ip add "+IPs+" "+masks+ "\n")
    remote_conn.send("no sh\n")
    remote_conn.send("do wr\n")
    time.sleep(1)
    back_home(remote_conn)

def get_dirs_red(remote_conn):
    list_dirs_red = []
    remote_conn.send("sh ip route connected | exclude /32\n")
    time.sleep(1)
    output = (remote_conn.recv(MAX_BUFFER)).decode()
    output = output.replace('\r\n', '\n').split('\n')
    for i in range(1, len(output) - 1):
        if ("connected" in output[i] and "/" in output[i]):
            line = output[i].split(" ")
            for j in range(0, len(line)):
                if ("/" in line[j]):
                    list_dirs_red.append(line[j])
                    break
    return list_dirs_red

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


def get_ip_interfaz(remote_conn):
    info_interfaz=[]
    remote_conn.send("sh ip int b\n")
    time.sleep(1)
    output = (remote_conn.recv(MAX_BUFFER)).decode()
    output = output.replace('\r\n', '\n').split('\n')
    for i in range(2, len(output)-1):
        line = output[i].split()
        interfaz = [line[0], line[4]]
        if line[4]!="up":
            interfaz[1]="down"
        info_interfaz.append(interfaz)
    print(info_interfaz)
    return info_interfaz

def config_OSPF(remote_conn):
    list_dirs_red = get_dirs_red(remote_conn)
    list_wildcards = get_wildcard(list_dirs_red)
    print(list_dirs_red)
    print(list_wildcards)
    remote_conn.send("conf t\n")
    remote_conn.send("router ospf 1\n")
    for i in range(0,len(list_dirs_red)):
        remote_conn.send("network "+list_dirs_red[i].split('/')[0]+" "+list_wildcards[i]+" area 0"+"\n")
        time.sleep(1)
    back_home(remote_conn)

def config_cef_mpls_ldp(remote_conn):
    remote_conn.send("conf t\n")
    remote_conn.send("ip cef\n")
    remote_conn.send("mpls label protocol ldp\n")
    remote_conn.send("mpld ldp router-id loopback0\n")
    remote_conn.send("mpls ip\n")
    time.sleep(1)
    back_home(remote_conn)

def config_vrf(remote_conn,name_vrf, AS, vlan):
    remote_conn.send("conf t\n")
    remote_conn.send("rd "+AS+":"+vlan+"\n")
    remote_conn.send("route-target export "+vlan+":"+vlan+"\n")
    remote_conn.send("route-target import " + vlan + ":" + vlan + "\n")
    #llamar a config_add_interfaz_vrf si se desea

def config_add_interfaz_vrf(remote_conn, name_vrf, vlan, interfaz, ip, mascara):
    remote_conn.send("interface "+interfaz+"\n")
    remote_conn.send("no sh\n")
    remote_conn.send("interface "+interfaz+"."+vlan+"\n")
    remote_conn.send("encapsulation dot1Q "+ vlan + "\n")
    remote_conn.send("ip vrf forwarding " + name_vrf + "\n")
    remote_conn.send("ip add "+ip+" "+mascara+ "\n")
    time.sleep(1)
    back_home(remote_conn)

def config_route_PE_CE(remote_conn, name_vrf, red_CE, masacara_CE, int_salida):
    remote_conn.send("conf t\n")
    remote_conn.send("ip route "+name_vrf+" "+red_CE+" "+masacara_CE+" "+int_salida+"\n")
    time.sleep(1)
    back_home(remote_conn)

def redistribute_vrf(remote_conn, name_vrf):
    remote_conn.send("conf t\n")
    remote_conn.send("router bgp 1\n")
    remote_conn.send("address-family ipv4 vrf "+name_vrf+"\n")
    remote_conn.send("redistribute static\n")
    time.sleep(1)
    back_home(remote_conn)

def conf_route_CE(remote_conn, int_salida):
    remote_conn.send("conf t\n")
    remote_conn.send("ip route 0.0.0.0 0.0.0.0 "+int_salida+"\n")
    time.sleep(1)
    back_home(remote_conn)

def config_iBGP(remote_conn):
    bgp_neigh = []
    remote_conn.send("conf t\n")
    remote_conn.send("router bgp 1\n")
    for i in range (0, len(bgp_neigh)):
        remote_conn.send("neighbor "+bgp_neigh[i]+" remote-as 1\n")
        remote_conn.send("neighbor " + bgp_neigh[i] + " update-source loopback0\n")
        remote_conn.send("neighbor " + bgp_neigh[i] + " next-hop-self\n")
        remote_conn.send("no auto-summary\n")
    time.sleep(1)
    back_home(remote_conn)

def config_MP_BGP(remote_conn):
    bgp_neigh = []
    remote_conn.send("conf t\n")
    remote_conn.send("router bgp 1\n")
    remote_conn.send("address-family vpnv4\n")
    for i in range(0, len(bgp_neigh)):
        remote_conn.send("neighbor " + bgp_neigh[i] + " activate\n")
        remote_conn.send("neighbor " + bgp_neigh[i] + " send-community extended\n")
    time.sleep(1)
    back_home(remote_conn)


"""remote_conn_pre,remote_conn = login_ssh("192.168.2.2","admin","admin")
disable_paging(remote_conn)
back_home(remote_conn)
get_ip_interfaz(remote_conn)
remote_conn_pre.close()"""