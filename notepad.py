# Notepad
# icon http://www.doublejdesign.co.uk
import tkinter as tk
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

# Define the layout
# Create frames
menu_frame = tk.Frame(root, bg=menu_color)
text_frame = tk.Frame(root, bg=text_color)
menu_frame.pack(padx=5, pady=5)
text_frame.pack(padx=5, pady=5)

# Layout for menu frame
# Create the menu: new, open, save, close, font family, font size, font option
new_image = ImageTk.PhotoImage(Image.open("img/new.png"))
new_button = tk.Button(menu_frame, image=new_image)
new_button.grid(row=0, column=0, padx=5, pady=5)

open_image = ImageTk.PhotoImage(Image.open("img/open.png"))
open_button = tk.Button(menu_frame, image=open_image)
open_button.grid(row=0, column=1, padx=5, pady=5)

save_image = ImageTk.PhotoImage(Image.open("img/save.png"))
save_button = tk.Button(menu_frame, image=save_image)
save_button.grid(row=0, column=2, padx=5, pady=5)

close_image = ImageTk.PhotoImage(Image.open("img/close.png"))
close_button = tk.Button(menu_frame, image=close_image, command=root.destroy)
close_button.grid(row=0, column=3, padx=5, pady=5)

# Run the root window's main loop
root.mainloop()
