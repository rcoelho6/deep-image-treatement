import tkinter as tk
from PIL import ImageTk, Image

#This creates the main window of an application
window = tk.Tk()
window.title("SEE image and ENTER its information")
window.geometry("600x400")
window.configure(background='grey')

# Create textbox in window
#text_widget = tk.Text(window)
#text_widget.insert('insert',"Enter image information here")
#text_widget.pack(anchor = "w", padx = 50, pady = 50)

#img = Label(self, image=render)
#img.image = render
#img.place(x=0, y=0)

#Start the GUI
window.mainloop()