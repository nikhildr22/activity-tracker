import time

def track_activity():
    while True:
        activity = input("What are you doing? ")
        print(f"You are doing: {activity}")
        time.sleep(60)  # Wait for 60 seconds

if __name__ == "__main__":
    track_activity()
import time
import tkinter as tk
from tkinter import messagebox

def track_activity():
    def submit_activity():
        activity = entry.get()
        messagebox.showinfo("Activity", f"You are doing: {activity}")
        entry.delete(0, tk.END)
        root.after(60000, submit_activity)  # Schedule the next prompt after 60 seconds

    root = tk.Tk()
    root.title("Activity Tracker")

    label = tk.Label(root, text="What are you doing?")
    label.pack(pady=10)

    entry = tk.Entry(root, width=50)
    entry.pack(pady=10)

    submit_button = tk.Button(root, text="Submit", command=submit_activity)
    submit_button.pack(pady=10)

    submit_activity()  # Initial prompt immediately
    root.mainloop()

if __name__ == "__main__":
    track_activity()
