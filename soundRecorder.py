import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100 #samp frequency
duration = int(input("Recording duration (s):")) #record duration

recording = sd.rec(int(duration * freq),
                   samplerate=freq, channels=2)
sd.wait()
fileName = str(input("Enter file name: "))
write(f"{fileName}.wav", freq, recording)