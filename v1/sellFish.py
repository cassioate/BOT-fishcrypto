import pyautogui
import time

def searchForHighConfidenceImage(imagem):
    print("Procurando imagem em searchForHighConfidenceImage: "+ imagem)
    contadorProcurarImagem = 0
    img = None
    confidence = 0.95
    while img == None:
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        if contadorProcurarImagem >= 10:
            raise Exception('Erro ao achar a imagem: ' + imagem)
        if img == None:
            time.sleep(1)
        contadorProcurarImagem += 1
    return img

def procurarImagemSemRetornarErro(imagem):
    print("Procurando em procurarImagemSemRetornarErro: "+ imagem)
    contador = 0
    confidence = 0.9
    while contador < 10:
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        if img != None:
            contador = 16
        contador += 1
        time.sleep(1)
    if img != None:
        return True
    return False

vender = True
while vender == True:
    time.sleep(2)
    try:
        if(procurarImagemSemRetornarErro("Sell")):
            x, y = searchForHighConfidenceImage("Sell")
            pyautogui.click(x, y, duration=1)
            x, y = searchForHighConfidenceImage("SellButton")
            pyautogui.click(x, y, duration=1)
            x, y = searchForHighConfidenceImage("ErrorClose")
            pyautogui.click(x, y, duration=1)
        else:
            x, y = searchForHighConfidenceImage("RodSell")
            pyautogui.click(x, y, duration=1)
            x, y = searchForHighConfidenceImage("Fishes")
            pyautogui.click(x, y, duration=1)
    except BaseException as err:
        print("OCORREU UM ERRO!")
        if(not procurarImagemSemRetornarErro("InventoryDentroDoInventory") and not procurarImagemSemRetornarErro("ErrorClose")):
            print("ENTREI")
            pyautogui.keyDown("ctrl")
            pyautogui.press("f5")
            pyautogui.keyUp("ctrl")
            time.sleep(10)
        elif(procurarImagemSemRetornarErro("InventoryDentroDoInventory")):
            x, y = searchForHighConfidenceImage("InventoryDentroDoInventory")
            pyautogui.click(x, y, duration=1)
        if(procurarImagemSemRetornarErro("inventory")):
            x, y = searchForHighConfidenceImage("inventory")
            pyautogui.click(x, y, duration=1)
        if(procurarImagemSemRetornarErro("RodSell")):
            x, y = searchForHighConfidenceImage("RodSell")
            pyautogui.click(x, y, duration=1)
            x, y = searchForHighConfidenceImage("Fishes")
            pyautogui.click(x, y, duration=1)
        if(procurarImagemSemRetornarErro("ErrorClose")):
            x, y = searchForHighConfidenceImage("ErrorClose")
            pyautogui.click(x, y, duration=1)
