from tkinter import *
from tkinter import filedialog as fd
from PIL import Image
from tkinter import messagebox
 
root = Tk()
root.title("Basic Image converter App")
 
def jpg_to_png():           # function of converting jeg to png
    global im1
 
    import_filename = fd.askopenfilename()              # import the image from the folder
    if import_filename.endswith(".jpg"):
 
        im1 = Image.open(import_filename)
 
        export_filename = fd.asksaveasfilename(defaultextension=".png")                     # after converting the image save to desired  location with the Extersion .png
        im1.save(export_filename)

        messagebox.showinfo("success ", "your Image converted to Png")
    else:
        Label_2 = Label(root, text="Error!", width=20,fg="red", font=("bold", 15))          # if not with jpg extension then display error message
        Label_2.place(x=80, y=280)
        messagebox.showerror("Fail!!", "Something Went Wrong...")
 
 
button1 = Button(root, text="JPG to PNG", width=20, height=2, bg="orange",fg="black", font=("helvetica", 12, "bold"), command=jpg_to_png)
button1.place(x=120, y=120)
 
root.geometry("450x400")
root.mainloop()