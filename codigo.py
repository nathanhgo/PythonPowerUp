# ----------------------------------- 1. Abrir o sistema da empresa -----------------------------------

# Para instalar: pip install pyautogui
import pyautogui
import time

# Configurar tempo de pausa entre execuções do pyautogui
pyautogui.PAUSE = 0.7

# Abrir navegador
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")

# Abrir link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Aqui pode ser que ele demore alguns segundos p/ carregar o site
time.sleep(3)

# ----------------------------------- 2. Fazer login no sistema -----------------------------------
pyautogui.click(x=525, y=399)
pyautogui.write("email_teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha_teste")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# ------------------- 3. Abrir/importar a base de dados de produtos p/ cadastrar ------------------
# pip install pandas numpy openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")

# ----------------------------------- 4. Cadastrar produtos -----------------------------------

for linha in  tabela.index:
    codigo = tabela.loc[linha, "codigo"]
    #clicar no campo do código
    pyautogui.click(x=569, y=291)

    #preencher o código
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    #tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    #apertar botao
    pyautogui.press("enter")
    #scrollar até o topo
    pyautogui.scroll(5000)
