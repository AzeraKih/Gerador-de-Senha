import configparser
from random import randrange as rand

config = configparser.ConfigParser()
config.read('config.ini')
senhasIni = config['Senhas']
senha = senhasIni.pop('ordem')
keysIni = [key for key in senhasIni]
d = dict()

for key in keysIni:
    d[key] = senha.count("[" + key + "]")

for field in d:
    for i in range(int(d[field])):
        arrps = senhasIni[field].split(" ")
        senha = senha.replace("[" + field + "]", arrps[rand(len(arrps))], 1)
        
print(senha)
input('Pressione ENTER para continuar...')
