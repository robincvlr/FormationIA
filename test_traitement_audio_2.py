import os
import wave

import pylab
import numpy as np


def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)
    pylab.title('spectrogram of %r' % wav_file)
    NFFT = 1024       # the length of the windowing segments
    Fs = int(1.0 / 0.0005)  # the sampling frequency
    n=2100
    pylab.specgram(sound_info[n:n+256*256], NFFT=NFFT, Fs=Fs, noverlap=1000, cmap='PuOr')
    pylab.savefig('spectrogram_parole.png')


def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'Int64')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

if __name__ == '__main__': # Main function
    wav_file = 'parole2.wav' # Filename of the wav file
    graph_spectrogram(wav_file)