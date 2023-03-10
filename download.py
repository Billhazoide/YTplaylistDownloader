from pytube import YouTube
from pytube import Playlist
import os, sys
import moviepy.editor as mp
import re

def print_same_line(text):
  sys.stdout.write('\r')
  sys.stdout.flush()
  sys.stdout.write(text)
  sys.stdout.flush()

class Download:
  def __init__(self, playlist, folder):
    self.playlist = playlist
    self.folder = folder

  def getSongs(self):
    print_same_line("Downloading videos(MP4).")
    try:
      self.playlist = Playlist(self.playlist)

      for url in self.playlist:
        YouTube(url).streams.filter(only_audio=True).first().download(self.folder)
    except Exception as e:
      print("Error while geting the video.", e)
  
  def convert(self):
    print_same_line("Converting to mp3 file.")
    try:
      for url in self.playlist:
        YouTube(url).streams.first().download(self.folder)
    except Exception as e:
      print("Error while downloading video.", e)

  def exclude_mp4(self):
    print_same_line("Excluding mp4 file.\n")
    try:
      for file in os.listdir(self.folder):
        if re.search('mp4', file):
          mp4_path = os.path.join(self.folder,file)
          mp3_path = os.path.join(self.folder, os.path.splitext(file)[0]+'.mp3')
          new_file = mp.AudioFileClip(mp4_path)
          new_file.write_audiofile(mp3_path)
          os.remove(mp4_path)
    except Exception as e:
      print("Error while converting video {} to audio.".format(file), e)

playlist = "https://www.youtube.com/watch?v=DyMMEmwFQUE&list=PLuI7TkWUP4S8zgs-DgB768k1Wc09CF0mf&index=5"
folder = "/home/goodtwin/Downloads/awesome_mix"

downloader = Download(playlist, folder)
downloader.getSongs()
downloader.convert()
downloader.exclude_mp4()