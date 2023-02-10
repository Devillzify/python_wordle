import random
listaLetras = ["A","B","C","D"]
posiciones = [],[]
listaConteo = [0,0,0,0]
def generarcodigo(var):
    dificultad = 0
    numero = int(var)
    if numero == 1:
        dificultad = 4
    if numero == 2:
        dificultad = 6
    if numero == 3:
        dificultad = 8
    num = 0
    codigo = ''
    while num < dificultad:
        codigo += random.choice(listaLetras)
        num = num + 1
    return codigo

def comprobarPosicion(codigo,palabra):
    if codigo == palabra:
        print("Has ganado campeon, eres como Santi")
        quit()
    posicionCorrecta = 0

    for x in range(len(codigo)):
        if codigo[x] == palabra[x]:
            posicionCorrecta = posicionCorrecta + 1
    print("Letras del codigo en la posicion correcta: " + str(posicionCorrecta))
    return posicionCorrecta
            
def conteo(codigo):
    for x in codigo:
        if x == "A":
            listaConteo[0] = listaConteo[0] + 1
        if x == "B":
            listaConteo[1] = listaConteo[1] + 1
        if x == "C":
            listaConteo[2] = listaConteo[2] + 1
        if x == "D":
            listaConteo[3] = listaConteo[3] + 1

def seleccioDificultat(no):
    valor = 0
    if(no=="1"):
        valor = 1
    elif(no=="2"):
        valor = 2
    elif(no=="3"):
        valor = 3
    else:
        print("Has d'introduir un valor vàlid!")
    return valor

# Reb el codi introduit per l'usuari
def comprovarInput(entrada,codigo):
    entrada = entrada.upper()
    
    #Comprovar lletres correctes
    flg = True
    for x in entrada:
        if (listaLetras.count(x) == 0):
            flg = False

    #Comprovar tamany correcte
    if len(entrada) != len(codigo):
        flg = False
    return flg


# Calcular lletres incorrectes pero existents
def lletresIncorrectes(listaLetras, codigo, palabra, lletresOk):

  letras = 0
  for x in range(len(listaLetras)):
    pal = palabra.count(listaLetras[x])
    cod = codigo.count(listaLetras[x])

    if (pal >= cod):
       letras = letras + cod
    else:
       letras = letras + pal

  letras = letras - lletresOk
  print("Las letras existentes en posicion incorrecta son: " + str(letras))



def juego(codigo,dificultad):
    vidas = (dificultad * 10) + 1
    while vidas > 1:
        vidas = vidas - 1
        print("Vidas restantes: " + str(vidas))
        palabra = input("Introduce el codigo: ").upper()
       
        print("")
        if comprovarInput(palabra,codigo):
           cantidadCorrecta =  comprobarPosicion(codigo,palabra)
           lletresIncorrectes(listaLetras,codigo,palabra,cantidadCorrecta)
        else:
            print("Codigo incorrecto, has perdido una vida!!!")
    print("Has perdido looser L2P")
    print("El codigo era: " + codigo + ". no era tan dificil, IMBECIL!!!")

        
def partida():
  print("Bienvenido al juego")
  print("El codigo esta formado por una combinacion aleatoria de: ")
  print(" A  B  C  D ")
  print("selecciona tu dificultad: ")
  print("")
  print("1: Facil (4 digitos) \n2: Intermedio (6 digitos) \n3: Dificil (8 digitos)")
  print("")
  dificultad = seleccioDificultat(input("Tu eleccion: "))
  codigo = generarcodigo(dificultad)
  conteo(codigo)
  juego(codigo,dificultad)
  

partida()


