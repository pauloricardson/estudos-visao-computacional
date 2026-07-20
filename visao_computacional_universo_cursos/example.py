import cv2 as cv

caminho = 'casa.jpg'

def imageConstruct(caminho):
    img = cv.imread(caminho)

    if img is None:
        raise FileNotFoundError(f'Imagem não encontrada: {caminho}')

    return img

def showImage(img):
    cv.imshow('Imagem', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def obterCor(img):
    altura, largura, canal = img.shape
    for y in range(0, altura):
        for x in range(0, largura):
            azul = img[y, x, 0]
            verde = img[y, x, 1]
            vermelho = img[y, x, 2]
    
    return azul, verde, vermelho

def mudarCor(img):
    azul, verde, vermelho = obterCor(img)

    altura, largura, canal = img.shape
    for y in range(0, altura):
        for x in range(0, largura):
    
            img[y, x, 0] = verde[y, x]
            img[y, x, 1] = vermelho[y, x]
            img[y, x, 2] = azul[y, x]

    return img

def alterarCor(img, altura, largura, azul=None, verde=None, vermelho=None):
    for y in range(altura):
        for x in range(largura):

            if azul is not None:
                img[y, x, 0] = azul

            if verde is not None:
                img[y, x, 1] = verde

            if vermelho is not None:
                img[y, x, 2] = vermelho

    return img

def salvarImagem(img, nome_imagem, formato):
    cv.imwrite(f"{nome_imagem}.{formato}", img)

def main():
    img = imageConstruct(caminho)

    altura, largura, canais_de_cor = img.shape
    print(
        f'Tamanho: {altura} x {largura}, '
        f'Canais de cor: {canais_de_cor}'
    )

    img = mudarCor(img)

  

    showImage(img)


main()