from tkinter import *
from tkinter import ttk
import os
from PIL import Image, ImageTk

guiFrame = Tk()
guiFrame.title("OS PBL")
guiFrame.geometry("500x500")
svar = StringVar()
deli = 150           # milliseconds of delay per character
labl = Label(guiFrame, textvariable=svar, height=15 )
#image2 = Image.open('C:\\Users\\dhruv\\Desktop\\Wallpaper\\.jpg')
#image1 = ImageTk.PhotoImage(image2)
#w = image1.width()
#h = image1.height()
#guiFrame.geometry('%dx%d+0+0' % (w,h))


class GUI(Frame):

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.grid()

        self.fnameLabel = Label(master, text="First Name")
        #self.fnameLabel.grid(row = 1, column = 1)
        self.fnameLabel.place(relx = 0.12, rely = 0.10, anchor = CENTER)

        self.fnameEntry = StringVar()
        self.fnameEntry = Entry(textvariable=self.fnameEntry)
        #self.fnameEntry.grid(row = 1, column = 7)
        self.fnameEntry.place(relx = 0.45, rely = 0.10, anchor = CENTER)

        self.lnameLabel = Label(master, text="Last Name")
        #self.lnameLabel.grid(row = 5, column = 1)
        self.lnameLabel.place(relx = 0.12, rely = 0.15, anchor = CENTER)

        self.lnameEntry = StringVar()
        self.lnameEntry = Entry(textvariable=self.lnameEntry)
        #self.lnameEntry.grid(row = 5, column = 7)
        self.lnameEntry.place(relx = 0.45, rely = 0.15, anchor = CENTER)


        #  lc command
        def buttonClick():
            os.system("start cmd")
            os.system('cmd /k "dir"')
            print("\nYou Explored ls command!")
            print(self.fnameEntry.get() + " " + self.lnameEntry.get() +", you clicked the ls command button!!!")

        self.submitButton = Button(master, text="ls Command", command=buttonClick)
        #self.submitButton.grid(row = 6, column = 1)
        self.submitButton.place(relx = 0.15, rely = 0.25, anchor = CENTER)


        # write content in file
        def buttonClick():
        
            R = input("\nEnter the file name with extension : ")
            F = open(R,"a+")
            Str = input("Enter the text : ")
            F.write(Str)
    
            print("\nYou Wrote content in the file!")
            print(self.fnameEntry.get() + " " + self.lnameEntry.get() +", you clicked the Write in file button!!!")

        self.submitButton = Button(master, text="Write in file", command=buttonClick)
        #self.submitButton.grid(row = 6, column = 1)
        self.submitButton.place(relx = 0.35, rely = 0.25, anchor = CENTER)

        # read content in file
        def buttonClick():
            R = input("\nEnter the file name with extension : ")
            F = open(R,"r+")            
            contents = F.read()
            print("Contents of the file are : " + contents)
                
            print("\nYou read the content in the file!")
            print(self.fnameEntry.get() + " " + self.lnameEntry.get() +", you clicked the Read file button!!!")

        self.submitButton = Button(master, text="Read file", command=buttonClick)
        #self.submitButton.grid(row = 6, column = 1)
        self.submitButton.place(relx = 0.15, rely = 0.35, anchor = CENTER)

        # open a file
        def buttonClick():
            R = input("\nEnter the file name with extension : ")
            osCommandString = "notepad.exe " + R
            os.system(osCommandString)
            #F = open(R,"w+")
            #Str = input("Enter the text : ")
            #F.write(Str)    
            print("\nYou Opened the file!")
            print(self.fnameEntry.get() + " " + self.lnameEntry.get() +", you clicked the Open file button!!!")

        self.submitButton = Button(master, text="Open file", command=buttonClick)
        #self.submitButton.grid(row = 6, column = 1)
        self.submitButton.place(relx = 0.35, rely = 0.35, anchor = CENTER)

        # quit button
        def buttonClick():    
            print(self.fnameEntry.get() + " " + self.lnameEntry.get() +", you clicked the Quit button!!!")

        self.submitButton = Button(master, text="Quit", fg = "red", command=quit)
        #self.submitButton.grid(row = 6, column = 1)
        self.submitButton.place(relx = 0.25, rely = 0.45, anchor = CENTER)

        # running text
        def shif():
            shif.msg = shif.msg[1:] + shif.msg[0]
            svar.set(shif.msg)
            guiFrame.after(deli, shif)

        shif.msg = ' Welcome to Operating System Project.              '
        shif()
        labl.place(relx = 0.30, rely = 0.55)

        # background image (This doesn't work. Find yourself other ocde to insert image in the GUI window and tell me also.)
##        def resize_image(event):
##            new_width = event.width
##            new_height = event.height
##            image = copy_of_image.resize((new_width, new_height))
##            photo = ImageTk.PhotoImage(image)
##            label1.config(image = photo)
##            label1.image = photo #avoid garbage collection
##
##        image = Image.open(r"image path.jpg")
##        copy_of_image = image.copy()
##        photo = ImageTk.PhotoImage(image)
##        label1 = guiFrame.Label(root, image = photo)
##        label1.bind('<Configure>', resize_image)
##        label1.pack(fill=BOTH, expand = YES)

if __name__ == "__main__":
    guiFrame = GUI()    
    guiFrame.mainloop()
