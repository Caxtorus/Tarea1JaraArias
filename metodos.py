def check_char(x):
    # metodo que retorna 0 si el valor ingresado es un solo caracter y este se
    # encuentra entre el rango a-z o A-Z o retorna un codigo de error unico:
    # Error 400: recibe mas de un caracter dentro de los rangos A-Z y a-z
    # Error 404: recibe uno o mas caracteres fuera de los rangos A-Z y a-z
    # Error 502: recibe un tipo de dato diferente de "char"/"string"
    # Se compara el tipo de dato ingresado. Si este es diferente de un string
    # retorna el codigo de error 502
    if isinstance(x, str):
        # Concatena, en un string,el codigo ascii de cada dato introducido y lo
        # convierte en entero
        x1 = int(''.join(str(ord(z)) for z in x))

        # Se compara si el caracter introducido se encuentra entre el rango A-Z
        # o a-z y además que sea un solo caracter. si se introduce mas de un
        # caracter se procede a realizar la comparacion para retornar el codigo
        # de error correspondiente
        if (65 <= x1 and x1 <= 90) or (97 <= x1 and x1 <= 122):
            # Se retorna 0 cuando el valor ingresado es un solo caracter y se
            # encuentra entre el rango A-Z o a-z
            return 0
        else:
            largo = len(x)  # Se determina el largo de la entrada
            # Se comparan uno a uno los caracteres de lla entrada revisando si
            # se encuentran o no dentro del rango, cuando se encuentra un
            # caracter que no pertenezca al rango se retorna el codigo de
            # error 404, si por el contrario no se encuentra ningun caracter
            # fuera del rango se retorna el codigo de error 400
            for i in range(0, largo):
                temp = ord(x[i])
                if (65 > temp) or (temp > 90 and 97 > temp) or (temp > 122):
                    return 404
            return 400
    else:
        return 502


def caps_switch(character):
    # metodo que recibe un parametro y verifica si es un caracter dentro del
    # rango A-Z o a-z. Si este se encuentra en este rango se convierte de
    # minuscula a mayuscula o viceversa; en cambio si no es un único valor o
    # no se encuentra dentro de los rangos establecidos retorna un codigo de
    # error unico, determinado por el metodo check_char()

    # recibe un codigo al evaluar la entrada con el metodo check_char()
    verification = check_char(character)
    # comprueba si se paso un único caracter dentro del rango establecido
    if verification == 0:
        # convierte de minuscula a mayuscula o viceversa el caracter
        character_swithed = character.swapcase()
        return character_swithed  # retorna el caracater invertido
    else:
        # retorna el codigo de error generado por check_char()
        return verification
