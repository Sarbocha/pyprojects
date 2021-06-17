from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Pandey Rocks")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/gui/images", title="select a file",filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image)


my_btn = Button(root, text="Open Files", command=open).pack()

root.mainloop()
