import tkinter as tk
from playsound3 import playsound
import pygame

import os
import sys


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # Initialize controller
        pygame.init()
        pygame.joystick.init()

        self.joystick = None

        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

        # Tkinter window
        self.geometry("300x500")
        self.title("Trackmania Metronome")

        # Audios
        self.bpm_100 = resource_path("assets/100_bpm.mp3")
        self.bpm_110 = resource_path("assets/110_bpm.mp3")
        self.bpm_120 = resource_path("assets/120_bpm.mp3")
        self.bpm_130 = resource_path("assets/130_bpm.mp3")
        self.bpm_140 = resource_path("assets/140_bpm.mp3")
        self.bpm_150 = resource_path("assets/150_bpm.mp3")
        self.bpm_160 = resource_path("assets/160_bpm.mp3")
        self.bpm_170 = resource_path("assets/170_bpm.mp3")
        self.bpm_180 = resource_path("assets/180_bpm.mp3")
        self.bpm_190 = resource_path("assets/190_bpm.mp3")
        self.bpm_200 = resource_path("assets/200_bpm.mp3")

        # Audio list
        self.all_tracks = [
            self.bpm_100,
            self.bpm_110,
            self.bpm_120,
            self.bpm_130,
            self.bpm_140,
            self.bpm_150,
            self.bpm_160,
            self.bpm_170,
            self.bpm_180,
            self.bpm_190,
            self.bpm_200
        ]

        # Global for keeping track of which index is selected for the track
        self.selected_track_index = 0

        # Global for the actual track being selected
        self.selected_track = self.all_tracks[
            self.selected_track_index
        ]

        self.sound = None
        self.running = False

        # Controller button state
        self.r1_pressed = False

        # GUI
        # Play button
        tk.Button(
            self,
            text="Play",
            command=self.play_sound
        ).pack(pady=5)

        # Stop button
        tk.Button(
            self,
            text="Stop",
            command=self.stop_sound
        ).pack(pady=5)

        # 100 bpm button
        tk.Button(
            self,
            text="100 BPM",
            command=self.q_100_bpm
        ).pack(pady=5)

        # 110 bpm button
        tk.Button(
            self,
            text="110 BPM",
            command=self.q_110_bpm
        ).pack(pady=5)

        # 120 bpm button
        tk.Button(
            self,
            text="120 BPM",
            command=self.q_120_bpm
        ).pack(pady=5)

        # 130 bpm button
        tk.Button(
            self,
            text="130 BPM",
            command=self.q_130_bpm
        ).pack(pady=5)

        # 140 bpm button
        tk.Button(
            self,
            text="140 BPM",
            command=self.q_140_bpm
        ).pack(pady=5)

        # 150 bpm button
        tk.Button(
            self,
            text="150 BPM",
            command=self.q_150_bpm
        ).pack(pady=5)

        # 160 bpm button
        tk.Button(
            self,
            text="160 BPM",
            command=self.q_160_bpm
        ).pack(pady=5)

        # 170 bpm button
        tk.Button(
            self,
            text="170 BPM",
            command=self.q_170_bpm
        ).pack(pady=5)

        # 180 bpm button
        tk.Button(
            self,
            text="180 BPM",
            command=self.q_180_bpm
        ).pack(pady=5)

        # 190 bpm button
        tk.Button(
            self,
            text="190 BPM",
            command=self.q_190_bpm
        ).pack(pady=5)

        # 200 bpm button
        tk.Button(
            self,
            text="200 BPM",
            command=self.q_200_bpm
        ).pack(pady=5)

        # Reset button
        tk.Button(
            self,
            text="Reset",
            command=self.reset
        ).pack(pady=5)

        # Start controller polling
        self.check_controller()

        self.protocol(
            "WM_DELETE_WINDOW",
            self.close
        )

    # Function to play the audio
    def play_sound(self):
        if self.sound:
            self.sound.stop()

        self.sound = playsound(
            self.selected_track,
            block=False
        )

        self.running = True

    # Function to stop the audio
    def stop_sound(self):
        self.running = False

        if self.sound:
            self.sound.stop()
            self.sound = None

    # Function to change the track to 100 bpm
    def q_100_bpm(self):
        self.selected_track_index = 0
        self.selected_track = self.all_tracks[0]

        self.play_sound()

    # Function to change the track to 110 bpm
    def q_110_bpm(self):
        self.selected_track_index = 1
        self.selected_track = self.all_tracks[0]

        self.play_sound()

    # Function to change the track to 120 bpm
    def q_120_bpm(self):
        self.selected_track_index = 2
        self.selected_track = self.all_tracks[2]

        self.play_sound()

    # Function to change the track to 130 bpm
    def q_130_bpm(self):
        self.selected_track_index = 3
        self.selected_track = self.all_tracks[3]

        self.play_sound()

    # Function to change the track to 140 bpm
    def q_140_bpm(self):
        self.selected_track_index = 4
        self.selected_track = self.all_tracks[4]

        self.play_sound()

    # Function to change the track to 150 bpm
    def q_150_bpm(self):
        self.selected_track_index = 5
        self.selected_track = self.all_tracks[5]

        self.play_sound()

    # Function to change the track to 160 bpm
    def q_160_bpm(self):
        self.selected_track_index = 6
        self.selected_track = self.all_tracks[6]

        self.play_sound()

    # Function to change the track to 170 bpm
    def q_170_bpm(self):
        self.selected_track_index = 7
        self.selected_track = self.all_tracks[7]

        self.play_sound()

    # Function to change the track to 180 bpm
    def q_180_bpm(self):
        self.selected_track_index = 8
        self.selected_track = self.all_tracks[8]

        self.play_sound()

    # Function to change the track to 190 bpm
    def q_190_bpm(self):
        self.selected_track_index = 9
        self.selected_track = self.all_tracks[9]

        self.play_sound()

    # Function to change the track to 130 bpm
    def q_200_bpm(self):
        self.selected_track_index = 10
        self.selected_track = self.all_tracks[10]

        self.play_sound()

    # Function to reset the audio
    def reset(self):
        self.stop_sound()
        self.play_sound()

    # Function to check for controller input
    def check_controller(self):

        try:
            if self.joystick:
                pygame.event.pump()

                # RumblePad 2 B button
                # Button index 2
                r1 = self.joystick.get_button(2)

                # Only trigger once when B is initially pressed
                if r1 and not self.r1_pressed:
                    self.reset()

                # Remember current state
                self.r1_pressed = r1

        except Exception:
            pass

        # Check again in 10 ms
        self.after(
            10,
            self.check_controller
        )

    # Function to close the app
    def close(self):
        if self.sound:
            self.sound.stop()

        pygame.quit()
        self.destroy()


# Function for the relative paths of the audio files
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    app = App()
    app.mainloop()