# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:01:56 2017

@author: cavr2302
"""

#Le but de ce fichier est de découper tous les sons en extraits de 4s

import wave 
import os
import pydub

############# TRAITEMENT DES AUDIOS
def traitement(wav_name):
     #sample_freq = 0
     #sample_width = 0 
     #detection du fichier
     #wav_file = 'sons_musique/'+ wav_name 
     print(wav_name)
     # ouverture du fichier
     #wave_read = wave.openfp(wav_file, 'rb')
     #print('1')
     # valeur de l'echantillonn. en bits
     #sample_width = wave_read.getsampwidth()
     #print ("sample width : %d" %sample_width)
     # Fréquence d'échantillonnage
     #sample_freq = wave_read.getframerate() 
     #print ("sample frequency : %d" %sample_freq) 
     #wave_read.close()
     from pydub import AudioSegment
     print('1')
     t1=1000 #Works in milliseconds
     t2=4000
     print('2')
     newAudio = AudioSegment.from_wav('/sons_musique/'+wav_name)
     print('3')
     newAudio = newAudio[t1:t2]
     print('4')
     newAudio.export(wav_name, format="wav")
     print('5')
     
############# MAIN
if __name__ == '__main__':
    #Boucle de traitement des audios
    #for element in os.listdir('sons_musique/' ):
        #if element.endswith('.wav'):
        file_path = '/sons_musique/'
        for path, dirs, files in os.walk(file_path):
                for filename in files:
                    print(filename)
                    traitement(filename)
     
    