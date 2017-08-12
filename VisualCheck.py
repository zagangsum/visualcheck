__author__ = 'gareth.cripps'
import time
from Tkinter import *

from PIL import Image, ImageTk

global run_at
global delay
from datetime import datetime

global fName
fName = 'Hovis.jpg'
global flist
global xsize
global ysize
global buttext
global remoteFileList
global localFileList
global currButSet
global butYpos
global butitems

LineID ="Line 1"
global firstRun
import os
firstRun = 1

from apscheduler.schedulers.background import BackgroundScheduler

class App(Frame):
    def __init__(self, master):

        self.tk = Tk()
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.state = False
        Frame.__init__(self, master)
        self.master = master
        pad = 2
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.original = Image.open(fName)
        self.image = ImageTk.PhotoImage(self.original)
        self.display = Canvas(self, bd=0, highlightthickness=0)
        self.display.create_image(0, 1, image=self.image, anchor=NE, tags="IMG")
        self.display.grid(row=0, sticky=W+E+N+S)
        self.pack(side="right", )
        self.pack(fill=BOTH, expand=1)
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        #size = (event.width, event.height)
        global xsize
        global ysize
        xsize = event.width
        ysize = event.height
        size = (xsize-22, ysize-120)
        resized = self.original.resize(size,Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display.delete("IMG")
        self.display.create_image(11, 42, image=self.image, anchor=NW, tags="IMG")

    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

    def change_image(self, btext):
            fName = btext
            self.original = Image.open(fName)
            self.image = ImageTk.PhotoImage(self.original)
            self.display.delete("IMG")
            self.display = Canvas(self, bd=0, highlightthickness=0)
            self.display.create_image(0, 1, image=self.image, anchor=NW, tags="IMG")
            self.display.grid(row=0, sticky=W+E+N+S)
            self.pack(side="right", )
            self.pack(fill=BOTH, expand=1)
            self.bind("<Configure>", self.resize)
            size = (xsize-22, ysize-120)
            resized = self.original.resize(size,Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(resized)
            self.display.delete("IMG")
            self.display.create_image(11, 42, image=self.image,anchor=NW, tags="IMG")
            return 1

    def change_buttons_next(self, changeButSet):

        if changeButSet == 0:
            root.currButSet = 0
            butwidth = int(xsize/10.5)
            dirbutwidth = xsize-(butwidth*10)
            butlabel = Label(root, font=('times', 25, 'bold'), bg='grey')
            butlabel.place(x=0, y=butYpos, width=xsize, height=40)
            if butitems > 0:
                button1 = Button(root, font=('arial', 12, 'bold'), text=buttext[0], command=lambda: app.change_image(btext=flist[0]))
                button1.place(x=1, y=butYpos, width=butwidth, height=40)
            if butitems > 1:
                button2 = Button(root, font=('arial', 12, 'bold'), text=buttext[1], command=lambda: app.change_image(btext=flist[1]))
                button2.place(x=butwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 2:
                button3 = Button(root, font=('arial', 12, 'bold'), text=buttext[2], command=lambda: app.change_image(btext=flist[2]))
                button3.place(x=(2*butwidth)+1, y=butYpos, width=butwidth, height=40)
            if butitems > 3:
                button4 = Button(root, font=('arial', 12, 'bold'), text=buttext[3], command=lambda: app.change_image(btext=flist[3]))
                button4.place(x=(3*butwidth)+1, y=butYpos, width=butwidth, height=40)
            if butitems > 4:
                button5 = Button(root, font=('arial', 12, 'bold'), text=buttext[4], command=lambda: app.change_image(btext=flist[4]))
                button5.place(x=(4*butwidth)+1, y=butYpos, width=butwidth, height=40)
            if butitems > 5:
                button6 = Button(root, font=('arial', 12, 'bold'), text=buttext[5], command=lambda: app.change_image(btext=flist[5]))
                button6.place(x=(5*butwidth)+1, y=butYpos, width=butwidth, height=40)
            if butitems > 6:
                button7 = Button(root, font=('arial', 12, 'bold'), text=buttext[6], command=lambda: app.change_image(btext=flist[6]))
                button7.place(x=(6*butwidth)+1, y=butYpos, width=butwidth, height=40)
            if butitems > 7:
                button8 = Button(root, font=('arial', 12, 'bold'), text=buttext[7], command=lambda: app.change_image(btext=flist[7]))
                button8.place(x=(7*butwidth)+1, y=butYpos, width=butwidth, height=40)
            if butitems > 8:
                button9 = Button(root, font=('arial', 12, 'bold'), text=buttext[8], command=lambda: app.change_image(btext=flist[8]))
                button9.place(x=(8*butwidth)+1, y=butYpos, width=butwidth, height=40)
            if butitems > 9:
                button10 = Button(root, font=('arial', 12, 'bold'), text=buttext[9], command=lambda: app.change_image(btext=flist[9]))
                button10.place(x=(9*butwidth)+1, y=butYpos, width=butwidth, height=40)
                buttonNext = Button(root, font=('arial', 12, 'bold'), text='>', command=lambda: app.change_buttons_next(1))
                buttonNext.place(x=xsize-dirbutwidth+1, y=butYpos, width=dirbutwidth, height=40)

        elif changeButSet == 1:
            root.currButSet = 1
            butlabel = Label(root, font=('times', 25, 'bold'), bg='grey')
            butlabel.place(x=0, y=butYpos, width=xsize, height=40)
            butwidth = int(xsize/11)
            dirbutwidth = butwidth/2
            buttonBack = Button(root, font=('arial', 12, 'bold'), text='<', command=lambda: app.change_buttons_next(0))
            buttonBack.place(x=1, y=butYpos, width=dirbutwidth, height=40)
            if butitems > 10:
                button11 = Button(root, font=('arial', 12, 'bold'), text=buttext[10], command=lambda: app.change_image(btext=flist[10]))
                button11.place(x=dirbutwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 11:
                button12 = Button(root, font=('arial', 12, 'bold'), text=buttext[11], command=lambda: app.change_image(btext=flist[11]))
                button12.place(x=(1*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 12:
                button13 = Button(root, font=('arial', 12, 'bold'), text=buttext[12], command=lambda: app.change_image(btext=flist[12]))
                button13.place(x=(2*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 13:
                button14 = Button(root, font=('arial', 12, 'bold'), text=buttext[13], command=lambda: app.change_image(btext=flist[13]))
                button14.place(x=(3*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 14:
                button15 = Button(root, font=('arial', 12, 'bold'), text=buttext[14], command=lambda: app.change_image(btext=flist[14]))
                button15.place(x=(4*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 15:
                button16 = Button(root, font=('arial', 12, 'bold'), text=buttext[15], command=lambda: app.change_image(btext=flist[15]))
                button16.place(x=(5*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 16:
                button17 = Button(root, font=('arial', 12, 'bold'), text=buttext[16], command=lambda: app.change_image(btext=flist[16]))
                button17.place(x=(6*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 17:
                button18 = Button(root, font=('arial', 12, 'bold'), text=buttext[17], command=lambda: app.change_image(btext=flist[17]))
                button18.place(x=(7*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 18:
                button19 = Button(root, font=('arial', 12, 'bold'), text=buttext[18], command=lambda: app.change_image(btext=flist[18]))
                button19.place(x=(8*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 19:
                button20 = Button(root, font=('arial', 12, 'bold'), text=buttext[19], command=lambda: app.change_image(btext=flist[19]))
                button20.place(x=(9*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
                buttonNext = Button(root, font=('arial', 12, 'bold'), text='>', command=lambda: app.change_buttons_next(2))
                buttonNext.place(x=xsize-dirbutwidth+1, y=butYpos, width=dirbutwidth+4, height=40)

        elif changeButSet == 2:
            root.currButSet = 2
            butlabel = Label(root, font=('times', 25, 'bold'), bg='grey')
            butlabel.place(x=1, y=butYpos, width=xsize, height=40)
            butwidth = int(xsize/11)
            dirbutwidth = butwidth/2
            buttonBack = Button(root, font=('arial', 12, 'bold'), text='<', command=lambda: app.change_buttons_next(1))
            buttonBack.place(x=0, y=butYpos, width=dirbutwidth, height=40)
            if butitems > 20:
                button21 = Button(root, font=('arial', 12, 'bold'), text=buttext[20], command=lambda: app.change_image(btext=flist[20]))
                button21.place(x=dirbutwidth, y=butYpos, width=butwidth, height=40)
            if butitems > 21:
                button22 = Button(root, font=('arial', 12, 'bold'), text=buttext[21], command=lambda: app.change_image(btext=flist[21]))
                button22.place(x=(1*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 22:
                button23 = Button(root, font=('arial', 12, 'bold'), text=buttext[22], command=lambda: app.change_image(btext=flist[22]))
                button23.place(x=(2*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 23:
                button24 = Button(root, font=('arial', 12, 'bold'), text=buttext[23], command=lambda: app.change_image(btext=flist[23]))
                button24.place(x=(3*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 24:
                button25 = Button(root, font=('arial', 12, 'bold'), text=buttext[24], command=lambda: app.change_image(btext=flist[24]))
                button25.place(x=(4*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 25:
                button26 = Button(root, font=('arial', 12, 'bold'), text=buttext[25], command=lambda: app.change_image(btext=flist[25]))
                button26.place(x=(5*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 26:
                button27 = Button(root, font=('arial', 12, 'bold'), text=buttext[26], command=lambda: app.change_image(btext=flist[26]))
                button27.place(x=(6*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 27:
                button28 = Button(root, font=('arial', 12, 'bold'), text=buttext[27], command=lambda: app.change_image(btext=flist[27]))
                button28.place(x=(7*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 28:
                button29 = Button(root, font=('arial', 12, 'bold'), text=buttext[18], command=lambda: app.change_image(btext=flist[18]))
                button29.place(x=(8*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
            if butitems > 29:
                button30 = Button(root, font=('arial', 12, 'bold'), text=buttext[19], command=lambda: app.change_image(btext=flist[19]))
                button30.place(x=(9*butwidth)+dirbutwidth+1, y=butYpos, width=butwidth, height=40)
                buttonNext = Button(root, font=('arial', 12, 'bold'), text='>', command=lambda: app.change_buttons_next(2))
                buttonNext.place(x=xsize-dirbutwidth, y=butYpos, width=dirbutwidth, height=40)

            return



root = Tk()

# If you only want to remove max, min and resize button below line is sufficient
root.overrideredirect(True)
# above line will helpful in designing flash screens

# To display the screen in full screen mode
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
xsize = root.winfo_screenwidth()
ysize = root.winfo_screenheight()
butYpos = ysize - 79

app = App(root)
toplabel = Label(root, font=('times', 25, 'bold'), bg='yellow')
toplabel.config(text=' ')
toplabel.place(x=0, y=0, width=xsize, height=40)
butitems = 0

def parse_files():
    global butitems
    global butwidth
    global currButSet
    global firstRun
    global fName
    global flist
    global buttext
    flist = []
    buttext = []
    print datetime.now()
    print 'Pasing files'
    for dirname, dirnames, filenames in os.walk('.'):
        # print path to all subdirectories first.

        for subdirname in dirnames:
            print os.path.join(dirname, subdirname)
            # sysPath = os.path.join(dirname, subdirname)
        # print path to all filenames.

            for filename in filenames:
                if filename != "Hovis.jpg":
                    extensiontest = filename[-3:]
                    if extensiontest == "jpg" or extensiontest == "JPG":
                        #print filename
                        flist.append(filename)
                        filename = filename[:4]
                        buttext.append(filename)
                        butitems += 1
                    #print butitems
            if butitems < 9:
                butwidth = (xsize/10)
                currButSet = 0
            elif butitems > 9 and butitems < 20:
                butwidth = (xsize/10)-5
                currButSet = 0
            elif butitems > 19 and butitems < 30:
                butwidth = (xsize/10)-10
                currButSet = 0
            elif butitems > 29 and butitems < 40:
                butwidth = (xsize/10)-10
                currButSet = 0
            currButSet = 0
            #destroy_buttons(currButSet)
            app.change_buttons_next(currButSet)


        if firstRun == 1:
            currButSet = 0
            firstRun = 0
            app.change_buttons_next(currButSet)


def training_matrix():
    app.change_image("Hovis.jpg") #well
    return


parse_files()

scheduler = BackgroundScheduler()
scheduler.add_job(parse_files, 'interval', seconds=300)
scheduler.start()

buttonExit = Button(root, font=('arial', 12, 'bold'), text="Exit", command=quit, bg='cyan', fg='black')
buttonExit.place(x=(xsize-121), y=1, width=120, height=40)
buttonRefresh = Button(root, font=('arial', 12, 'bold'), text="Refresh", command=lambda: parse_files(), bg='cyan', fg='black')
buttonRefresh.place(x=(xsize-242), y=1, width=120, height=40)

buttonTraining = Button(root, font=('arial', 12, 'bold'), text="Training", command=lambda: training_matrix(), bg='cyan', fg='black')
buttonTraining.place(x=(xsize-363), y=1, width=120, height=40)

time1 = ''
clock = Label(root, font=('times', 25, 'bold'), bg='yellow')
clock.place(x=(xsize/2)-120, y=0, width=240, height=40)

line = Label(root, font=('times', 25, 'bold'), bg='cyan')
line.place(x=1, y=0, width=120, height=40)
datelabel = Label(root, font=('times', 25, 'bold'), bg='yellow')
datelabel.place(x=121, y=0, width=240, height=40)

def tick():
    global time1
    global run_at
    global now
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')

    datetext = time.strftime("%d/%m/%Y")


    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        line.config(text=LineID)
        datelabel.config(text=datetext)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)

tick()
app.mainloop()
root.destroy()


