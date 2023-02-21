from pydub import AudioSegment

filename = 'test1.wav'

sound = AudioSegment.from_wav('test.wav')
sound.export("test_export.mp3", format="mp3")