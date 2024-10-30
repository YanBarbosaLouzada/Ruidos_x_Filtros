# Comparando a eficacia de filtros de suavização.
# objetivo: avaliar a eficacia de diferentes filtros de suavização
# no tratamento de ruidos aplicados a uma imagem

# aplique dois tipos de ruidos a imagem: ruido gaussiano e ruido sal e pimenta 
# filtros: filtros media (gaussiano), filtro da mediana, filtro bilateral
# avalie a eficacia de cada filtro em reduzir o ruido
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Funções para adicionar ruído
def addRuidoGaussiano(imagem, media=0, sigma=25):
    gaussiano = np.random.normal(media, sigma, imagem.shape).astype('uint8')
    imagem_ruidosa = cv2.add(imagem, gaussiano)
    return imagem_ruidosa

def addRuidoSalEPimenta(imagem, proporcao=0.05):
    imagem_ruidosa = imagem.copy()
    num_pixels = int(proporcao * imagem.size)
    for _ in range(num_pixels // 2):
        y_coord = np.random.randint(0, imagem.shape[0])
        x_coord = np.random.randint(0, imagem.shape[1])
        imagem_ruidosa[y_coord, x_coord] = 255
    for _ in range(num_pixels // 2):
        y_coord = np.random.randint(0, imagem.shape[0])
        x_coord = np.random.randint(0, imagem.shape[1])
        imagem_ruidosa[y_coord, x_coord] = 0
    return imagem_ruidosa

# Funções para aplicar filtros
def aplicarFiltroG(imagem, kernel_size=5):
    return cv2.GaussianBlur(imagem, (kernel_size, kernel_size), 0)

def aplicarFiltroM(imagem, kernel_size=5):
    return cv2.medianBlur(imagem, kernel_size)

def aplicarFiltroB(imagem, diametro=9, sigmaColor=75, sigmaSpace=75):
    return cv2.bilateralFilter(imagem, diametro, sigmaColor, sigmaSpace)

# Carrega a imagem e adiciona ruído
img = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
imgG = addRuidoGaussiano(img)
imgS = addRuidoSalEPimenta(img)

# Aplica filtros nas imagens com ruído gaussiano
gaussianoFG = aplicarFiltroG(imgG)
gaussianoFM = aplicarFiltroM(imgG)
gaussianoFB = aplicarFiltroB(imgG)

# Aplica filtros nas imagens com ruído sal e pimenta
SalpFG = aplicarFiltroG(imgS)
SalpFM = aplicarFiltroM(imgS)
SalpFB = aplicarFiltroB(imgS)

# Configura exibição com matplotlib
fig, axes = plt.subplots(3, 4, figsize=(15, 10))
fig.suptitle("Comparação de Filtros para Remoção de Ruído", fontsize=16)

# Primeira linha: Original 
axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title("Imagem Original")


# Segunda linha: Resultados dos filtros na imagem com ruído gaussiano
axes[1, 0].imshow(imgG, cmap='gray')
axes[1, 0].set_title("Ruído Gaussiano")
axes[1, 1].imshow(gaussianoFG, cmap='gray')
axes[1, 1].set_title("Ruído Gaussiano - Filtro Gaussiano")
axes[1, 2].imshow(gaussianoFM, cmap='gray')
axes[1, 2].set_title("Ruído Gaussiano - Filtro Mediana")
axes[1, 3].imshow(gaussianoFB, cmap='gray')
axes[1, 3].set_title("Ruído Gaussiano - Filtro Bilateral")

# Terceira linha: Resultados dos filtros na imagem com ruído sal e pimenta

axes[2, 0].imshow(imgS, cmap='gray')
axes[2, 0].set_title("Ruído Sal e Pimenta")
axes[2, 1].imshow(SalpFG, cmap='gray')
axes[2, 1].set_title("Ruído Sal e Pimenta - Filtro Gaussiano")
axes[2, 2].imshow(SalpFM, cmap='gray')
axes[2, 2].set_title("Ruído Sal e Pimenta - Filtro Mediana")
axes[2, 3].imshow(SalpFB, cmap='gray')
axes[2, 3].set_title("Ruído Sal e Pimenta - Filtro Bilateral")

# Remove eixos e ajusta layout
for ax in axes.flat:
    ax.axis("off")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
