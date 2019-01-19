import ctypes

import serial
import time
import datetime
import paramiko

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


def disable_paging(ser):
    '''Disable paging on a Cisco router'''
    ser.write("end\r\n")
    ser.write("terminal length 0\r\n")
    time.sleep(1)
    output = ser.read(MAX_BUFFER)
    ser.write("\r\n")

def login_com(puerto):
    try:

        ser = serial.Serial()
        print(ser)

        print("aqui se cayo1")
        ser.port = puerto #puerto debe ser COM1 o lo que sea
        print("aqui se cayo2")

        print(ser)
        ser.baudrate = 96000
        ser.bytesize = serial.EIGHTBITS
        ser.parity = serial.PARITY_NONE
        ser.stopbits = serial.STOPBITS_ONE
        ser.timeout = 0
        ser.writeTimeout = 1
        ser.open()
        print("yaaaaaaaaaaaaa")
        return ser
    except Exception:
        print("Conexión por consola sin éxito")
        return ""

def back_home(ser):
    ser.write("\r\n".encode())
    time.sleep(1)
    output = (ser.read(MAX_BUFFER)).decode()
    if('config' in output):
        ser.write("end\r\n")
        time.sleep(1)
        output = (ser.read(MAX_BUFFER)).decode()

def config_dir(ser,interfaces, IPs, masks):
    ser.write("conf t\r\n")
    ser.write("int " + interfaces + "\r\n")
    ser.write("ip add " + IPs + " " + masks + "\r\n")
    ser.write("no sh\r\n")
    ser.write("do wr\r\n")
    time.sleep(1)
    back_home(ser)
def read_serial(console):
    '''
    Check if there is data waiting to be read
    Read and return it.
    else return null string
    '''
    data_bytes = console.inWaiting()
    if data_bytes:
        return console.read(data_bytes)
    else:
        return ""

def send(console, cmd=''):
    '''
    Send a command down the channel
    Return the output
    '''
    console.write(cmd + '\r\n')
    time.sleep(1)
    return read_serial(console)

def conf_plantilla(ser, hostname, domain_name, dns1, dns2):
    print("ESTOY AQUI")

    ser.write(("sh ip int b\r\n"))
    print(1)
    """print(1)
time.sleep(1)
print(ser.read(MAX_BUFFER).decode())
ser.write(("host " + hostname + "\r\n").encode())
try:
    if (len(dns1) > 0):
        print("here 1")
        ser.write(("ip name-server " + dns1 + "\r\n").encode())
except Exception:
    ctypes.windll.user32.MessageBoxW(0, "DNS1 ingresada inválida", 1)
try:
    if (len(dns2) > 0):
        print("here 2")
        ser.write(("ip name-server " + dns2 + "\r\n").encode())
except Exception:
    ctypes.windll.user32.MessageBoxW(0, "DNS2 ingresada invalida",
                                     "Error", 1)
print("here 3")
ser.write(("ip domain-name " + domain_name + "\r\n" +
                 "banner motd # ACCESO SOLO A PERSONAL AUTORIZADO#" + "\r\n" +
                 "line vty 0 4" + "\r\n" +
                 "transport input all" + "\r\n" +
                 "login local" + "\r\n" +
                 "exec-timeout 3 3" + "\r\n" +
                 "logging synchronous" + "\r\n" +
                 "line console 0" + "\r\n" +
                 "transport output all" + "\r\n" +
                 "login local" + "\r\n" +
                 "exec-timeout 3 3" + "\r\n" +
                 "logging synchronous" + "\r\n" +
                 "do wr" + "\r\n").encode())
print("here 4")
time.sleep(1)"""
    print(ser.read(MAX_BUFFER))
    back_home(ser)
    print("here 5")

def conf_credencial(ser,user,password,privilegio):
    print("LLEGOOO")
    try:
        ser.write("conf t" + "\r\n" +
                         "username " + user + " privilege " + privilegio + " secret " + password + '\r\n' +
                         "do wr" + '\r\n')
        time.sleep(1)
        ser.write('end\r\n')

    except Exception:
        ctypes.windll.user32.MessageBoxW(0, "Ocurrio un error",
                                         "Error", 1)

def get_dirs_red(ser):
    list_dirs_red = []
    ser.write("sh ip route connected | exclude /32\r\n")
    time.sleep(1)
    output = (ser.read(MAX_BUFFER)).decode()
    output = output.replace('\r\n', '\n').split('\n')
    for i in range(1, len(output) - 1):
        if ("connected" in output[i] and "/" in output[i]):
            line = output[i].split(" ")
            for j in range(0, len(line)):
                if ("/" in line[j]):
                    list_dirs_red.append(line[j])
                    break
    back_home(ser)
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

def get_ip_interfaz(ser):
    info_interfaz = []
    ser.write("sh ip int b\r\n")
    time.sleep(1)
    output = (ser.read(MAX_BUFFER)).decode()
    print(output)
    output = output.replace('\r\n', '\n').split('\n')
    for i in range(2, len(output) - 1):
        line = output[i].split()
        print(line)
        interfaz = [line[0], line[4]]
        if line[4] != "up":
            interfaz[1] = "down"
        info_interfaz.append(interfaz)
    back_home(ser)

    return info_interfaz

def get_ospf_neig(ser):
    list_neig = []
    ser.write("sh ip ospf neighbor\r\n")
    time.sleep(1)
    output = (ser.read(MAX_BUFFER)).decode()
    output = output.replace('\r\n', '\n').split('\n')
    for i in range(3, len(output) - 1):
        line = output[i].split()
        list_neig.append(line[0])
    back_home(ser)
    return list_neig

def config_OSPF(ser):
    list_dirs_red = get_dirs_red(ser)
    list_wildcards = get_wildcard(list_dirs_red)
    print(list_dirs_red)
    print(list_wildcards)
    ser.write("conf t\r\n")
    ser.write("router ospf 1\r\n")
    for i in range(0, len(list_dirs_red)):
        ser.write("network " + list_dirs_red[i].split('/')[0] + " " + list_wildcards[i] + " area 0" + "\r\n")
        time.sleep(1)
    back_home(ser)

def conf_mpls_interfaces(ser):
    disable_paging(ser)
    ser.write('end\r\n')
    interfaces = get_ip_interfaz(ser)
    print(interfaces)
    ser.write("conf t\r\n")
    for i in range(0,len(interfaces)):
        if (interfaces[i][1]=="up"):
            ser.write("int "+interfaces[i][0]+"\r\n")
            ser.write("mpls ip\r\n")
    back_home(ser)

def config_cef_mpls_ldp(ser):
    ser.write("conf t\r\n")
    ser.write("ip cef\r\n")
    ser.write("mpls label protocol ldp\r\n")
    ser.write("mpls ldp router-id loopback0\r\n")
    ser.write("mpls ip\r\n")
    print("2.0")
    conf_mpls_interfaces(ser)
    time.sleep(1)
    back_home(ser)

def config_vrf(ser, name_vrf, AS, vlan):
    ser.write("conf t\r\n")
    ser.write("ip vrf "+name_vrf+"\r\n")
    ser.write("rd "+AS+":"+vlan+"\r\n")
    ser.write("route-target export "+vlan+":"+vlan+"\r\n")
    ser.write("route-target import " + vlan + ":" + vlan + "\r\n")
    back_home(ser)


def config_add_interfaz_vrf(ser, name_vrf, vlan, interfaz, ip, mascara):
    ser.write("interface "+interfaz+"\r\n")
    ser.write("no sh\r\n")
    ser.write("no mpls ip\r\n")
    ser.write("interface "+interfaz+"."+vlan+"\r\n")
    ser.write("encapsulation dot1Q "+ vlan + "\r\n")
    ser.write("ip vrf forwarding " + name_vrf + "\r\n")
    ser.write("ip add "+ip+" "+mascara+ "\r\n")
    time.sleep(1)
    back_home(ser)


def config_route_PE_CE(ser, name_vrf, red_CE, masacara_CE, int_salida):
    ser.write("conf t\r\n")
    ser.write("ip route vrf "+name_vrf+" "+red_CE+" "+masacara_CE+" "+int_salida+"\r\n")
    time.sleep(1)
    back_home(ser)


def redistribute_vrf(ser, name_vrf):
    ser.write("conf t\r\n")
    ser.write("router bgp 1\r\n")
    ser.write("address-family ipv4 vrf "+name_vrf+"\r\n")
    ser.write("redistribute static\r\n")
    ser.write("do wr\r\n")
    time.sleep(1)
    back_home(ser)


def conf_route_CE(ser, int_salida):
    ser.write("conf t\n")
    ser.write("ip route 0.0.0.0 0.0.0.0 "+int_salida+" \r\n")
    time.sleep(1)
    back_home(ser)


def config_iBGP(ser):
    bgp_neigh = get_ospf_neig(ser)
    ser.write("conf t\r\n")
    ser.write("router bgp 1\r\n")
    for i in range (0, len(bgp_neigh)):
        ser.write("neighbor "+bgp_neigh[i]+" remote-as 1\r\n")
        ser.write("neighbor " + bgp_neigh[i] + " update-source loopback0\r\n")
        ser.write("neighbor " + bgp_neigh[i] + " next-hop-self\r\n")
        ser.write("no auto-summary\r\n")
    time.sleep(1)
    back_home(ser)


def config_MP_BGP(ser):
    bgp_neigh = get_ospf_neig(ser)
    ser.write("conf t\r\n")
    ser.write("router bgp 1\r\n")
    ser.write("address-family vpnv4\r\n")
    for i in range(0, len(bgp_neigh)):
        ser.write("neighbor " + bgp_neigh[i] + " activate\r\n")
        ser.write("neighbor " + bgp_neigh[i] + " send-community extended\r\n")
    time.sleep(1)
    back_home(ser)


def show_res(ser):
    ser.write("show vrf\r\n")
    time.sleep(1)
    output = (ser.recv(MAX_BUFFER)).decode()
    back_home(ser)
    return output