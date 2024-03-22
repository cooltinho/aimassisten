import cv2
import pyautogui

def detectar_bolinhas(imagem):
    # Converte a imagem para o espaço de cores HSV
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    # Define os limites de cor para as bolinhas
    # (H, S, V)
    # Vermelho
    baixo_vermelho = np.array([0, 100, 100])
    alto_vermelho = np.array([10, 255, 255])

    # Verde
    baixo_verde = np.array([40, 100, 100])
    alto_verde = np.array([70, 255, 255])

    # Azul
    baixo_azul = np.array([110, 100, 100])
    alto_azul = np.array([130, 255, 255])

    # Cria máscaras para cada cor
    mascara_vermelho = cv2.inRange(hsv, baixo_vermelho, alto_vermelho)
    mascara_verde = cv2.inRange(hsv, baixo_verde, alto_verde)
    mascara_azul = cv2.inRange(hsv, baixo_azul, alto_azul)

    # Combina as máscaras
    mascara = mascara_vermelho | mascara_verde | mascara_azul

    # Encontra os contornos das bolinhas
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Retorna os contornos das bolinhas
    return contornos

def mover_mouse_para_bolinhas(contornos):
    for contorno in contornos:
        # Encontra o centro da bolinha
        x, y, w, h = cv2.boundingRect(contorno)
        centro_x = x + w // 2
        centro_y = y + h // 2

        # Move o mouse para o centro da bolinha
        pyautogui.moveTo(centro_x, centro_y)

while True:
    # Captura a tela
    imagem = np.array(pyautogui.screenshot())

    # Detecta as bolinhas
    contornos = detectar_bolinhas(imagem)

    # Move o mouse para as bolinhas
    mover_mouse_para_bolinhas(contornos)

    if __name__ == "__main__":
    while True:
        # Captura a tela
        imagem = np.array(pyautogui.screenshot())

        # Detecta as bolinhas
        contornos = detectar_bolinhas(imagem)

        # Move o mouse para as bolinhas
        mover_mouse_para_bolinhas(contornos)

