import wave
import contextlib
import math
import struct


tot_files = 3  # Total number of files in the folder + 1 (151)
sample_rate = 44100.0


def append_sinewave(duration):
    volume = 1.0
    freq = 440.0

    num_samples = duration * sample_rate
    for x in range(int(num_samples)):
        audio.append(volume * math.sin(2 * math.pi * freq * (x / sample_rate)))
    return

def save_wav(file_name, audio):
    wav_file = wave.open(file_name, "w")
    # wav params
    nchannels = 1
    sampwidth = 2

    # 44100 is the industry standard sample rate - CD quality.  If you need to
    # save on file size you can adjust it downwards. The standard for low quality
    # is 8000 or 8kHz.
    nframes = len(audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

    # WAV files here are using short, 16 bit, signed integers for the
    # sample size.  So we multiply the floating point data we have by 32767, the
    # maximum value for a short integer.  NOTE: It is theortically possible to
    # use the floating point -1.0 to 1.0 data directly in a WAV file but not
    # obvious how to do that using the wave module in python.
    for sample in audio:
        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))

    wav_file.close()
    return



def get_wav_duration(file_name):
    with contextlib.closing(wave.open(file_name, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration


def generate_beep_wav(beep_file_name, duration, audio):
    append_sinewave(duration)
    save_wav(beep_file_name, audio)



for i in range(1, tot_files):
    audio = []
    # Generate path name
    file_number = str(i).zfill(3)
    file_name = './' + file_number + '.wav'
    duration = get_wav_duration(file_name)
    print(file_name + ' lasts for ' + str(duration) + ' seconds.')

    beep_file_name = './' + file_number + 'beep.wav'
    generate_beep_wav(beep_file_name, duration, audio)
    duration = get_wav_duration(beep_file_name)
    print(beep_file_name + ' lasts for ' + str(duration) + ' seconds.')






