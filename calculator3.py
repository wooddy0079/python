import sys
from tkinter import Tk, StringVar, Entry, Button


class calculator:
    def __init__(self):

        root = Tk()


        root.title("Calculator")

        self.string = StringVar()
        txtDisplay = Entry(root,textvariable = self.string,insertwidth = 1 , font = "Helvetica 17 bold")
        txtDisplay.grid(row = 0,column = 0,columnspan = 6)
        txtDisplay.focus()



        values = ["7","8","9","/","Clear",
                  "4","5","6","*","<-",
                  "1","2","3","-","=",
                  "0",".","%","+"]


        i = 0
        row = 1
        col = 0

        for txt in values:

            if(i==5):
                row = 2
                col = 0
            if(i==10):
                row = 3
                col = 0
            if(i==15):
                row = 4
                col = 0
            padx = 23
            pady = 23

            if(txt == "="):
                btn = Button(root,height = 2,width = 4,padx = padx,pady =pady,text = txt,
                             command = lambda:self.equals())
                btn.grid(row = row,column = col,columnspan = 2,rowspan = 2,padx = 1,pady =1)
            elif(txt == "<-"):
                btn = Button(root,height = 2,width = 4,padx = 10,pady = 10,text = txt,
                             command = lambda:self.DeleteText())
                btn.grid(row = row,column = col,columnspan = 2,rowspan = 1,padx = 1,pady =1)
            elif(txt == "Clear"):
                btn = Button(root,height = 2,width = 4,padx = 10,pady = 10,text = txt,
                             command = lambda:self.ClearText())
                btn.grid(row = row,column = col,columnspan = 2,rowspan = 1,padx = 1,pady =1)
            else:
                btn = Button (root,height = 2,width = 4,padx = 10,pady = 10,text = txt,
                              command = lambda txt=txt:self.addchar(txt))
                btn.grid(row = row,column = col,padx = 1,pady =1)

            col = col + 1
            i = i + 1
        root.mainloop()

    def equals(self):
            result = ""

            try:
                result = eval(self.string.get())
            except:
                result = "Error"
            self.string.set(result)


    def addchar(self,char):
            self.string.set(self.string.get() + (str(char)))


    def ClearText(self):
            self.string.set("")

    def DeleteText(self):
            self.string.set(self.string.get()[0:-1])


calculator()