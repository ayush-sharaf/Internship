import tkinter as tk
import random
import time
class SpeedTypingTest:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Speed Typing Test")

        # Create a label to display the sentence to be typed
        self.sentence_label = tk.Label(self.root, text="Ready to start?")
        self.sentence_label.pack()

        # Create an entry widget for the user to type the sentence
        self.entry = tk.Entry(self.root)
        self.entry.pack()

        # Create a button to start the test
        self.start_button = tk.Button(self.root, text="Start", command=self.start_test)
        self.start_button.pack()

        # Create a button to stop the test
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_test)
        self.stop_button.pack()

        # Create a label to display the results of the test
        self.results_label = tk.Label(self.root)
        self.results_label.pack()

    def start_test(self):
        # Generate a random sentence to be typed
        self.sentence = random.choice(["The quick brown fox jumps over the lazy dog.", "Now is the time for all good men to come to the aid of the party.", "A penny saved is a penny earned."])

        # Display the sentence to be typed
        self.sentence_label.config(text=self.sentence)

        # Start a timer
        self.start_time = time.time()

        # Disable the start button
        self.start_button.config(state="disabled")

        # Enable the stop button
        self.stop_button.config(state="normal")

    def stop_test(self):
        # Calculate the time taken to type the sentence
        self.end_time = time.time()
        self.time_taken = self.end_time - self.start_time

        # Calculate the typing speed in words per minute (WPM)
        self.wpm = len(self.sentence.split()) / self.time_taken * 60

        # Display the results of the test
        self.results_label.config(text="Your typing speed is {} WPM!".format(self.wpm))

        # Disable the stop button
        self.stop_button.config(state="disabled")

        # Enable the start button
        self.start_button.config(state="normal")

if __name__ == "__main__":
    test = SpeedTypingTest()
    test.root.mainloop()
