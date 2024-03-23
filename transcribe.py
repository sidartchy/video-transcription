import azure.cognitiveservices.speech as speechsdk
import time 
import os
from dotenv import load_dotenv
from moviepy.editor import *



load_dotenv() 


speech_key = os.getenv("SPEECH_KEY")
service_region = os.getenv("SERVICE_REGION")

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)






audio_file = 'audio.wav'

audio_config = speechsdk.audio.AudioConfig(filename=audio_file)
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

transcriptions = []

def continuous_recognition_handler(evt):
    if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
      transcriptions.append(evt.result.text)

speech_recognizer.recognized.connect(continuous_recognition_handler)
speech_recognizer.start_continuous_recognition()


# wait for recognition to finish
audio_path = 'audio.wav'
audio_clip = AudioFileClip(audio_path)
audio_duration = audio_clip.duration
timeout_seconds = audio_duration
timeout_expiration = time.time() + timeout_seconds




while time.time() < timeout_expiration:
    time.sleep(1)

speech_recognizer.stop_continuous_recognition()


transcription = ' '.join(transcriptions)


#output transcriptions
output_file = 'transcriptions.txt'
with open(output_file, 'w') as f:
    f.write(transcription)

print("Transcription complete! Check transcriptions.txt for the output.")