import wave
import numpy as np


def convolution(parameter):
    # Use a breakpoint in the code line below to debug your script.
    print("Do convolution with parameter: ", parameter)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Audio input
    phrase = wave.open("Adria nao faz licao.wav", "rb")
    word = wave.open("Adria Recorte.wav", "rb") # este eh um recorte do primeiro audio, contendo apenas 1 palavra
    # word = wave.open("Adria.wav", "rb") # Este eh outro audio com a palavra repetida

    # Convert to bytes
    phrase_soundwave = phrase.readframes(-1)
    word_soundwave = word.readframes(-1)

    # Convert bytes to integers of size 16
    phrase_signal = np.frombuffer(phrase_soundwave, dtype="int16")
    word_signal = np.frombuffer(word_soundwave, dtype="int16")

    # Convolution operation
    np.convolve(phrase_signal, word_signal)

    print("Done")

