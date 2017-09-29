# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:01:56 2017

@author: cavr2302
"""

#Le but de ce fichier est de découper tous les sons en extraits de 4s

import wave 
import os

############# TRAITEMENT DES AUDIOS
def traitement(wav_name):
     sample_freq = 0
     sample_width = 0 
     #detection du fichier
     wav_file = 'sons_musique/'+ wav_name 
     print(wav_file)
     # ouverture du fichier
     wave_read = wave.openfp(wav_file, 'rb')
     print('1')
     # valeur de l'echantillonn. en bits
     sample_width = wave_read.getsampwidth()
     print ("sample width : %d" %sample_width)
     # Fréquence d'échantillonnage
     sample_freq = wave_read.getframerate() 
     print ("sample frequency : %d" %sample_freq) 
     wave_read.close()
     
     
############# MAIN
if __name__ == '__main__':
    #Boucle de traitement des audios
    for element in os.listdir('sons_musique/' ):
        if element.endswith('.wav'):
            traitement(element)
     
    