from struct import *
from bitstream import BitStream
import math
import time

def Compressor(k,flag):
    # Utilizando a flag para ficar alternando entre os arquivos de teste
    comeco = time.time()
    res = []
    
    if flag == 0:
        with open('corpus16MB.txt', 'rb') as file: 
            while True:
                rec = file.read(1) # lendo arquivo byte a byte
                if len(rec) != 1:
                    break
                res.append(rec) 
    else:
        with open('disco.mp4', 'rb') as file:
            while True:
                rec = file.read(1)
                if len(rec) != 1:
                    break
                res.append(rec)

    alfabeto = 256
   

    tam_dic = 256
    dicionario = {i.to_bytes(1,'big'): i for i in range(alfabeto)} # inicializando o dicionario com o alfabeto
    
    tam_max_dic = pow(2,k)  # definindo o tamanho maximo da tabela
    dados_comprimidos = []    #dados comprimidos serão enviados para cá

    concatena = bytes() #bytes a serem concatenados

    for simbolo in res:
        
        string_com_simbolo =  concatena + simbolo #concatenação de bytes se necessario
    
        
        if string_com_simbolo in dicionario: 
            concatena = string_com_simbolo
        
        else:
            aux = concatena
            dados_comprimidos.append(dicionario[aux])
            if(len(dicionario) <= tam_max_dic):
                dicionario[string_com_simbolo] = tam_dic
                tam_dic+= 1
            concatena = simbolo

    if concatena in dicionario:
        
        dados_comprimidos.append(dicionario[concatena])

    arquivo_de_saida = open("Comprimido" + "_" + str(k) + ".lwz", "wb")
    for data in dados_comprimidos:
        arquivo_de_saida.write(pack('>H',data))
    fim = time.time()
    print("Tempo de processamento para k = " + str(k)  + " Tempo = " , fim - comeco)
    
    arquivo_de_saida.close()


for k in range(9,16):
    Compressor(k,1)