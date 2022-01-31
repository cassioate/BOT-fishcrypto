import pyautogui
import time

def searchForHighConfidenceImage(imagem):
    contadorProcurarImagem = 0
    img = None
    confidence = 0.95
    loading = True
    while img == None:
        print("Procurando imagem em searchForLowConfidenceImage: "+ imagem)
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        contadorProcurarImagem += 1
        if contadorProcurarImagem >= 500:
            raise Exception('Erro ao achar a imagem: ' + imagem)
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

vender = True
while vender == True:

    if(procurarImagemSemRetornarErro("Sell")):
        x, y = searchForHighConfidenceImage("Sell")
        pyautogui.click(x, y, duration=3)
        x, y = searchForHighConfidenceImage("SellButton")
        pyautogui.click(x, y, duration=3)
        x, y = searchForHighConfidenceImage("ErrorClose")
        pyautogui.click(x, y, duration=3)
    else:
        vender = False