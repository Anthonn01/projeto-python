from ftplib import *

ftp = FTP("ftp.ibge.gov.br")

print(ftp.getwelcome())

usuario = input("informe o usuario")
senha = input("informe o senha")

ftp.login(usuario, senha)

print("Pasta atual: ", ftp.pwd())
print(ftp.retrlines('LIST'))

ftp.quit()