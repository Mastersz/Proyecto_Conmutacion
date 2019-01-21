import sqlite3

'''
Buscar en la base de datos
Necesita la conexion con base de datos, tabla a buscar, y si es necesario una condicion.
Si la condicion no se especifica, regresara todos los campos.
Regresa el resutado de la busqueda en forma de lista 
'''
def buscar_bd(bd, tabla, condicion='1=1'):
	cursor = bd.cursor()
	sentencia = "SELECT * FROM "+tabla+" WHERE "+ condicion +";"
	cursor.execute( sentencia )
	resultado = cursor.fetchall()

	return resultado


'''
Verificar contrasenia de usuario
Utlizamos la funcion buscar_bd() para buscar al usuario.
Si el resultado es 0, entonces no se encuentra el usuario en la base de datos
En caso de que exista, se verifica si las contrasenias son iguales.
'''
def verificarCredenciales(bd, usuario, contrasenia):
    resultado = buscar_bd(bd, "user", "username='" + usuario + "'")
    if usuario == '' or contrasenia == '':
        return 2
    elif (len(resultado) == 0):
        return 0
    else:
        usuario = resultado[0]
        if (str(usuario[3]) == contrasenia):
            return 1
        else:
            return 3

'''
Escribir en Base de Datos
Necesita la conexion con base de datos, tabla a escribir 
'''
def historial_bd(bd,inf):
    c = bd.cursor()
    insert = ''' INSERT INTO historial(usuario,hora_fecha,dispositivo,evento)
	                                              VALUES(?,?,?,?) '''
    c.execute(insert, inf)
    bd.commit()
    return "Regristro realizado"