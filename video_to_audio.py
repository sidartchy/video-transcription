from moviepy.editor import *


video_path = 'video.mp4'; 
audio_path = 'audio.wav';


def video_to_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio_params = {
        'codec': 'pcm_s16le',
        'bitrate': '16k',
        'fps': 16000,
        'nchannels': 1,
    }
    audio.write_audiofile(audio_path, fps=audio_params['fps'], codec=audio_params['codec'], bitrate=audio_params['bitrate'], nbytes=2),
    audio.close()
    video.close()

video_to_audio(video_path, audio_path)
