import pyautogui
import time
import datetime

pyautogui.PAUSE = 2

def conectarFunc():
    connect = True
    pyautogui.keyDown("ctrl")
    pyautogui.press("f5")
    pyautogui.keyUp("ctrl")
    while connect == True:
        if (procurarImagemSemRetornarErro("ConnectWallet")):
            pyautogui.click(searchForHighConfidenceImage("ConnectWallet"), duration=3)
            pyautogui.click(searchForHighConfidenceImage("AssinarMetamask"), duration=3)
            connect = False
        elif(procurarImagemSemRetornarErro("FAmarelo")):
            time.sleep(5)
            if(procurarImagemSemRetornarErro("FAmareloNaoCarregou")):
                connect = True
            else:
                connect = False
            
def searchForHighConfidenceImage(imagem):
    contadorProcurarImagem = 0
    img = None
    confidence = 0.8
    loading = True
    while img == None:
        print("Procurando imagem em searchForHighConfidenceImage: "+ imagem)
        if (procurarImagemSemRetornarErro("ErrorClose")):
            pyautogui.click(pyautogui.locateCenterOnScreen("./assets/ErrorClose.png", confidence=confidence), duration=3)
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        contadorProcurarImagem += 1
        print("IMG")
        print(img)
        if contadorProcurarImagem >= 15:
            raise Exception('Erro ao achar a imagem: ' + imagem)
    pyautogui.moveTo(img)
    return img

def lookIfTheBotShouldStart(imagem):
    print("Procurando imagem em lookIfTheBotShouldStart: "+ imagem)
    contadorProcurarImagem = 0
    img = None
    confidence = 0.8
    while img == None:
        error = pyautogui.locateCenterOnScreen('./assets/ErrorClose.png', confidence=confidence)
        if error != None:
            raise Exception('Erro ao achar a imagem: ' + imagem)
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        contadorProcurarImagem += 1
        if contadorProcurarImagem >= 10:    
            return None
    print("Procurando imagem em lookIfTheBotShouldStart: "+ imagem)
    return img

def procurarImagemSemRetornarErro(imagem):
    loop = True
    contador = 0
    time.sleep(3)
    confidence = 0.8
    print("Procurando imagem em procurarImagemSemRetornarErro: "+ imagem)
    img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
    if img != None:
        return True
    return False

def procurarLocalizacaoDaImagemPelosEixos(imagem):
    if procurarImagemSemRetornarErro(imagem):
        confidence = 0.8
        x, y = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        return x, y
    else:
        return None, None

def waitForTheAvailablesRodsEnd():
    availableRods = True
    while availableRods == True:
        img = procurarImagemSemRetornarErro("AvailableRods")
        if img == False:
            availableRods = False

def waitForTheAvailablesFriendsRodsRodsEnd():
    friendsRods = True
    while friendsRods == True:
        img = procurarImagemSemRetornarErro("FriendsRods")
        if img == False:
            friendsRods = False

def chooseRodShared():
    x, y = procurarLocalizacaoDaImagemPelosEixos("FriendsRods")
    y += 50
    pyautogui.click(x, y, duration=3)
    time.sleep(2)
    while not procurarImagemSemRetornarErro("Pick"):
        y += 85
        pyautogui.click(x, y, duration=3)
    pyautogui.click(searchForHighConfidenceImage("Pick"), duration=3)
    waitForTheAvailablesFriendsRodsRodsEnd()

def clickAddSharedAndChooseWallet(carteira):
    x, y = searchForHighConfidenceImage("addShared")
    pyautogui.click(x, y+10, duration=3)
    if(procurarImagemSemRetornarErro(carteira+"Borrowed")):
        print("Vara da carteira "+carteira+" já está sendo utilizada")
        fechar = searchForHighConfidenceImage("x")
        pyautogui.click(fechar)
    else:
        img = searchForHighConfidenceImage(carteira)
        pyautogui.click(img)
        chooseRodShared()

def addRodInThelakeForLoop(rod):
    pyautogui.click(searchForHighConfidenceImage(rod), duration=3)
    if lookIfTheBotShouldStart("MoedaDaRod") != None:
        pyautogui.click(searchForHighConfidenceImage("MoedaDaRod"), duration=3)
    elif lookIfTheBotShouldStart("MoedaDaRod2") != None:
        pyautogui.click(searchForHighConfidenceImage("MoedaDaRod2"), duration=3)
    # pyautogui.click(searchForHighConfidenceImage("Pick"), duration=3)
    waitForTheAvailablesRodsEnd()

def addRodInThelake(carteiraDaVaraCompartilhada):
    time.sleep(5)
    if lookIfTheBotShouldStart("addRod") != None or lookIfTheBotShouldStart("addRodOpcao2") != None or lookIfTheBotShouldStart("addRodOpcao3") != None:
        clickAddSharedAndChooseWallet("rodCompartilhadaUM/"+carteiraDaVaraCompartilhada)
        clickAddSharedAndChooseWallet("rodCompartilhadaDOIS/"+carteiraDaVaraCompartilhada)
        
        for i in range(7):
            if lookIfTheBotShouldStart("addRod") != None:
                addRodInThelakeForLoop("addRod")
            elif lookIfTheBotShouldStart("addRodOpcao2") != None:
                addRodInThelakeForLoop("addRodOpcao2")
            elif lookIfTheBotShouldStart("addRodOpcao3") != None:
                addRodInThelakeForLoop("addRodOpcao3")
            else:
                print("Não foi encontrado nenhum spot para inserir uma vara")
    else:
        print("O lago já está cheio")

def switchScreen():
    time.sleep(1)
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")
    time.sleep(1)

#CONNECT
time.sleep(2)
while True:
    try:
        print("-- INICIANDO --")
        timeDeEntrada = datetime.datetime.utcnow()
        print(timeDeEntrada)

        conectarFunc()
        addRodInThelake("carteira")
        time.sleep(10)
        switchScreen()
        time.sleep(10)

        conectarFunc()
        addRodInThelake("carteira2")
        time.sleep(10)
        switchScreen()
        time.sleep(10)

        timeDeSaida = datetime.datetime.utcnow()
        print("Entrando em modo de espera por 8 horas.")
        print(timeDeSaida)
        print("-- ENCERRANDO --")
        for i in range(7250):
            moveRange = round(random.uniform(100,700), 10)
            moveRange2 = round(random.uniform(100,700), 10)
            pyautogui.moveTo(moveRange, moveRange2, duration = 4)

    except BaseException as err:
        print("Ocorreu um ERRO:")
        print(err)