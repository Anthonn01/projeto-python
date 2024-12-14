from  socket import *
import time

tempo_inicial = time.time()

alvo = input("imfome o IP para ser escaneado: ")

ip_alvo = gethostbyname(alvo)

print("começando scan: ", ip_alvo)

for i in range(50,500):
    s = socket(AF_INET, SOCK_STREAM)
    
    conexao = s.connect_ex((ip_alvo, i))
    
    if conexao == 0:
        print("porta:",i,"aberta")
        
    s.close()
    
print("tempo que levou : ", time.time
()- tempo_inicial)