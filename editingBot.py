from moviepy.editor import AudioFileClip, ImageClip
import auto_editor
from os import system
import sys


#NOMBRE DE LA IMAGEN.
imagePath = sys.argv[2]

#NOMBRE DEL AUDIO.
audioPath = sys.argv[1]

def remove_silence_from_audio(audio_path):
    system(f'auto-editor {audio_path} -m 0.1sec --no-open -o audio_ALTERED.wav')
    

def add_static_image_to_audio(image_path, audio_path, output_path):
    audio_clip = AudioFileClip(audio_path)
    image_clip = ImageClip(image_path)
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration
    video_clip.fps = 1
    video_clip.write_videofile(output_path)

    
remove_silence_from_audio(audioPath)

audioPath = 'audio_ALTERED.wav'

add_static_image_to_audio(imagePath , audioPath, 'video.mp4')