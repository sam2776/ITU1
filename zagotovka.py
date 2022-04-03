from tkinter import *

i = 0
def page_qown():
   pass

def page_up():
   global i
   i += 1
   img = images[i % len(images)]
   canvas.create_image(0, 0, anchor=NW, image=img)


canvas_width = 200
canvas_height = 150

master = Tk()

canvas = Canvas(master, width=canvas_width, height=canvas_height, bg='white')

bt_Down = Button(master, text='<-', command=page_qown)
bt_Up = Button(master, text='->', command=page_up)
#
canvas.place(x=20, y=20)
bt_Down.place(x=50, y=200, width=30, height=30)
bt_Up.place(x=100, y=200, width=30, height=30)
img1 = PhotoImage(file="1.ppm")
img2 = PhotoImage(file="2.ppm")
img3 = PhotoImage(file="3.ppm")
images = [img1, img2, img3]

mainloop()