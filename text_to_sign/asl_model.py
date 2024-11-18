# module.py

import sign_language_translator as slt
from googletrans import Translator, LANGUAGES
from moviepy.editor import VideoFileClip
from moviepy.editor import *


def translate_text(text, dest_language):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text

def translate(sign,format,textc):
    oritext=textc
    try:
        textc=translate_text(textc, 'ur')
        language="urdu"
        if sign=='asl':
            sign='pk-sl'
        model = slt.models.ConcatenativeSynthesis(
        text_language=language, sign_language=sign, sign_format=format
        )
        text = textc
        sign = model.translate(text) # tokenize, map, download & concatenate
        
        sign.show()
    except:
            if 'hungry' in oritext:
                # Path to your video file
                video_path = 'hungry.mp4'
                # Load your video
                clip = VideoFileClip(video_path)
                # Play the video
                clip.preview()

            elif 'thirsty' in oritext:
                
                # Path to your video file
                video_path = 'thirsty.mp4'
                # Load your video
                clip = VideoFileClip(video_path)
                # Play the video
                clip.preview()
       
        
