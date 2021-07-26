# Notepad
# icon http://www.doublejdesign.co.uk
import tkinter as tk
from tkinter import StringVar, IntVar, scrolledtext, END, messagebox, filedialog
from PIL import ImageTk, Image

# Define window
root = tk.Tk()
root.title("Notepad")
root.iconbitmap("pad.ico")
root.geometry("600x600")
root.resizable(0,0)

# Define fonts and colors
text_color = "#fffacd"
menu_color = "#dbd9db"
root_color = "#6c809a"
root.config(bg=root_color)

# Define functions
def change_font(event):
    """change the given font based off dropbox options"""
    if font_option.get() == "none":
        my_font = (font_family.get(), font_size.get())
    else:
        my_font = (font_family.get(), font_size.get(), font_option.get())

    # Change the font style
    input_text.config(font=my_font)

def new_note():
    """Creates a new Note which essentially clears the screen"""
    # Use a messagebox to ask for a new note
    question = messagebox.askyesno("New Note", "Are you sure you want to start a new note")
    if question == 1:
        # ScrolledText widgets starting index is 1. not 0
        input_text.delete("1.0", END)

def close_note():
    """Closes the note which essentially quits the program"""
    # Use a messagebox to ask to close
    question = messagebox.askyesno("Close Note", "Are you sure you want to close your note?")
    if question == 1:
        root.destroy()

def save_note():
    """"Save the given note. First threel ines are saved as font family, font size, and font option."""
    # Use filedialog to get location and name of where/what to save the file as.
    save_name = filedialog.asksaveasfilename(initialdir="./", title="Save Note", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    with open(save_name, 'w') as f:
        # First three lines of save file are font_family, font_size, and font_options. Font size must be a string not int.
        f.write(font_family.get() + "\n")
        f.write(str(font_size.get()) + "\n")
        f.write(font_option.get() + "\n")

        # Write remaining text
        f.write(input_text.get("1.0", END))


# Define the layout
# Create frames
menu_frame = tk.Frame(root, bg=menu_color)
text_frame = tk.Frame(root, bg=text_color)
menu_frame.pack(padx=5, pady=5)
text_frame.pack(padx=5, pady=5)

# Layout for menu frame
# Create the menu: new, open, save, close, font family, font size, font option
new_image = ImageTk.PhotoImage(Image.open("img/new.png"))
new_button = tk.Button(menu_frame, image=new_image, command=new_note)
new_button.grid(row=0, column=0, padx=5, pady=5)

open_image = ImageTk.PhotoImage(Image.open("img/open.png"))
open_button = tk.Button(menu_frame, image=open_image)
open_button.grid(row=0, column=1, padx=5, pady=5)

save_image = ImageTk.PhotoImage(Image.open("img/save.png"))
save_button = tk.Button(menu_frame, image=save_image, command=save_note)
save_button.grid(row=0, column=2, padx=5, pady=5)

close_image = ImageTk.PhotoImage(Image.open("img/close.png"))
close_button = tk.Button(menu_frame, image=close_image, command=close_note)
close_button.grid(row=0, column=3, padx=5, pady=5)

# Create a list of fonts to use
families = ["Terminal", "Modern", "Script", "Courier", "Arial", "Calibri", "Cambria", "Georgia", "MS Gothic", "SimSun", "Tahoma", "Times New Roman", "Verdana", "Wingdings"]
font_family = StringVar()
font_family_drop = tk.OptionMenu(menu_frame, font_family, *families, command=change_font)
font_family.set("Terminal")
# Set the width so it will fit "Times New Roman" and remain constant
font_family_drop.config(width=16)
font_family_drop.grid(row=0, column=4, padx=5, pady=5)

sizes = [8, 10, 12, 14, 16, 20, 24, 32, 48, 64, 72, 96]
font_size = IntVar()
font_size_drop = tk.OptionMenu(menu_frame, font_size, *sizes, command=change_font)
font_size.set(12)
# Set the font widget width so it will remain constant
font_size_drop.config(width=2)
font_size_drop.grid(row=0, column=5, padx=5, pady=5)

options = ["none", "bold", "italic"]
font_option = StringVar()
font_option_drop = tk.OptionMenu(menu_frame, font_option, *options, command=change_font)
font_option.set("none")
# Set the width to be constant
font_option_drop.config(width=5)
font_option_drop.grid(row=0, column=6, padx=5, pady=5)

# Layout for the text frame
my_font = (font_family.get(), font_size.get())

# Create the input_text as a scrolltext so you can scroll through the text field
# Set the default width and height to be more than the window size so that on the smallest size, the text field size is constant
input_text = tk.scrolledtext.ScrolledText(text_frame, width="1000", height="100",  bg=text_color, font=my_font)
input_text.pack()

# Run the root window's main loop
root.mainloop()
