import cv2
import numpy as np
from pyzbar.pyzbar import decode
# cv2: derivada da OpenCV, a cv2 é uma Função de Interface de Captura de Vídeo
# numpy: Biblioteca de operação com Arrays, Álgebra Linear, Transformadas de Fourier e Matrizes.
# pyzbar: Biblioteca de leitura de Barcodes e QRCodes por meio da Biblioteca zbar.
def decoder(image):
    img_cinza = cv2.cvtColor(image,0)
    #cvtColor(src,code[, dst[, dstCn]]): converte Imagem de um Espaço de Cor em outro.
    barcode = decode(img_cinza)
    for img in barcode:
        ponto = img.polygon
        #polygon(): Wrapper de APIs de Polígono, usado para desenhar Formas Poligonais.
        (x,y,w,h) = img.rect
        #Rect(): usado para desenhar Retângulos.
        ptos = np.array(ponto, np.int32)
        #array(): converte Informações do Polígono na criação de um Array com Coordenadas Inteiras.
        ptos = ptos.reshape((-1, 1, 2))
        #reshape(): dá uma nova forma para o Array sem modificar seus Dados.
        cv2.polylines(image, [ptos], True, (0, 255, 0), 3)
        #polylines(): desenho de um Polígono em qualquer imagem.
        barcodeDados = img.data.decode("utf-8")
        #decode("utf-8"): decodifica string em Formato UTF-8.
        barcodeTipos = img.type
        #type - Tipo de Formato do Código
        string = "Dado: " + str(barcodeDados) + " || Tipo: " + str(barcodeTipos)
        #putText(): usado para inserir Textos de String em Imagens.
        cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
        print("Código de Barras: " + barcodeDados + " || Tipo: " + barcodeTipos)
        #printa o dado decodificado do Código e seu respectivo tipo.
captura = cv2.VideoCapture(0)
    #VideoCapture: função de Machine Learning e Processamento de Imagens
    # para Captura de Vídeo por Webcam ou Arquivo de Vídeo.
while True:
    ret, frame = captura.read()
    #Read(): leitura de Imagem por Frame e Retângulo.
    decoder(frame)
    #Decoder(): Função definida a priori para a decodificação do Frame.
    cv2.imshow('Image', frame)
    #Imshow(): usa uma Imagem como Display de uma Janela.
    code = cv2.waitKey(10)
    #WaitKey(): abre uma Janela enquanto nenhuma tecla é pressionada em tal Intervalo de Tempo.
    if code == ord('q'):
        #Ord: função que realiza o Break da variável Code,
        # pois quando a Tecla q é pressionada, a janela se fecha
        break
