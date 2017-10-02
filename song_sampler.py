# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:01:56 2017

@author: cavr2302
"""

#Le but de ce fichier est de découper tous les sons en extraits de 3s

import os

############# TRAITEMENT DES AUDIOS
def traitement(wav_name):
     #print(wav_name)
     #from pydub import AudioSegment
     #AudioSegment.converter = "/ffmpeg/bin/"
     #print('1')
     #t1=1000 #Works in milliseconds
     #t2=4000
     #print('2')
     #newAudio = AudioSegment.from_file('/sons_musique/'+wav_name, format="wav")
     #print('3')
     #newAudio = newAudio[t1:t2]
     #print('4')
     #newAudio.export(wav_name, format="wav")
     #print('5')
     
############# MAIN
if __name__ == '__main__':
    #Boucle de traitement des audios
        file_path = '/sons_musique/'
        for path, dirs, files in os.walk(file_path):
                for filename in files:
                    subprocess.call(['ffmpeg -t 30 -ss 00:00:00.000 -i %d -acodec copy %d'], filename)
                    #print(filename)
                    #traitement(filename)
     
    