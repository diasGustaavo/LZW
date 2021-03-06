import sys
from sys import argv
import struct
from struct import *

decodificacao = 'latin-1'
dadosComprimidos = []
alfabeto = 256
contexto = 15

tamanhoDicionario = 256
dicionario = dict([(x, x.to_bytes(1,'big')) for x in range(256)])
tamanhoM√°ximoTabela = pow(2,contexto)           
dedadosComprimidos = []
concatenador = ""
proximo = 256

with open('Comprimido_15.lwz', 'rb') as f:
    while True:
        lido = f.read(2)
        if len(lido) != 2:
             break
        (data, ) = unpack('>H', lido)
        dadosComprimidos.append(data)

for frase in dadosComprimidos:
    if not (frase in dicionario):
        dicionario[frase] = (concatenador + concatenador[0]).encode(decodificacao)
    dedadosComprimidos.append(dicionario[frase])
    
    if not(len(concatenador) == 0):
        dicionario[proximo] = (concatenador + dicionario[frase].decode(decodificacao)[0]).encode(decodificacao)
        proximo +=1
    concatenador = dicionario[frase].decode(decodificacao)

video = True

if(video):
    arquivoResultante = open("disco_resultante" + ".mp4", "wb")
else:
    arquivoResultante = open("corpus16MB_resultante" + ".txt", "wb")

for data in dedadosComprimidos:
    arquivoResultante.write(data)
    
arquivoResultante.close()
