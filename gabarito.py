import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.3

email = "algo@gmail.com"
senha = "123"
URL = "http://127.0.0.1:5500/index.html"

# ---------------- ABRIR NAVEGADOR ----------------
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

time.sleep(2)

pyautogui.write(URL)
pyautogui.press("enter")
time.sleep(3)

# ---------------- LOGIN ----------------
pyautogui.click(x=932, y=541)  # campo email
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# ---------------- IMPORTAR CSV ----------------
tabela = pd.read_csv("produtos.csv")

# ---------------- CADASTRO ----------------
for linha in tabela.index:
    # Clicar no campo código
    pyautogui.click(x=669, y=425)
    time.sleep(0.3)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")

    time.sleep(1)


print("Cadastro finalizado 🚀")
