import time
import customtkinter as ctk
from tkinter import messagebox

def track_activity():
    def submit_activity():
        working_on = working_on_textbox.get("1.0", ctk.END).strip()
        notes = notes_textbox.get("1.0", ctk.END).strip()
        todos = todos_textbox.get("1.0", ctk.END).strip()

        # messagebox.showinfo("Activity", f"You are working on: {working_on}\nNotes: {notes}\nTodos: {todos}")

        working_on_textbox.delete("1.0", ctk.END)
        notes_textbox.delete("1.0", ctk.END)
        todos_textbox.delete("1.0", ctk.END)

        root.after(60000, submit_activity)  # Schedule the next prompt after 60 seconds

    root = ctk.CTk()
    root.title("Activity Tracker")

    tabview = ctk.CTkTabview(root)
    tabview.pack(pady=10, fill="both", expand=True)

    # Tab 1: Working On
    tabview.add("Working On")
    working_on_label = ctk.CTkLabel(tabview.tab("Working On"), text="What are you working on?")
    working_on_label.pack(pady=10)
    working_on_textbox = ctk.CTkTextbox(tabview.tab("Working On"), width=400, height=200)
    working_on_textbox.pack(pady=10)

    # Tab 2: Notes
    tabview.add("Notes")
    notes_label = ctk.CTkLabel(tabview.tab("Notes"), text="Notes:")
    notes_label.pack(pady=10)
    notes_textbox = ctk.CTkTextbox(tabview.tab("Notes"), width=400, height=200)
    notes_textbox.pack(pady=10)

    # Tab 3: Todos
    tabview.add("Todos")
    todos_label = ctk.CTkLabel(tabview.tab("Todos"), text="Todos:")
    todos_label.pack(pady=10)
    todos_textbox = ctk.CTkTextbox(tabview.tab("Todos"), width=400, height=200)
    todos_textbox.pack(pady=10)

    submit_button = ctk.CTkButton(root, text="Submit", command=submit_activity, width=200, height=30)
    submit_button.pack(pady=10, fill="both", expand=True)

    # submit_activity()  # Initial prompt immediately
    root.mainloop()

if __name__ == "__main__":
    track_activity()
