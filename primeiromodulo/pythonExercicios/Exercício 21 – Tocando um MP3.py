import pygame
print('Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3')
pygame.mixer.init() #inicia o payler
pygame.init() #inicia a bilbioteca
pygame.mixer.music.load('morning.mp3') #localiza o arquivo
pygame.mixer.music.play(loops=0, start=0.0) #play no arquivo (audio)
pygame.event.wait() #finaliza o programa
