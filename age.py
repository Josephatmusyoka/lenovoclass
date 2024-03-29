import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
from PIL import Image, ImageTk  # Import Pillow classes for image handling

def calculate_age():
    birthdate_str = birthdate_entry.get()
    try:
        birthdate = datetime.strptime(birthdate_str, '%d/%m/%Y')
        today = datetime.now()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        result_label.config(text=f"You are {age} years old.")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please enter in DD/MM/YYYY format.")

def on_entry_click(event):
    if birthdate_entry.get() == 'Enter your birthdate (DD/MM/YYYY)':
       birthdate_entry.delete(0, "end")
       birthdate_entry.insert(0, '')
       birthdate_entry['fg'] = 'black'  # Change text color to black

def on_focusout(event):
    if birthdate_entry.get() == '':
        birthdate_entry.insert(0, 'Enter your birthdate (DD/MM/YYYY)')
        birthdate_entry['fg'] = 'grey'  # Change text color to grey

def create_gui():
    window = tk.Tk()
    window.title("Age Calculator")

    # Adjust window background to a solid color matching your design if needed
    window.configure(bg="#333333")

    # Load the background image with Pillow
    image_path = "group_phto.jpg"  # Ensure this path is correct
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    background_label = tk.Label(window, image=photo)
    background_label.place(relwidth=1, relheight=1, x=0, y=0)

    global birthdate_entry
    birthdate_entry = ttk.Entry(window, font=("Helvetica", 12))
    birthdate_entry.insert(0, 'Enter your birthdate (DD/MM/YYYY)')
    birthdate_entry.bind('<FocusIn>', on_entry_click)
    birthdate_entry.bind('<FocusOut>', on_focusout)
    birthdate_entry['fg'] = 'grey'  # Initial text color
    birthdate_entry.place(relx=0.5, rely=0.4, anchor='center')

    calculate_button = ttk.Button(window, text="Calculate Age", command=calculate_age)
    calculate_button.place(relx=0.5, rely=0.5, anchor='center')

    global result_label
    result_label = ttk.Label(window, text="", bg="#333333", fg="white")
    result_label.place(relx=0.5, rely=0.6, anchor='center')

    window.eval('tk::PlaceWindow . center')
    window.mainloop()

if __name__ == "__main__":
    create_gui()
