# Versión 3.1 de Piedra Papel Tijera Lagarto Spock con Multijugador, animaciones caseras
# selección de idiomas y modos manual y automático


import random
import json
import os
import loadsavefiles
#  Aquí estan las funciones de cargar y salvar archivos de Json
from messenges import SP_MESSENGES
# Aquí hay un diccionario con todos los mensajes en español
from en_messenges import EN_MESSENGES
# El mismo diccionari de arriba con los mensajes en Inglés
import paints
import time
import platform
if platform.system() == 'Windows':
    import winsound

sessionStats = {"totalImputs": 0, "totalGoods": 0, "sessionTime": 0}
SOUNDS = {"load": "Punch.wav", "win": "Aplause.wav", "draw": "Cough.wav", "lose": "Jajaja.wav"}
victory = ['PR', 'PK', 'RS', 'RL', 'SP', 'SL', 'KS', 'KR', 'LK', 'LP']
# La lista de condiciones de victoria del jugador 1 o el usuario
options = ['R', 'P', 'S', 'L', 'K']
FILE = "score.json"
#  Ruta del fichero donde guardamos la partida
SAVE_ON_EXIT = True
SAVE_EACH_CYCLE = False
AUTOOPTIONS = ['1', '2']
'''Para elegir el modo en el que juegas, y el idioma. Sirve la misma constante
porque en ambas solo hay dos opciones. Si añadimos un idioma o otro
modo de juego debemos crear una nueva constante para controlarlo'''


def lenguageSelection():
    #  funcion para elegir el idioma
    selectLenguage = '3'
    while selectLenguage not in AUTOOPTIONS:
        selectLenguage = input(SP_MESSENGES["lenguage"])
        if selectLenguage == '1':
            #  En función de la lengua escogida cargará en el diccionario
            # 'MESSENGES' el diccionario del idioma que hayamos elegido
            MESSENGES = SP_MESSENGES
            return MESSENGES
        elif selectLenguage == '2':
            MESSENGES = EN_MESSENGES
            return MESSENGES


def userChoice():
    #  función para que el jugador haga su elección en modo manual
    option = 'j'
    while option not in options:
        option = input(MESSENGES["msg"])
        sessionStats["totalImputs"] += 1
        option = option.upper()
        if option == 'Q':
            sessionStats["totalGoods"] += 1
            programExit()
        cleanScreen()
    sessionStats["totalGoods"] += 1
    return option


def printStats():
    print(f'{MESSENGES["totalimputs"]}{allPlayers["stats"]["totalimputs"]}')
    print(f'{MESSENGES["totalgoods"]}{allPlayers["stats"]["goodsimputs"]}')
    print(f'{MESSENGES["totalbads"]}{allPlayers["stats"]["totalimputs"] - allPlayers["stats"]["goodsimputs"]}')
    print(f'{MESSENGES["sesionimputs"]}{sessionStats["totalImputs"]}')
    print(f'{MESSENGES["sesiongoods"]}{sessionStats["totalGoods"]}')
    print(f'{MESSENGES["sesionbads"]}{sessionStats["totalImputs"] - sessionStats["totalGoods"]}')
    sessionTime = time.gmtime(sessionStats["sessionTime"])
    totalTime = time.gmtime(allPlayers["stats"]["usertime"])
    print(f'{MESSENGES["totaltime"]}{time.strftime("%H:%M:%S", totalTime)}')
    print(f'{MESSENGES["sesiontime"]}{time.strftime("%H:%M:%S", sessionTime)}')


def cpuChoice():
    #  función para la elección de la maquina, tanto en modo manual
    # como para ambas elecciones en modo automático
    option = random.choice(options)
    '''if AUTOOPTIONS == 1:
        if option == 'R':
            print(MESSENGES["rock"])
        elif option == 'P':
            print(MESSENGES["paper"])
        elif option == 'S':
            print(MESSENGES["scissor"])
        elif option == 'L':
            print(MESSENGES["lizard"])
        else:
            print(MESSENGES["spock"])'''
    return option


def automaticMode(userValue, cpuValue):
    #   funcion que juega en modo automático. No imprime resultados
    chain = userValue + cpuValue
    if chain in victory:
        playerScore["victorys"] += 1
    elif userValue == cpuValue:
        playerScore["draws"] += 1
    else:
        playerScore["defeats"] += 1


def makeSomeNoise(soundfile):
    if platform.system() == 'Windows':
        winsound.PlaySound(soundfile, winsound.SND_ASYNC)
    elif platafor.system() == 'Linux':
        command = "aplay " + soundfile + "&"
        os.system(command)


def playerMode(userValue, cpuValue):
    #  funcion que juega en modo manual, imprimiendo los resultados de cada
    #  partida y las puntuaciones del usuario
    chain = userValue + cpuValue
    election = 'election' + cpuValue
    graphicals(userValue, cpuValue, election)
    if chain in victory:
        makeSomeNoise(SOUNDS["win"])
        print("\033[1;33m"+MESSENGES["win"]+'\033[0;m')
        playerScore["victorys"] += 1
    elif userValue == cpuValue:
        makeSomeNoise(SOUNDS["draw"])
        print("\033[1;33m"+MESSENGES["draw"]+'\033[0;m')
        playerScore["draws"] += 1
    else:
        makeSomeNoise(SOUNDS["lose"])
        print("\033[1;33m"+MESSENGES["lose"]+'\033[0;m')
        playerScore["defeats"] += 1
    if SAVE_EACH_CYCLE is True:
        allPlayers[player] = playerScore
        #  A la hora de salvar en multiusuario, asignamos el valor de las
        # puntuaciones en la clave de diccionario de nuestro jugador
        loadsavefiles.saveFile(allPlayers, FILE)
        #  Ahora salvamos todo el diccionario en el archivo json
    printResult(playerScore)


def cleanScreen():
    if platform.system() == 'Windows':
        os.system("cls")
    elif platform.system() == 'Linux':
        os.system("clear")


def graphicals(userValue, cpuValue, election):
    cleanScreen()
    for i in range(0, 2):
        makeSomeNoise(SOUNDS["load"])
        print(paints.STYLES["R"])
        print(paints.PAINT["R"])
        print(paints.PAINT["R"])
        time.sleep(1)
        cleanScreen()
        time.sleep(0.3)
    print(paints.STYLES[userValue])
    print(paints.PAINT[userValue])
    print(paints.STYLES[cpuValue])
    print(paints.PAINT[cpuValue])


def loadTable(player):
    # funcion que carga la tabla si esta existe, o la crea, con el nombre del
    # primer jugador, y la carga si no existe
    validate = os.path.isfile(FILE)
    if validate is not True:
        #  Si no existe el fichero, lo creamos
        modelDict = {player: {"victorys": 0, "defeats": 0, "draws": 0}, "stats": {"totalimputs": 0, "goodsimputs": 0, "usertime": 0}}
        #  creamos un modelo de diccionario para guardarlo como primer jugador,
        # si no existe el fichero
        loadsavefiles.saveFile(modelDict, FILE)
    allPlayers = loadsavefiles.loadfile(FILE)
    #  Cargamos el fichero en el diccionario allPlayers
    if player not in allPlayers:
        #  Si el jugador elegido no existe en el fichero, lo creamos
        # con la siguiente instrucción, con todos sus valores a 0
        allPlayers[player] = {"victorys": 0, "defeats": 0, "draws": 0}
    if "stats" not in allPlayers:
        allPlayers["stats"] = {"totalimputs": 0, "goodsimputs": 0, "usertime": 0}
    print(f'{MESSENGES["welcome"]} {player} ')
    return allPlayers


def printResult(playerScore):
    #  Imprime los resultados en la pantalla para el jugador
    print(f'{MESSENGES["results_a"]}{playerScore["victorys"]}{MESSENGES["victorys"]}')
    print(f'{MESSENGES["results_a"]}{playerScore["defeats"]}{MESSENGES["defeats"]}')
    print(f'{MESSENGES["results_a"]}{playerScore["draws"]}{MESSENGES["draws"]}')


def numberGames():
    #  función para introducir el numero de juegos que quieres que realice
    # la máquina en modo automático
    games = input(MESSENGES["games"])
    try:
        games = int(games)
    except ValueError:
        print(MESSENGES["error2"])
        return
    return games


def automatic():
    # función con el bucle para jugar el número de veces que queramos
    # en el modo automático
    numGames = numberGames()
    if numGames is None:
        return
    if numGames > 500000:
        print(MESSENGES["waiting"])
        #  Imprimira un 'Espere, por favor...' siempre que se juegue por encima
        #  de 300000 partidas, pues la CPU tardará cierto tiempo en hacerlo
    for i in range(0, numGames):
        automaticMode(cpuChoice(), cpuChoice())
    printResult(playerScore)
    #  Imprime los resultados sólo tras jugar todas las veces en el modo
    # automático. Siempre fuera del bucle, pues si no cargaríamos en exceso
    # la CPU y, además, no podríamos leer los resultados hasta el final
    if SAVE_EACH_CYCLE is True:
        allPlayers[player] = playerScore
        loadsavefiles.saveFile(allPlayers, FILE)


def principal(allPlayers, playerScore, player):
    #  función del bucle principal para el juego
    while True:
        autogame = '3'
        while autogame not in AUTOOPTIONS:
            autogame = input(MESSENGES["typegame"])
            #  Aquí elegimos el tipo de juego que queremos, manual o automático
        if autogame == '1':
            option = userChoice()
            playerMode(option, cpuChoice())
        if autogame == '2':
            automatic()
        contin = input(MESSENGES["continue"])
        #  El programa nos deja salir después de jugar, y también nos dará
        # la oportunidad de salir en mitad del juego manual
        if contin.upper() != 'S':
            programExit()
        cleanScreen()


def programExit():
    if SAVE_ON_EXIT is True:
        sessionStats["sessionTime"] = calculateTime()
        allPlayers[player] = playerScore
        allPlayers["stats"]["totalimputs"] = allPlayers["stats"]["totalimputs"] + sessionStats["totalImputs"]
        allPlayers["stats"]["goodsimputs"] = allPlayers["stats"]["goodsimputs"] + sessionStats["totalGoods"]
        allPlayers["stats"]["usertime"] = allPlayers["stats"]["usertime"] + sessionStats["sessionTime"]
        loadsavefiles.saveFile(allPlayers, FILE)
        printStats()
        #  cleanScreen()
    exit()


def calculateTime():
    elapsedTime = time.time()-startTime
    return elapsedTime


startTime = time.time()
cleanScreen()
MESSENGES = lenguageSelection()
#  Elegimos el idioma que queremos. En nuestro caso entre Inglés o Español,
#  pero se podrían incluir muchos más, solo copiando y traduciendo los
#  archivos MESSENGES
player = input(MESSENGES["newplayer"])
#  Preguntamos el nombre del jugador
player = player.upper()
#  Pasamos el nombre del jugador a mayusculas. El programa no creará
# dos usuarios con el mismo nombre
allPlayers = loadTable(player)
#  Cargamos el todo fichero en la tabla allPlayers, que será el diccionario
# que tendremos que guardar en el fichero posteriormente
playerScore = allPlayers[player]
#  Aquí cargamos las puntuaciones del jugador elegido en un diccionario,
# con el cual trabajaremos para aumentar la puntuación. Después asignaremos
# este diccionario como valor a la clave del nombre del jugador del diccionario
# allPlayers para poder guardar todos los datos
principal(allPlayers, playerScore, player)
#  Llamamos a la funcion principal

#  time.strftime("%H:%M:%S", time.gmtime(elapsed_time)) para transformar la variable de tiempo 
# en horas, minutos y segundos
