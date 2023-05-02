from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

# Add database name and password
mypass = "yaswanth"
mydatabase = "LMS"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library Management System")
root.minsize(width=400, height=400)
root.geometry("684x634")

# Take n greater than 0.25 and less than 5
same = True
n = 0.25

# background image
background_image = Image.open("lpulib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

# background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)

img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="green", bd=2)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Yaswanth's Library", bg='black', fg='white', font=('Times', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Add Book Details", bg='black', fg='green', command=addBook)
btn1.place(relx=0.28, rely=0.35, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List", bg='black', fg='green', command=View)
btn3.place(relx=0.28, rely=0.55, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book to Student", bg='black', fg='green', command=issueBook)
btn4.place(relx=0.28, rely=0.65, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='black', fg='green', command=returnBook)
btn5.place(relx=0.28, rely=0.45, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='black', fg='red', command=delete)
btn2.place(relx=0.28, rely=0.75, relwidth=0.45, relheight=0.1)


# function to quit the application
def close():
    root.after(100, root.destroy())


btn6 = Button(root, text="Quit", bg='black', fg='red', command=close)
btn6.place(relx=0.28, rely=0.85, relwidth=0.45, relheight=0.1)

root.mainloop()
