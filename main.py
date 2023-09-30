import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

#frekans
freq = 4410

#süre
duration = 5

#kaydedici verileri
recording = sd.rec(int(duration * freq), samplerate = freq, channels = 2)

#sesi durdurur
sd.wait()

#dosyaya yazdırır
write("recording0.wav", freq, recording)
wv.write("recording1.wav", recording, freq ,sampwidth=2)
