#!/usr/bin/python3
''' comment '''


if __name__ == "__main__":

    from sys import argv
    import MySQLdb
    MY_H = "localhost"
    MY_U = argv[1]
    MY_P = argv[2]
    MY_D = argv[3]
    nuevaconexion = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    consulta = nuevaconexion.cursor()
    consulta.execute("SELECT * FROM states ORDER BY state.id ascending")
    resultado = consulta.fetchall()
    for fila in resultado:
        print(fila)
    nuevaconexion.close()
