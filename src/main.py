import pytest

#Validacion de fecha
def ValFecha(mes, dia):

    anio = 2025
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        meses[1] += 1


    if type(mes) == int and type(dia) == int:
        if (1 <= mes <= 12):

            dias_mes_actual = meses[(mes - 1)]

            if (1 <= dia <= dias_mes_actual):
                fecha = mes*100 + dia

                if fecha >= 625:
                    return True
                
                elif 101 <= fecha < 625:
                    with pytest.raises(Exception) as excinfo:
                        assert str(excinfo.value) == "Fecha válida pero expirada"
                    return True
                else:
                    return False
            return False
        return False
    return False

#################################

dominio = ["gmail.com","yahoo.com","hotmail.com"]

def ValCorreo(correo):

    if type(correo) != str:
        return False

    partes = correo.split("@")
    if len(partes) != 2:
        return False

    if partes[1] not in dominio:
        return False

    return type(correo) == str and len(correo.split("@")) == 2 and partes[1] in dominio

#######################################################

def ValContrasena(contrasena):

    if type(contrasena) != str:
        return False

    cantidad = len(contrasena)
    if cantidad < 12 or cantidad > 30:
        return False

    mayus = False
    minus = False
    numer = False

    for i in range(len(contrasena)):
        if contrasena[i].isnumeric():
            numer = True
        if contrasena[i].isupper():
            mayus = True
        if contrasena[i].islower():
            minus = True
    if numer and mayus and minus:
        return True
    else:
        return False

##############################

def ValUsuario(usuario, contraseña):
        usuarios_validos = {"usuario1": "Amarillo123", "usuario2": "durAzno456"}
        return usuario in usuarios_validos and usuarios_validos[usuario] == contraseña