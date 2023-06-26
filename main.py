from random import choice

palabras = ['python', 'javascript', 'consola', 'github', 'programa']
letras_correctas = []
# para poder llevar la cuenta de letras correctas e incorrectas
letras_incorrectas = []
intentos = 6
aciertos = 0
# estos aciertos los iremos comparando con la cantidad de letras unicas que le ha tocado resolver
juego_terminado = False
# flag para juego terminado o no

# ahora vienen las funciones
# la 1ra hara que el sistema elija al azar una palabra de la lista de palabras


def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    # va a contener cuantas letras distintas/unicas tiene nuestra palabra, sin importar
    # las repeticiones para que luego podamos controlarlo
    # con los aciertos del usuario y saber cuando ha ganado

    return palabra_elegida, letras_unicas

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    # para validar si la letra elegida esta aqui, que sea una letra y no un numero

    # hacemos un while para que el usuario no pueda salir del
    # bucle hasta ingresar una letra valida

    # mientras es_valida sea falso
    while not es_valida:
        letra_elegida = input("Elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
            # cuando sea true se sale del bucle
        else:
            print("No has elegido una letra correcta")

    return letra_elegida
    # devolvemos la letra elegida que ya comprobamos que es valida

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('_')

    print(' '.join(lista_oculta))
    # permite unir todos los elem de lista oculta separados por un espacio
    # esta funcion solo imprime el "estado" de adivinacion en el que se encuentra el usuario

def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya has encontrado esa letra. Intenta con otra diferente.")
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
        # perder nos va devolver true y hara otras cosas
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias

def perder():
    print("Te has quedado sin vidas")
    print("La palabra oculta era " + palabra)

    return True

def ganar():
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicitaciones, has encontrado la palabra!!!")

    return True


palabra, letras_unicas = elegir_palabra(palabras)

# metemos juego terminado en un while, que mientras no sea verdad se ejecute el while
while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()
    # la almacenamos en letra para usarla más tarde

    intentos, terminado, aciertos = chequear_letra(letra,palabra,intentos,aciertos)

    juego_terminado = terminado



