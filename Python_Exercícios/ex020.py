# Importando o PyGame
import pygame
import os
#os.getcwd() retorna o caminho do executável que está dentro do meu projeto

# Inicializando o PyGame
pygame.init()

# Carregando o arquivo MP3 e executando
if os.path.exists('audios/firework.mp3'):#verificando se o áudio existe no meu projeto
    pygame.mixer.music.load('audios/firework.mp3')#carregando o mp3
    pygame.mixer.music.play()#executando o player
    pygame.mixer.music.set_volume(1)#setando o volume

    clock = pygame.time.Clock()
    clock.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
else:
    print('O arquivo musica.mp3 não está no diretório do script Python')