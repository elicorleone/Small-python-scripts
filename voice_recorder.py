import sounddevice
from scipy.io.wavfile import write
fs = 44100   # sample_rate
seconds = 10
print("recording...")
record_voice = sounddevice.rec(int(seconds * fs), samplerate=fs, channels=2)
sounddevice.wait()
write("out.wav", fs, record_voice)

'''Audio Recording Script using Python and sounddevice": 
A Python script that uses the sounddevice library to record audio 
for a specified duration and saves it as a high-quality WAV file.'''
