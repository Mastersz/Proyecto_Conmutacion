import sqlite3

"""Script individual, al ser corrido se actualiza la tabla de usuarios y contraseñas del aplicativo. Reemplazar en los
campos ‘USUARIO’ ‘PRIVILEGIO’ ‘CONTRASENA’ por las credenciales de la persona que desea agregar a la base de datos."""
def createTable():
    connection = sqlite3.connect('DataBase.db')



    connection.execute("INSERT INTO USERS VALUES(?,?)",('day','admin'))

    connection.commit()

    result = connection.execute("SELECT * FROM user")
    
    for data in result:
        print("username : ",data[0])
        print("password : ",data[1])

    connection.close()

createTable()
        
    
