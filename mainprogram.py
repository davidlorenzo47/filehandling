from tkinter import *
import os
from PIL import Image, ImageTk

guiFrame = Tk()
guiFrame.title("OS PBL")
guiFrame.geometry("500x500")


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

if __name__ == "__main__":
    guiFrame = GUI()    
    guiFrame.mainloop()
