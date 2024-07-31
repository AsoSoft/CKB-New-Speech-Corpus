from transformers import pipeline, AutoModel
from pydub import AudioSegment
from pytube import YouTube, Playlist
from pydub.utils import which
AudioSegment.converter = which("ffmpeg")
from pydub.silence import split_on_silence, detect_leading_silence
import codecs
import os
import moviepy.editor as mp
import whisperx
import requests
from faster_whisper import WhisperModel
import gc 
import numpy as np
import webrtcvad

device = "cuda" 
audio_file = "nawroz.mp3"
batch_size = 256 # reduce if low on GPU mem
compute_type = "int8" # change to "int8" if low on GPU mem (may reduce accuracy)

# model = WhisperModel("/home/asosoft/api/STT/whisper-large-v3-ckb", device, device_index=1, compute_type="int8_float16")

def extract_video(link):
    try:
        yt = YouTube(link)
    except Exception as e:
        print(f"Error connecting to YouTube: {e}")
        return None

    try:
        stream = yt.streams.get_by_itag(139)
        if stream:
            stream.download("/home/asosoft/api/", "videoplayback.mp4")
            given_audio = AudioSegment.from_file('/home/asosoft/api/videoplayback.mp4', format="mp4")
            given_audio.export("/home/asosoft/api/sab.mp3", format="mp3")
            return AudioSegment.from_file("/home/asosoft/api/sab.mp3", "mp3")
        else:
            print("Failed to get audio stream from the YouTube video.")
            return None
    except Exception as e:
        print(f"Error extracting video: {e}")
        return None

def speechtotext(audio_file):
   

    try:
        response = requests.post(url, headers=headers, params=params, files=files)
        if response.status_code == 200:
            out = response.text
            out = out.replace("{", "").replace('}', '').replace('"', '').split(":")
            return out[1]
        else:
            print(f"Failed to transcribe audio. Status code: {response.status_code}")
            return ""
    except Exception as e:
        print(f"Failed to transcribe audio: {e}")
        return ""

# def sabtitel(sound_file, name):
#     try:
#         path = "/home/asosoft/api/speech/"
#         audio_chunks = split_on_silence(sound_file, min_silence_len=400, silence_thresh=-36)
#         if not os.path.exists(path):
#             os.makedirs(path)

#         for i, chunk in enumerate(audio_chunks):
#             out_file = path + name + "{0}.mp3".format(i)
#             chunk.export(out_file, format="mp3")
#             segments, _ = model.transcribe(out_file, word_timestamps=True)
#             s = ""
#             probabilities = []
#             for segment in segments:
#                 for word in segment.words:
#                     probabilities.append(word.probability)
#                     s = s + word.word
#             average_probability = sum(probabilities) / len(probabilities)

#             if average_probability >= 0.95:
#                 transcription = speechtotext(out_file)
#                 file = codecs.open(path + name + "{0}.txt".format(i), "w", "utf-8")
#                 file.write(transcription)
#                 file.close()
#             else:
#                 os.remove(out_file)
#     except Exception as e:
#         print(f"Failed to transcribe audio: {e}")

def sabtitel(sound_file, name):
    try:
        path = "/home/asosoft/api/speech/"
        audio_chunks = split_on_silence(sound_file, min_silence_len=400, silence_thresh=-36)
        if not os.path.exists(path):
            os.makedirs(path)

        for i, chunk in enumerate(audio_chunks):
            out_file = path + name + "{0}.mp3".format(i)
            chunk.export(out_file, format="mp3")
            transcription = speechtotext(out_file)
            print(transcription)
              
    except Exception as e:
        print(f"Failed to transcribe audio: {e}")

def extract_video_id(url):
    parts = url.split('=')
    return parts[1] if len(parts) == 2 else None

def playvideo(playlist_url):
    try:
        playlist = Playlist(playlist_url)
        video_links = playlist.video_urls

        if video_links:
            for link in video_links:
                try:
                    print(link)
                    audio_paths = extract_video(link)
                    if audio_paths:
                        video_id = extract_video_id(link)
                        sabtitel(audio_paths, video_id)
                except Exception as e:
                    print(f"Error processing video {link}: {e}")
        else:
            print("Unable to retrieve video links from the playlist.")
    except Exception as e:
        print(f"Error retrieving playlist: {e}")

file_path = "/home/asosoft/api/link.txt"
content_list = []
try:
    with open(file_path, "r") as file:
        for line in file:
            content_list.append(line.strip())
except Exception as e:
    print(f"Error reading file {file_path}: {e}")

for i in content_list:
    try:
        print(1)
        playvideo(i)
    except Exception as e:
        print(f"Error playing video {i}: {e}")



