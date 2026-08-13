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
        self.bpm_120 = resource_path("assets/120_bpm.mp3")

        # Audio list
        self.all_tracks = [
            self.bpm_100,
            self.bpm_120
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

        # 120 bpm button
        tk.Button(
            self,
            text="120 BPM",
            command=self.q_120_bpm
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

    # Function to change the track to 120 bpm
    def q_120_bpm(self):
        self.selected_track_index = 1
        self.selected_track = self.all_tracks[1]

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