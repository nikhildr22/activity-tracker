import time
import customtkinter as ctk
from tkinter import messagebox

def track_activity():
    def submit_activity():
        working_on = working_on_textbox.get("1.0", ctk.END).strip()
        notes = notes_textbox.get("1.0", ctk.END).strip()
        todos = todos_textbox.get("1.0", ctk.END).strip()

        # messagebox.showinfo("Activity", f"You are working on: {working_on}\nNotes: {notes}\nTodos: {todos}")

        import json
        from datetime import datetime

        # Create a dictionary with the activity data
        activity_data = {
            "timestamp": datetime.now().isoformat(),
            "current_task": working_on,
            "todos": todos,
            "notes": notes
        }

        # Load existing data from the JSON file
        try:
            with open("activity_data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        # Append the new activity data
        data.append(activity_data)

        # Save the updated data back to the JSON file
        with open("activity_data.json", "w") as file:
            json.dump(data, file, indent=4)

        # Clear the textboxes
        working_on_textbox.delete("1.0", ctk.END)
        notes_textbox.delete("1.0", ctk.END)
        todos_textbox.delete("1.0", ctk.END)

        root.after(900000, submit_activity)  # Schedule the next prompt after 900 seconds (15 minutes)

    root = ctk.CTk()
    root.title("Activity Tracker")

    tabview = ctk.CTkTabview(root)
    tabview.pack(pady=10, fill="both", expand=True)

    # Tab 1: Working On
    tabview.add("Working On")
    working_on_label = ctk.CTkLabel(tabview.tab("Working On"), text="What are you working on?")
    working_on_label.pack(pady=10)
    working_on_textbox = ctk.CTkTextbox(tabview.tab("Working On"), width=400, height=200)
    working_on_textbox.pack(pady=10, fill="both", expand=True)

    # Tab 2: Notes
    tabview.add("Notes")
    notes_label = ctk.CTkLabel(tabview.tab("Notes"), text="Notes:")
    notes_label.pack(pady=10)
    notes_textbox = ctk.CTkTextbox(tabview.tab("Notes"), width=400, height=200)
    notes_textbox.pack(pady=10, fill="both", expand=True)

    # Tab 3: Todos
    tabview.add("Todos")
    todos_label = ctk.CTkLabel(tabview.tab("Todos"), text="Todos:")
    todos_label.pack(pady=10)
    todos_textbox = ctk.CTkTextbox(tabview.tab("Todos"), width=400, height=200)
    todos_textbox.pack(pady=10, fill="both", expand=True)

    submit_button = ctk.CTkButton(root, text="Submit", command=submit_activity, width=100, height=30)
    submit_button.pack(pady=10)

    # submit_activity()  # Initial prompt immediately
    root.mainloop()

if __name__ == "__main__":
    track_activity()
