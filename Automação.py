import pyautogui
from time import sleep 

# Preencher quadros sozinho(usuário)
pyautogui.click(689,384,duration=0.5)
pyautogui.write('Joao')

# Preencher quadros sozinho(senha)
pyautogui.click(688,411,duration=0.5)
pyautogui.write('191221')

# Clicar em "Entrar"

pyautogui.click(590,441,duration=0.5)

# Extração de cada produto

with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        
# Clicar e digitar o produto 

        pyautogui.click(388,371,duration=0.5) 
        pyautogui.write(produto)

# Clicar e digitar quantidade     

        pyautogui.click(402,398,duration=0.5)  
        pyautogui.write(quantidade)

# Clicar e digitar preço 

        pyautogui.click(389,425,duration=0.5)
        pyautogui.write(preco)

# Clicar em registrar 

        pyautogui.click(313,581,duration=0.5)
        sleep(1)