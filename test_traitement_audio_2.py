##############Import librairie
import wave
import pylab as pb
import numpy as np


#############Constante
#Fréquence d'échantillonage = 2 * fc
FE = 22050
#NFFT echantillonnage - length of the windowing segments
NFFT = 1024

#############Fonction get_Info du fichier audio
#Return les info de l'audio et sa duree
def get_wav_info(wav_file):
    #Ouverture du fichier en lecture
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = np.fromstring(frames, 'Int16')
    wav.close()
    #Return
    return sound_info

#############Fonction enregistrement du spectrogramme
def graph_spectrogram(wav_file, name):
    #Recupere les infos de  audio
    sound_info = get_wav_info(wav_file)
    pb.figure(num=None, figsize=(19, 12))
    pb.subplot(111)
    pb.title('spectrogram of %r' % wav_file)
    #Definition des bornes de l audio a utiliser
    n1 = int(len(sound_info)/6)
    n2 = int(len(sound_info)*5/6)
    #Desine le spectrogramme d une partie de l audio
    # pb.specgram(sound_info[n1:n2], NFFT=NFFT, Fs=FE, noverlap=1000, cmap='jet')
    pb.specgram(sound_info, NFFT=NFFT, Fs=FE, noverlap=1000, cmap='jet')
    #Enregistrement du spectrogramme
    #pb.savefig('Base_spect_parole/' +name + '.png')
    pb.savefig('Base_spect_musique/' +name + '.png')



#############Fonction main
if __name__ == '__main__':
    #Boucle de traitement des audios
    i = 0
    while i < 936 :
        i = i+1
       # wav_file_parole = 'Base_parole/Parole (' + str(i) + ').wav' # Filename of the wav file
        wav_file_parole = 'sons_musique/Musique (' + str(i) + ').wav' # Filename of the wav file
       # name_png = 'spectrogram_parole_' + str(i)
        name_png = 'spectrogram_musique_' + str(i)
        graph_spectrogram(wav_file_parole, name_png)
        