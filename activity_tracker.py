import time
import customtkinter as ctk
from tkinter import messagebox
import webbrowser
import json
from datetime import datetime, date

def track_activity():
    def open_html_page():
        webbrowser.open("C:\\Users\\DELL\\apps\\activity-dashboard.html")

    def load_previous_task():
        # Load the most recent task from today's log file
        log_file_name = f"activity_log_{date.today().isoformat()}.json"
        try:
            with open(log_file_name, "r") as file:
                data = json.load(file)
                if data and len(data) > 0:
                    return data[-1]["current_task"]  # Return the most recent task
        except FileNotFoundError:
            return None
        return None

    def update_previous_task_label():
        previous_task = load_previous_task()
        if previous_task:
            previous_task_label.configure(text=f"Previous task: {previous_task}")
            previous_task_checkbox.configure(state="normal")
        else:
            previous_task_label.configure(text="No previous task found")
            previous_task_checkbox.configure(state="disabled")

    def on_checkbox_change():
        previous_task = load_previous_task()
        if previous_task and previous_task_var.get():
            working_on_textbox.delete("1.0", ctk.END)
            working_on_textbox.insert("1.0", previous_task)
            working_on_textbox.configure(state="disabled")  # Disable the text area
        else:
            working_on_textbox.configure(state="normal")  # Enable the text area
            working_on_textbox.delete("1.0", ctk.END)

    def submit_activity():
        working_on = working_on_textbox.get("1.0", ctk.END).strip()
        notes = notes_textbox.get("1.0", ctk.END).strip()
        todos = todos_textbox.get("1.0", ctk.END).strip()

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

        # Clear the textboxes and re-enable the working on textbox
        working_on_textbox.configure(state="normal")  # Enable before clearing
        working_on_textbox.delete("1.0", ctk.END)
        notes_textbox.delete("1.0", ctk.END)
        todos_textbox.delete("1.0", ctk.END)
        
        # Reset checkbox
        previous_task_var.set(False)
        
        # Update the previous task label
        update_previous_task_label()

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
    
    # Previous task frame
    previous_task_frame = ctk.CTkFrame(tabview.tab("Working On"))
    previous_task_frame.pack(pady=5, fill="x")
    
    previous_task_label = ctk.CTkLabel(previous_task_frame, text="No previous task found", text_color="black")
    previous_task_label.pack(side="left", padx=5)
    
    previous_task_var = ctk.BooleanVar()
    previous_task_checkbox = ctk.CTkCheckBox(previous_task_frame, text="Continue previous task", 
                                           variable=previous_task_var, 
                                           command=on_checkbox_change,
                                           text_color="black")
    previous_task_checkbox.pack(side="right", padx=5)

    working_on_label = ctk.CTkLabel(tabview.tab("Working On"), text="What are you working on?", text_color="black")
    working_on_label.pack(pady=10)
    working_on_textbox = ctk.CTkTextbox(tabview.tab("Working On"), width=400, height=200, text_color="black")
    working_on_textbox.pack(pady=10, fill="both", expand=True)

    open_html_button = ctk.CTkButton(tabview.tab("Working On"), text="Open HTML", command=open_html_page, width=100, text_color="black")
    open_html_button.pack(pady=10, side="right")

    # Tab 2: Notes
    tabview.add("Notes")
    notes_label = ctk.CTkLabel(tabview.tab("Notes"), text="Do you have any notes to remember?", text_color="black")
    notes_label.pack(pady=10)
    notes_textbox = ctk.CTkTextbox(tabview.tab("Notes"), width=400, height=200, text_color="black")
    notes_textbox.pack(pady=10, fill="both", expand=True)

    open_html_button = ctk.CTkButton(tabview.tab("Notes"), text="Open HTML", command=open_html_page, width=100, text_color="black")
    open_html_button.pack(pady=10, side="right")

    # Tab 3: Todos
    tabview.add("Todos")

    todo_frame = ctk.CTkFrame(tabview.tab("Todos"))
    todo_frame.pack(pady=5, fill="x")

    todo_entry = ctk.CTkEntry(todo_frame, placeholder_text="Enter todo description")
    todo_entry.pack(side="left", padx=5, fill="x", expand=True)

    add_todo_button = ctk.CTkButton(todo_frame, text="Add", command=add_todo, width=50, text_color="black")
    add_todo_button.pack(side="right", padx=5)

    todos_textbox = ctk.CTkTextbox(tabview.tab("Todos"), width=400, height=200, text_color="black")
    todos_textbox.pack(pady=10, fill="both", expand=True)

    open_html_button = ctk.CTkButton(tabview.tab("Todos"), text="Open HTML", command=open_html_page, width=100, text_color="black")
    open_html_button.pack(pady=10, side="right")

    submit_button = ctk.CTkButton(root, text="Submit", command=submit_activity, width=100, height=30, text_color="black")
    submit_button.pack(pady=10)

    # Update the previous task label when starting the application
    update_previous_task_label()

    root.mainloop()

if __name__ == "__main__":
    track_activity()