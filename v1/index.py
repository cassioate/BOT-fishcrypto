import pyautogui
import time

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
            connect = False
            

def searchForHighConfidenceImage(imagem):
    contadorProcurarImagem = 0
    img = None
    confidence = 0.95
    loading = True
    while img == None:
        print("Procurando imagem em searchForLowConfidenceImage: "+ imagem)
        if (procurarImagemSemRetornarErro("Loading")):
            while loading == True:
                if (procurarImagemSemRetornarErro("Loading")):
                    print("Ainda esta carregando")
                else:
                    if (procurarImagemSemRetornarErro("ErrorClose")):
                        pyautogui.click(pyautogui.locateCenterOnScreen("./assets/ErrorClose.png", confidence=confidence), duration=3)
                    else:
                        loading = False
        if (procurarImagemSemRetornarErro("ErrorClose")):
            pyautogui.click(pyautogui.locateCenterOnScreen("./assets/ErrorClose.png", confidence=confidence), duration=3)
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        contadorProcurarImagem += 1
        if contadorProcurarImagem >= 500:
            raise Exception('Erro ao achar a imagem: ' + imagem)
    return img

def searchForMidConfidenceImage(imagem):
    contadorProcurarImagem = 0
    img = None
    confidence = 0.9
    loading = True
    while img == None:
        print("Procurando imagem em searchForLowConfidenceImage: "+ imagem)
        if (procurarImagemSemRetornarErro("Loading")):
            while loading == True:
                if (procurarImagemSemRetornarErro("Loading")):
                    print("Ainda esta carregando")
                else:
                    if (procurarImagemSemRetornarErro("ErrorClose")):
                        pyautogui.click(pyautogui.locateCenterOnScreen("./assets/ErrorClose.png", confidence=confidence), duration=3)
                    else:
                        loading = False
        if (procurarImagemSemRetornarErro("ErrorClose")):
            pyautogui.click(pyautogui.locateCenterOnScreen("./assets/ErrorClose.png", confidence=confidence), duration=3)
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        contadorProcurarImagem += 1
        if contadorProcurarImagem >= 500:
            raise Exception('Erro ao achar a imagem: ' + imagem)
    return img

def searchForLowConfidenceImage(imagem):
    contadorProcurarImagem = 0
    img = None
    confidence = 0.6
    loading = True
    while img == None:
        print("Procurando imagem em searchForLowConfidenceImage: "+ imagem)
        if (procurarImagemSemRetornarErro("Loading")):
            while loading == True:
                if (procurarImagemSemRetornarErro("Loading")):
                    print("Ainda esta carregando")
                else:
                    if (procurarImagemSemRetornarErro("ErrorClose")):
                        pyautogui.click(pyautogui.locateCenterOnScreen("./assets/ErrorClose.png", confidence=confidence), duration=3)
                    else:
                        loading = False
        if (procurarImagemSemRetornarErro("ErrorClose")):
            pyautogui.click(pyautogui.locateCenterOnScreen("./assets/ErrorClose.png", confidence=confidence), duration=3)
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        contadorProcurarImagem += 1
        if contadorProcurarImagem >= 500:
            raise Exception('Erro ao achar a imagem: ' + imagem)
    return img

def lookIfTheBotShouldStart(imagem):
    contadorProcurarImagem = 0
    img = None
    confidence = 0.6
    while img == None:
        error = pyautogui.locateCenterOnScreen('./assets/ErrorClose.png', confidence=confidence)
        if error != None:
            raise Exception('Erro ao achar a imagem: ' + imagem)
        print("Procurando imagem em searchForLowConfidenceImage: "+ imagem)
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        contadorProcurarImagem += 1
        if contadorProcurarImagem >= 25:
            return None
    return img

def procurarImagemSemRetornarErro(imagem):
    loop = True
    contador = 0
    time.sleep(3)
    confidence = 0.95
    print("Procurando imagem em procurarImagemSemRetornarErro: "+ imagem)
    img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
    print(img)
    if img != None:
        return True
    return False


def procurarImagemSemRetornarErroMidConfidence(imagem):
    time.sleep(5)
    confidence = 0.9
    print("Procurando imagem em procurarImagemSemRetornarErro: "+ imagem)
    img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
    print(img)
    if img != None:
        return True
    return False

def procurarLocalizacaoDaImagemPelosEixos(imagem):
    if procurarImagemSemRetornarErro(imagem):
        confidence = 0.9
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
    pyautogui.click(x, y+50, duration=3)
    time.sleep(2)
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

def addRodInThelake(carteiraDaVaraCompartilhada):
    time.sleep(15)
    if lookIfTheBotShouldStart("addRod") != None:
        clickAddSharedAndChooseWallet("rodCompartilhadaUM/"+carteiraDaVaraCompartilhada)
        clickAddSharedAndChooseWallet("rodCompartilhadaDOIS/"+carteiraDaVaraCompartilhada)
        for i in range(7):
            pyautogui.click(searchForLowConfidenceImage("addRod"), duration=3)
            pyautogui.click(searchForHighConfidenceImage("MoedaDaRod"), duration=3)
            pyautogui.click(searchForHighConfidenceImage("Pick"), duration=3)
            waitForTheAvailablesRodsEnd()

    else:
        print("O lago já está cheio")

def switchScreen():
    time.sleep(1)
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")
    time.sleep(1)

#CONNECT
time.sleep(29000)
while True:
    try:
        conectarFunc()
        addRodInThelake("carteira")

        time.sleep(15)
        switchScreen()

        conectarFunc()
        addRodInThelake("carteira2")
        switchScreen()
        time.sleep(29000)

    except BaseException as err:
        print("Ocorreu um ERRO:")
        print(err)
        conectar = True