import time
import customtkinter as ctk
from tkinter import messagebox

def track_activity():
    def submit_activity():
        activity = entry.get()
        messagebox.showinfo("Activity", f"You are doing: {activity}")
        entry.delete(0, ctk.END)
        root.after(60000, submit_activity)  # Schedule the next prompt after 60 seconds

    root = ctk.CTk()
    root.title("Activity Tracker")

    label = ctk.CTkLabel(root, text="What are you doing?")
    label.pack(pady=10)

    entry = ctk.CTkEntry(root, width=300)
    entry.pack(pady=10)

    submit_button = ctk.CTkButton(root, text="Submit", command=submit_activity)
    submit_button.pack(pady=10)

    submit_activity()  # Initial prompt immediately
    root.mainloop()

if __name__ == "__main__":
    track_activity()
