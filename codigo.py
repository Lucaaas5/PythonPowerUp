
import pyautogui 
import time

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#Passo 1: Entrar no Sistema da emmpresa

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(10)
pyautogui.write(link)
pyautogui.press("enter")
#pausa maior pro site carregar
time.sleep(3)

#Passo 2: Fazer login
pyautogui.click(x=617, y=370)
pyautogui.write("cordeirolucas@gmail.com")
pyautogui.press("tab") #passando para proximo botao
pyautogui.write("12345")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

#Passo 3: Abrir a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    #Passo 4: Cadastrar 1 produto
    #codigo
    pyautogui.click(x=643, y=259)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write("codigo")
    pyautogui.press("tab")
    #marca
    marca  = str(tabela.loc[linha, "marca"])
    pyautogui.write("marca")    
    pyautogui.press("tab")
    #tipo
    tipo  = str(tabela.loc[linha, "tipo"])
    pyautogui.write("tipo")   
    pyautogui.press("tab")
    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write("categoria")
    pyautogui.press("tab")
    #preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write("preco")
    pyautogui.press("tab")
    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write("custo")
    pyautogui.press("tab")
    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.write("obs")
    pyautogui.press("tab") #passar par o enviar
    pyautogui.press("enter") #enviou
    pyautogui.scroll(5000)#volta pro inicio
#Passo 5: Repetir o passo 4 até acabar a lista de produtos


