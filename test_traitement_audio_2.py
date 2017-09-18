##############Import librairie
import wave
import pylab as pb


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
    sound_info = pb.fromstring(frames, 'Int64')
    frame = wav.getnframes()
    print(frame)
    rate = wav.getframerate()
    #Calcul duree de l audio
    duration = frame/float(rate)
    wav.close()
    #Return
    return sound_info, duration

#############Fonction enregistrement du spectrogramme
def graph_spectrogram(wav_file, name):
    #Recupere les infos de  audio
    sound_info, duration = get_wav_info(wav_file)
    pb.figure(num=None, figsize=(19, 12))
    pb.subplot(111)
    pb.title('spectrogram of %r' % wav_file)
    #Nombre dechantillons
    n=int(duration*FE)
    print(n)
    n=int(44100/3)
    #Desine le spectrogramme d une partie de l audio
    pb.specgram(sound_info[n:n+256*256], NFFT=NFFT, Fs=FE, noverlap=1000, cmap='jet')
    #Enregistrement du spectrogramme
    pb.savefig(name + '.png')



#############Fonction main
if __name__ == '__main__':
    #Boucle de traitement des audios
    wav_file_parole = 'parole2.wav' # Filename of the wav file
    wav_file_musique = 'musique.wav' # Filename of the wav file
    graph_spectrogram(wav_file_parole, 'spectrogram_parole')