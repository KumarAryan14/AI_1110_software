import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import numpy as np

class MusicPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Music Player")
        self.root.geometry("400x200")

        self.playlist = []
        self.current_index = -1
        self.paused = False

        # Buttons
        self.btn_browse = tk.Button(self.root, text="Browse Folder", command=self.browse_folder)
        self.btn_previous = tk.Button(self.root, text="Previous", state=tk.DISABLED, command=self.play_previous)
        self.btn_pause_resume = tk.Button(self.root, text="Pause", state=tk.DISABLED, command=self.pause_resume)
        self.btn_next = tk.Button(self.root, text="Next", state=tk.DISABLED, command=self.play_next)

        self.btn_browse.pack(pady=10)
        self.btn_previous.pack(pady=5)
        self.btn_pause_resume.pack(pady=5)
        self.btn_next.pack(pady=5)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.playlist = self.get_song_list(folder_path)
            if self.playlist:
                self.current_index = -1
                self.enable_controls()
                self.play_next()

    def get_song_list(self, folder_path):
        song_list = []
        for file in os.listdir(folder_path):
            if file.endswith(".mp3"):
                song_list.append(os.path.join(folder_path, file))
        return song_list

    def enable_controls(self):
        self.btn_previous.config(state=tk.NORMAL)
        self.btn_pause_resume.config(state=tk.NORMAL)
        self.btn_next.config(state=tk.NORMAL)

    def disable_controls(self):
        self.btn_previous.config(state=tk.DISABLED)
        self.btn_pause_resume.config(state=tk.DISABLED)
        self.btn_next.config(state=tk.DISABLED)

    def play_song(self, song_path):
        mixer.init()
        mixer.music.load(song_path)
        mixer.music.play()

    def play_next(self):
        if self.current_index < len(self.playlist) - 1:
            self.current_index += 1
            self.play_song(self.playlist[self.current_index])
            self.btn_pause_resume.config(text="Pause")
        else:
            np.random.shuffle(self.playlist)
            self.current_index = 0
            self.play_song(self.playlist[self.current_index])
            self.btn_pause_resume.config(text="Pause")

    def play_previous(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.play_song(self.playlist[self.current_index])
            self.btn_pause_resume.config(text="Pause")

    def pause_resume(self):
        if not self.paused:
            mixer.music.pause()
            self.paused = True
            self.btn_pause_resume.config(text="Resume")
        else:
            mixer.music.unpause()
            self.paused = False
            self.btn_pause_resume.config(text="Pause")

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    player = MusicPlayer()
    player.run()

