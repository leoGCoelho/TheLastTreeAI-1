import urllib.request
import sys
import random
import time
import os

def switch(val):
    if val == 0:
        return 1

    return 0

if len(sys.argv)==1:
    print("Voce deve especificar o numero do jogador (0 ou 1)\n\nExemplo:    ./random_client.py 0")
    quit()

# Alterar se utilizar outro host
host = "http://localhost:8080"

player = int(sys.argv[1])

done = False
while True:
    os.system('python3 minimax_client.py ' + str(player))
    
    # Descansa um pouco para nao inundar o servidor com requisicoes
    time.sleep(1)
    player = switch(player)




