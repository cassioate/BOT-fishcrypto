import pyautogui
import time

# time.sleep(5)
# pyautogui.keyDown("alt")
# pyautogui.press("tab")
# pyautogui.keyUp("alt")

def procurarImagemSemRetornarErro(imagem):
    loop = True
    contador = 0
    time.sleep(3)
    confidence = 0.95
    print("Procurando imagem em procurarImagemSemRetornarErro: "+ imagem)
    img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
    if img != None:
        return True
    return False



def searchForHighConfidenceImage(imagem):
    contadorProcurarImagem = 0
    img = None
    confidence = 0.95
    loading = True
    while img == None:
        print("Procurando imagem em searchForHighConfidenceImage: "+ imagem)
        if (procurarImagemSemRetornarErro("ErrorClose")):
            pyautogui.click(pyautogui.locateCenterOnScreen("./assets/ErrorClose.png", confidence=confidence), duration=3)
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        contadorProcurarImagem += 1
        if contadorProcurarImagem >= 15:
            raise Exception('Erro ao achar a imagem: ' + imagem)
    return img


# returno = searchForHighConfidenceImage("rodCompartilhadaUM\carteira")
returno = procurarImagemSemRetornarErro("rodCompartilhadaDOIS/carteiraBorrowed")
print(returno)

# position = pyautogui.position()
# print(position)

# xSettings, ySettings = pyautogui.locateCenterOnScreen('./assets/'+ "Settingsname"+'.png', confidence=0.9)
# xF, yF = pyautogui.locateCenterOnScreen('./assets/'+ "FAmarelo"+'.png', confidence=0.9)

# pyautogui.click(xSettings, ySettings)
# pyautogui.click(xF, ySettings)

# def procurarImagemSemRetornarErro(imagem):
#     time.sleep(5)
#     confidence = 0.95
#     print("Procurando imagem em procurarImagemSemRetornarErro: "+ imagem)
#     img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
#     print(img)
#     if img != None:
#         return True
#     return False

# def procurarLocalizacaoDaImagemPelosEixos(imagem):
#     if procurarImagemSemRetornarErro(imagem):
#         confidence = 0.9
#         x, y = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
#         return x, y
#     else:
#         return None, None

# x, y = procurarLocalizacaoDaImagemPelosEixos("addShared")
# pyautogui.click(x, y+50, duration=3)

# def dragForTheLeft():
#     xSettings, ySettings = pyautogui.locateCenterOnScreen('./assets/'+ "Settingsname"+'.png', confidence=0.9)
#     xF, yF = pyautogui.locateCenterOnScreen('./assets/'+ "FAmarelo"+'.png', confidence=0.9)   
#     pyautogui.moveTo(x=xF, y=ySettings)
#     pyautogui.mouseDown(button='left')
#     pyautogui.dragTo(x=xSettings, y=ySettings, duration=1.5)
#     pyautogui.mouseUp(button='left')
#     time.sleep(2)

# def dragForTheRight():
#     xSettings, ySettings = pyautogui.locateCenterOnScreen('./assets/'+ "Settingsname"+'.png', confidence=0.9)
#     xF, yF = pyautogui.locateCenterOnScreen('./assets/'+ "FAmarelo"+'.png', confidence=0.9)   
#     pyautogui.moveTo(x=xSettings, y=ySettings)
#     pyautogui.mouseDown(button='left')
#     pyautogui.dragTo(x=xF, y=ySettings, duration=1.5)
#     pyautogui.mouseUp(button='left')
#     time.sleep(2)

# def waitForTheAvailablesFriendsRodsRodsEnd():
#     friendsRods = True
#     while friendsRods == True:
#         img = procurarImagemSemRetornarErro("FriendsRods")
#         if img == False:
#             friendsRods = False


# pyautogui.moveTo(1738, 49, duration = 4)