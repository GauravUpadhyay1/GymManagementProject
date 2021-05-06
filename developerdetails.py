from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.title("GYM MANAGEMENT SYSTEM")
        self.root.geometry("800x450+170+50")

        imgfoot = Image.open(r"E:\Python\Projects\project-3-gym\img\10.jpeg")
        imgfoot = imgfoot.resize((400, 400), Image.ANTIALIAS)
        self.photoimgfoot = ImageTk.PhotoImage(imgfoot)

        lblimgfoot = Label(
            self.root, image=self.photoimgfoot)
        lblimgfoot.place(x=0, y=20, width=400, height=400)

        lbl = LabelFrame(self.root, font=("times new roman",
                         11, "bold"), padx=2, bd=4, relief=RIDGE)
        lbl.place(x=400, y=20, width=398, height=400)

        lbl1 = Label(
            lbl, text="Made By:", font=("times new roman",
                                        18, "bold"))
        lbl1.place(x=10, y=30)

        lbl2 = Label(
            lbl, text="Gaurav Upadhyay", font=("times new roman",
                                               18, "bold"))
        lbl2.place(x=140, y=30)

        lblimg3 = Label(
            lbl, text="Targeted Users:", font=("times new roman",
                                               13, "bold"))
        lblimg3.place(x=10, y=100)

        lblimg4 = Label(
            lbl, text="Gym Owners and Managers", font=("times new roman",
                                                       13, "bold"))
        lblimg4.place(x=140, y=100)

        lblimg5 = Label(
            lbl, text="Contact me:", font=("times new roman",
                                           13, "bold"))
        lblimg5.place(x=10, y=170)

        lblimg6 = Label(
            lbl, text="9654494467", font=("times new roman",
                                          13, "bold"))
        lblimg6.place(x=140, y=170)

        lblimg52 = Label(
            lbl, text="Email me:", font=("times new roman",
                                         13, "bold"))
        lblimg52.place(x=10, y=240)

        lblimg62 = Label(
            lbl, text="gupadhyay8080@gmail.com", font=("times new roman",
                                                       13, "bold"))
        lblimg62.place(x=140, y=240)

        lblimg522 = Label(
            lbl, text="My Instagram", font=("times new roman",
                                            13, "bold"))
        lblimg522.place(x=10, y=310)

        lblimg622 = Label(
            lbl, text="@gauravupadhyayyy", font=("times new roman",
                                                 13, "bold"))
        lblimg622.place(x=140, y=310)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
