# Notepad
# icon http://www.doublejdesign.co.uk
import tkinter as tk

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


# Run the root window's main loop
root.mainloop()
