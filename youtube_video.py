import os
import speech_recognition as sr
import yt_dlp as yt
from prompt import main as prompt_main
from pydub import AudioSegment

def download_video(url, video_dir):
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
            "preferredquality": "192",
        }],
        "verbose": True,
        "outtmpl": os.path.join(video_dir, "%(title)s.%(ext)s")
    }
    try:
        with yt.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            return filename
    except Exception as e:
        print(f"An error occurred while downloading the video: {str(e)}")
        return None

def transcribe_audio(audio, recognizer):
    text = recognizer.recognize_google(audio)
    return text

def detect_fallacy(text):
    print("Transcription:", text)
    with open("output.txt", "a") as f:
        f.write(text + "\n")
    prompt_main()

def split_audio(audio_path, chunk_length_ms=30000):
    audio = AudioSegment.from_wav(audio_path)
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
    return chunks

def main():
    url = "https://www.youtube.com/watch?v=1j0X9QMF--M"
    
    recognizer = sr.Recognizer()
    
    # Create directories for video and chunks
    video_dir = "videos"
    chunks_dir = "chunks"
    os.makedirs(video_dir, exist_ok=True)
    os.makedirs(chunks_dir, exist_ok=True)
    
    video_path = download_video(url, video_dir)
    if video_path is None:
        print("Failed to download the video. Exiting.")
        return
    
    audio_path = video_path.rsplit('.', 1)[0] + '.wav'
    
    try:
        chunks = split_audio(audio_path)
        full_text = ""
        for i, chunk in enumerate(chunks):
            chunk_path = os.path.join(chunks_dir, f"chunk{i}.wav")
            chunk.export(chunk_path, format="wav")
            with sr.AudioFile(chunk_path) as source:
                audio = recognizer.record(source)
            text = transcribe_audio(audio, recognizer)
            full_text += text + " "
        detect_fallacy(full_text)
    except Exception as e:
        print(f"An error occurred while processing the audio: {str(e)}")

if __name__ == "__main__":
    main()