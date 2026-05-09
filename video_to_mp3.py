# Converts the videos to mp3 
import os 
import subprocess
import re

os.makedirs("audios", exist_ok=True)

files = os.listdir("videos") 

for file in files: 
    if file.endswith(".mp4"):
        
        # robust extraction (works for ALL files)
        match = re.search(r"Tutorial\s*#(\d+)", file)
        tutorial_number = match.group(1) if match else "unknown"
        
        file_name = os.path.splitext(file)[0]
        
        print(tutorial_number, file_name)
        
        subprocess.run([
            "ffmpeg",
            "-i", f"videos/{file}",
            f"audios/{tutorial_number}_{file_name}.mp3"
        ])