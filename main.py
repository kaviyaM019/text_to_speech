from gtts import gTTS
import os
import subprocess

# Function to convert text to speech and save as .wav
def text_to_speech(text, filename='output.wav'):
    # Convert text to speech using Google TTS
    tts = gTTS(text=text, lang='en')
    
    # Save as mp3 first (gTTS only outputs mp3)
    temp_mp3 = 'temp.mp3'
    tts.save(temp_mp3)
    
    # Convert mp3 to wav using ffmpeg
    subprocess.run(['ffmpeg', '-i', temp_mp3, filename], check=True)
    
    # Remove temp mp3 file
    os.remove(temp_mp3)
    print(f'Speech saved as {filename}')

# Example usage
text = "Hello! This is a text-to-speech test."
text_to_speech(text)