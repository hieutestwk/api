import vosk
import wave
import json

def listen_and_transcribe(model_path='models/vosk-model-small-en-us-0.15', wav_file='audio.wav'):
    vosk.SetLogLevel(-1)
    model = vosk.Model(model_path)
    rec = vosk.KaldiRecognizer(model, 16000)

    with wave.open(wav_file, "rb") as wf:
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            rec.AcceptWaveform(data)

    result = json.loads(rec.FinalResult())
    return result.get("text", "")