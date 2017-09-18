import os
import wave

import pylab as pb
import numpy as np

#Fréquence d'échantillonage = 2 * fc
FE = 10000
#NFFT echantillonnage - length of the windowing segments
NFFT = 1024

def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pb.figure(num=None, figsize=(19, 12))
    pb.subplot(111)
    pb.title('spectrogram of %r' % wav_file)
    n=2100
    pb.specgram(sound_info[n:n+256*256], NFFT=NFFT, Fs=FE, noverlap=1000, cmap='jet')
    pylab.savefig('spectrogram_parole.png')
    #pb.savefig('spectrogram_musique.png')

def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'Int64')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

if __name__ == '__main__': # Main function
    wav_file = 'ben_bravo.wav' # Filename of the wav file
    graph_spectrogram(wav_file)
    