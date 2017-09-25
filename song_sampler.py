# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:01:56 2017

@author: cavr2302
"""

#Le but de ce fichier est de découper tous les sons en extraits de 4s

import wave 

############# TRAITEMENT DES AUDIOS
def traitement(wav_file):
     sample_freq = 0
     sample_width = 0 
     # ouverture du fichier
     wave_write = wave.open(wav_file, 'rb')
     # valeur de l'echantillonn. en bits
     sample_width = wave_write.getsampwidth()
     print(sample_width)
     # Fréquence d'échantillonnage
     sample_freq = wave_write.getframerate() 
     print(sample_freq)
     wave.close()
     
     
############# MAIN
if __name__ == '__main__':
    #Boucle de traitement des audios
    i = 0
    while i < 2 :
        i = i+1
        wav_file = 'sons_musique/Musique (' + str(i) + ').wav' 
        traitement(wav_file)
     
    