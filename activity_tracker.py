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
        from datetime import datetime, date

        # Create a dictionary with the activity data
        activity_data = {
            "timestamp": datetime.now().isoformat(),
            "current_task": working_on,
            "todos": todos,
            "notes": notes
        }

        # Load existing data from the JSON file
        log_file_name = f"activity_log_{date.today().isoformat()}.json"
        try:
            with open(log_file_name, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        # Append the new activity data
        data.append(activity_data)

        # Save the updated data back to the JSON file
        with open(log_file_name, "w") as file:
            json.dump(data, file, indent=4)

        # Clear the textboxes
        working_on_textbox.delete("1.0", ctk.END)
        notes_textbox.delete("1.0", ctk.END)
        todos_textbox.delete("1.0", ctk.END)

        root.after(900000, submit_activity)  # Schedule the next prompt after 900 seconds (15 minutes)

    def add_todo():
        todo_description = todo_entry.get().strip()
        if todo_description:
            todos_textbox.insert(ctk.END, f"- [ ] {todo_description}\n")
            todo_entry.delete(0, ctk.END)  # Clear the entry field

    root = ctk.CTk()
    root.title("Activity Tracker")

    # Set appearance mode to light
    ctk.set_appearance_mode("light")  

    tabview = ctk.CTkTabview(root)
    tabview.pack(pady=10, fill="both", expand=True)

    # Tab 1: Working On
    tabview.add("Working On")
    working_on_label = ctk.CTkLabel(tabview.tab("Working On"), text="What are you working on?", text_color="black")
    working_on_label.pack(pady=10)
    working_on_textbox = ctk.CTkTextbox(tabview.tab("Working On"), width=400, height=200, text_color="black")
    working_on_textbox.pack(pady=10, fill="both", expand=True)

    # Tab 2: Notes
    tabview.add("Notes")
    notes_label = ctk.CTkLabel(tabview.tab("Notes"), text="Notes:", text_color="black")
    notes_label.pack(pady=10)
    notes_textbox = ctk.CTkTextbox(tabview.tab("Notes"), width=400, height=200, text_color="black")
    notes_textbox.pack(pady=10, fill="both", expand=True)

    # Tab 3: Todos
    tabview.add("Todos")

    todo_frame = ctk.CTkFrame(tabview.tab("Todos"))
    todo_frame.pack(pady=5, fill="x")  # Make the frame expand horizontally

    todo_entry = ctk.CTkEntry(todo_frame, placeholder_text="Enter todo description")
    todo_entry.pack(side="left", padx=5, fill="x", expand=True)  # Make the entry expand

    add_todo_button = ctk.CTkButton(todo_frame, text="Add", command=add_todo, width=50, text_color="black")
    add_todo_button.pack(side="right", padx=5)

    todos_textbox = ctk.CTkTextbox(tabview.tab("Todos"), width=400, height=200, text_color="black")
    todos_textbox.pack(pady=10, fill="both", expand=True)

    submit_button = ctk.CTkButton(root, text="Submit", command=submit_activity, width=100, height=30, text_color="black")
    submit_button.pack(pady=10)

    # submit_activity()  # Initial prompt immediately
    root.mainloop()

if __name__ == "__main__":
    track_activity()
