# Append the directory to sys.path
from text_to_sign import asl_model

# Use the function
text=input('Write text to translate to ASL\n')
print(asl_model.translate('asl','video',text))

# Example of using exec to run code from another file
if 'hungry' in text:
    with open('video_player.py', 'r') as file:
        script_content = file.read()
    exec(script_content)
