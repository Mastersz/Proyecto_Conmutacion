import sqlite3

"""Script individual, al ser corrido se actualiza la tabla de usuarios y contraseñas del aplicativo. Reemplazar en los
campos ‘USUARIO’ ‘PRIVILEGIO’ ‘CONTRASENA’ por las credenciales de la persona que desea agregar a la base de datos."""
def createTable():
    connection = sqlite3.connect('login.db')



    connection.execute("INSERT INTO USERS VALUES(?,?,?)",('carlos','15','carlos'))

    connection.commit()

    result = connection.execute("SELECT * FROM USERS")
    
    for data in result:
        print("Username : ",data[0])
        print("Privilegio : ",data[1])
        print("Password :",data[2])

    connection.close()

createTable()
        
    
