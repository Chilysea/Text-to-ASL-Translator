from moviepy.editor import VideoFileClip
from moviepy.editor import *

# Path to your video file
video_path = 'hungry.mp4'

# Load your video
clip = VideoFileClip(video_path)

# Play the video
clip.preview()

