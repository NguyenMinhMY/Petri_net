import time
import _thread
import tkinter as tk
import tkinter.font as tk_font
from tkinter.constants import END, INSERT, SOLID
from tkinter.font import BOLD, Font
from tkinter.ttk import *
from tkinter import *
import tkinter.messagebox as mbox
from tkinter import image_names, scrolledtext
from PIL import ImageTk, Image 
def create_circle(x, y, r, canvasName): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1)
class HomePage(tk.Frame):
    def __init__(self,parent,appController):
        tk.Frame.__init__(self,parent)
        image = Image.open("MVP_logo.png")
        photo = ImageTk.PhotoImage(image.resize((196, 196), Image.AFFINE))
        label = Label(self,image=photo, bg='#bfd6f6')
        label.image = photo
        label.place(x=280,y=100)

        self.configure(bg = "#bfd6f6")

        ft = Font(family="Times",size = 30,weight=BOLD)
        lbl = tk.Label(self,text="Welcome to team MVP",font=ft,fg="#c68642",bg="#bfd6f6")
        lbl.place(x=200,y=50)

        button_1 = tk.Button(self,text="Item 1: Specialist network",bg="#84c1ff",font=("Times",10),width=40,command=lambda: appController.showPage(Item_1))
        button_1.place(x=240,y=310)

        button_2 = tk.Button(self,text="Item 2: Patient network",bg="#84c1ff",font=("Times",10),width=40,command=lambda: appController.showPage(Item_2))
        button_2.place(x=240,y=360)

        button_3 = tk.Button(self,text="Item 3: Superimposed network",bg="#84c1ff",font=("Times",10),width=40,command=lambda: appController.showPage(Item_3))
        button_3.place(x=240,y=410)

        button_4 = tk.Button(self,text="Item 4: Reachable marking",bg="#84c1ff",font=("Times",10),width=40,command=lambda: appController.showPage(Item_4))
        button_4.place(x=240,y=460)

        button_5 = tk.Button(self,text="Item Enhanced: MVP",bg="#84c1ff",font=("Times",10),width=40,command=lambda: appController.showPage(Item_enhanced))
        button_5.place(x=240,y=510)
class Item_1(tk.Frame):
    def __init__(self,parent,appController):
        tk.Frame.__init__(self,parent)
        self.places = {'free':0,'busy':0,'docu':0}
        self.flagCheck = tk.BooleanVar()
        self.drawPetri(appController)
        self.showPetri()
    def drawPetri(self,appController):
        P = tk.Canvas(self,height= 600,width=800)
        P.pack()
        ft = Font(family="Times",size = 15,weight="bold")
        tk.Label(self,text="Item 1: Specialist network",font=ft).place(x=270,y=30)
        # Draw Places
        create_circle(250,215,20,P)
        tk.Label(self,text = "FREE", fg = "Black",font = ("Arial",8)).place(x=234 ,y=175)

        create_circle(370,300,20,P)
        tk.Label(self,text = "BUSY", fg = "Black",font = ("Arial",8)).place(x=354 ,y=260)

        create_circle(490,215,20,P)
        tk.Label(self,text = "DOCU", fg = "Black",font = ("Arial",8)).place(x=474,y=175)

        # Draw Flows
        P.create_line(250,235,250,280,arrow=tk.LAST)# free to start
        P.create_line(270,300,347,300,arrow=tk.LAST)# start to busy
        P.create_line(390,300,465,300,arrow=tk.LAST)# busy to change
        P.create_line(490,290,490,235,arrow=tk.LAST)# change to docu
        P.create_line(470,215,390,215,arrow=tk.LAST)# docu to end
        P.create_line(380,215,270,215,arrow=tk.LAST)# end to free

        # Draw Transitions
        self.T_Start = tk.Button(self,activebackground='yellow',relief=SOLID,bd=1,height=2,width=5,command=lambda:self.handleStart())
        self.T_Start.place(x=228,y=280)
        tk.Label(self,text="START",fg="black",font=("Arial",8)).place(x=207,y=260)
        self.T_Change = tk.Button(self,activebackground='yellow',relief=SOLID,bd=1,height=2,width=5,command=self.handleChange)
        self.T_Change.place(x = 468,y=280)
        tk.Label(self,text="CHANGE",font=("Arial",8)).place(x=493,y=260)
        self.T_End = tk.Button(self,activebackground='yellow',relief=SOLID,height=2,bd=1,width=5,command=self.handleEnd)
        self.T_End.place(x=347,y=195)
        tk.Label(self,text="END",font=("Arial",8)).place(x=355,y=175)

        # Add and draw ComboBox
        tk.Label(self,text="Enter a initial marking: M0 = [",font=('Arial',10)).place(x=40,y=110)

        self.combo_free = Combobox(self,width=5)
        self.combo_free['value'] = (0,1,2,3,4,5,6,7,8,9,10)
        self.combo_free.place(x=220,y=110)
        self.combo_free.current(0)
        tk.Label(self,text = ".Free, ",font=('Arial',10)).place(x=273,y=110)

        self.combo_busy = Combobox(self,width=5,state='readonly')
        self.combo_busy['value'] = (0,1,2,3)
        self.combo_busy.place(x=320,y=110)
        self.combo_busy.current(0)
        tk.Label(self,text = ".Busy, ",font=('Arial',10)).place(x=373,y=110)

        self.combo_docu = Combobox(self,width=5,state='readonly')
        self.combo_docu['value'] = (0,1,2)
        self.combo_docu.place(x=420,y=110)
        self.combo_docu.current(0)
        tk.Label(self,text = ".Docu ]",font=('Arial',10)).place(x=473,y=110)

        # Add some functions as checkbox, run, set, back, next,home
        back_button = tk.Button(self,text="Back",width=10,command=lambda: appController.showPage(HomePage))
        back_button.place(x=50,y=30)
        home_button = tk.Button(self,text = "Home", width= 10,command=lambda: appController.showPage(HomePage))
        home_button.place(x=50,y=60)
        next_button = tk.Button(self,text="Next",width=10,command=lambda: appController.showPage(Item_2))
        next_button.place(x=670,y=30)
        check_box = tk.Checkbutton(self,text="Auto firing",onvalue=1,offvalue=0,variable=self.flagCheck)
        check_box.place(x=600,y=108)
        run_button = tk.Button(self,text = "Run",width=8,command=lambda:_thread.start_new_thread(self.handleRun,()))
        run_button.place(x=690,y=108)
        set_button = tk.Button(self, text = "Set", command=self.handleSet,width=8)
        set_button.place(x=530,y=108)

        # The number of token in every place
        self.free = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.free.place(x =243, y = 205)

        self.busy = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.busy.place(x = 363, y = 290)
        tk.Label(self,text="k = 3",fg = "black",font=("Arial",10)).place(x=355,y=325)

        self.docu = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.docu.place(x = 483, y = 205)
        tk.Label(self,text="k = 2",fg = "black",font=("Arial",10)).place(x=515,y=205)

        # Show current marking
        self.marking = tk.Message(self,relief=SOLID,borderwidth=1,text=f"Current marking: [ {self.places['free']} Free, {self.places['busy']} Busy, {self.places['docu']} Docu]",font=("Time new Roman",13),width=400)
        self.marking.place(x=210,y=370)
    def handleRun(self):
        if(self.flagCheck.get()==1):
            time.sleep(1)
            while self.places['free'] > 0 or self.places['busy'] > 0 or self.places['docu'] > 0:
                if(self.flagCheck.get()==0):
                    return
                if self.places['free'] > 0 and self.places['busy']<3:
                    if(self.flagCheck.get()==0):
                        return
                    self.T_Start.configure(bg="yellow")
                    time.sleep(0.5)
                    self.places['busy']+=1
                    self.places['free']-=1
                    if(self.flagCheck.get()==0):
                        self.places['busy']-=1
                        self.places['free']+=1
                        return
                    self.showPetri()
                    time.sleep(1)
                    continue             
                if self.places['busy']>0 and self.places['docu']<2 :
                    if(self.flagCheck.get()==0):
                        return
                    self.T_Change.configure(bg="yellow")
                    time.sleep(0.5)
                    self.places['busy']-=1
                    self.places['docu']+=1
                    if(self.flagCheck.get()==0):
                        self.places['busy']+=1
                        self.places['docu']-=1
                        return
                    self.showPetri()
                    time.sleep(1)
                    continue
                if self.places['docu']>0:
                    if(self.flagCheck.get()==0):
                        return
                    self.T_End.configure(bg="yellow")
                    time.sleep(0.5)
                    self.places['docu']-=1
                    self.places['free']+=1
                    if(self.flagCheck.get()==0):
                        self.places['docu']+=1
                        self.places['free']-=1
                        return
                    self.showPetri()
                    time.sleep(1)
        else:
            return
    def handleSet(self):
        self.flagCheck.set(False)
        self.places['free'] = int(self.combo_free.get())
        if self.places['free'] <0 :
            mbox.showerror("Error","Invalid input: The number of tokens must be non-negative")
            self.places['free'] = 0
        self.places['busy'] = int(self.combo_busy.get())
        self.places['docu'] = int(self.combo_docu.get())
        self.showPetri()
        return
    def handleStart(self):
        if self.flagCheck.get()==False:
            if self.places['free']>0 :
                if self.places['busy'] < 3:
                    self.showPetri()
                    self.places['free']-=1
                    self.places['busy']+=1
                    self.showPetri()
                else:
                    mbox.showwarning("Warning", "The place Busy only can contain at most 3 tokens.")
            else:
                mbox.showerror("Error","The transition Start is not enable.") 
    def handleChange(self):
        if self.flagCheck.get()==False:
            if self.places['busy']>0:
                if self.places['docu']<2:
                    self.showPetri()
                    self.places['docu']+=1
                    self.places['busy']-=1
                    self.showPetri()
                else:
                    mbox.showwarning("Warning"," The place Docu only can contain at most 2 tokens.")
            else:
                mbox.showerror("Error","The transition Change is not enable.")
    def handleEnd(self):
        if self.flagCheck.get()==False:
            if self.places['docu']>0:
                self.showPetri()
                self.places['docu']-=1
                self.places['free']+=1
                self.showPetri()
            else:
                mbox.showerror("Error","The transition End is not enable.")
    def showPetri(self):
        if(self.places['free']>0):
            self.T_Start.configure(background='green')
        else:
            self.T_Start.configure(background='red')
        if(self.places['busy']>0):
            self.T_Change.configure(background='green')
        else:
            self.T_Change.configure(background='red')
        if(self.places['docu']>0 ):
            self.T_End.configure(background='green')
        else:
            self.T_End.configure(background='red')
        self.marking.configure(text=f"Current marking: [ {self.places['free']} Free, {self.places['busy']} Busy, {self.places['docu']} Docu ]")
        self.free.configure(text=self.places['free'])
        self.busy.configure(text=self.places['busy'])
        self.docu.configure(text = self.places['docu'])
class Item_2(tk.Frame):
    def __init__(self,parent,appController):
        tk.Frame.__init__(self,parent)
        self.places = {'wait':0,'inside':0,'done':0}
        self.flagCheck = tk.BooleanVar()
        self.drawPetri(appController)
        self.showPetri()
    def drawPetri(self,appController):
        P = tk.Canvas(self,height= 600,width=800)
        P.pack()
        ft = Font(family="Times",size = 15,weight="bold")
        tk.Label(self,text="Item 2: Patient network",font=ft).place(x=270,y=30)

        create_circle(120,300,20,P)
        tk.Label(self,text = "WAIT", fg = "Black",font = ("Arial",8)).place(x=104 ,y=260)

        create_circle(370,300,20,P)
        tk.Label(self,text = "INSIDE", fg = "Black",font = ("Arial",8)).place(x=354 ,y=260)

        create_circle(630,300,20,P)
        tk.Label(self,text = "DONE", fg = "Black",font = ("Arial",8)).place(x=614 ,y=260)

        # Draw Flows
        P.create_line(140,300,225,300,arrow=tk.LAST)# wait to start
        P.create_line(270,300,347,300,arrow=tk.LAST)# start to inside
        P.create_line(390,300,465,300,arrow=tk.LAST)# inside to change
        P.create_line(490,300,610,300,arrow=tk.LAST)# change to done

        # Draw Transitions
        self.T_Start = tk.Button(self,activebackground='yellow',relief=SOLID,bd=1,height=2,width=5,command=lambda:self.handleStart())
        self.T_Start.place(x=228,y=280)
        tk.Label(self,text="START",fg="black",font=("Arial",8)).place(x=228,y=260)
        self.T_Change = tk.Button(self,activebackground='yellow',relief=SOLID,bd=1,height=2,width=5,command=self.handleChange)
        self.T_Change.place(x = 468,y=280)
        tk.Label(self,text="CHANGE",font=("Arial",8)).place(x=468,y=260)

        # Add and draw ComboBox
        tk.Label(self,text="Enter a initial marking: M0 = [",font=('Arial',10)).place(x=40,y=110)

        self.combo_wait = Combobox(self,width=5,state='readonly')
        self.combo_wait['value'] = (0,1,2,3,4,5,6,7,8,9,10)
        self.combo_wait.place(x=220,y=110)
        self.combo_wait.current(0)
        tk.Label(self,text = ".Wait, ",font=('Arial',10)).place(x=273,y=110)

        self.combo_inside = Combobox(self,width=5,state='readonly')
        self.combo_inside['value'] = (0,1,2,3)
        self.combo_inside.place(x=320,y=110)
        self.combo_inside.current(0)
        tk.Label(self,text = ".Inside, ",font=('Arial',10)).place(x=373,y=110)

        self.combo_done = Combobox(self,width=5)
        self.combo_done['value'] = (0,1,2,3,4,5,6,7,8,9,10)
        self.combo_done.place(x=420,y=110)
        self.combo_done.current(0)
        tk.Label(self,text = ".Done ]",font=('Arial',10)).place(x=473,y=110)

        # Add some functions as checkbox, run, set, back, next
        back_button = tk.Button(self,text="Back",width=10,command=lambda: appController.showPage(Item_1))
        back_button.place(x=50,y=30)
        home_button = tk.Button(self,text = "Home", width= 10,command=lambda: appController.showPage(HomePage))
        home_button.place(x=50,y=60)
        next_button = tk.Button(self,text="Next",width=10,command=lambda: appController.showPage(Item_3))
        next_button.place(x=670,y=30)
        check_box = tk.Checkbutton(self,text="Auto firing",onvalue=1,offvalue=0,variable=self.flagCheck)
        check_box.place(x=600,y=108)
        run_button = tk.Button(self,text = "Run",width=8,command=lambda:_thread.start_new_thread(self.handleRun,()))
        run_button.place(x=690,y=108)
        set_button = tk.Button(self, text = "Set", command=self.handleSet,width=8)
        set_button.place(x=530,y=108)

        # The number of token in every place
        self.wait = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.wait.place(x =110, y = 290)
        tk.Label(self,text="k = 10",fg = "black",font=("Arial",10)).place(x=103,y=325)

        self.inside = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.inside.place(x = 363, y = 290)
        tk.Label(self,text="k = 3",fg = "black",font=("Arial",10)).place(x=355,y=325)

        self.done = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.done.place(x = 620, y = 290)

        # Show current marking
        self.marking = tk.Message(self,relief=SOLID,borderwidth=1,text=f"Current marking: [ {self.places['wait']} Wait, {self.places['inside']} Inside, {self.places['done']} Done]",font=("Time new Roman",13),width=400)
        self.marking.place(x=210,y=370)
    def handleRun(self):
        time.sleep(1)
        if(self.flagCheck.get()==True):
            while self.places['wait']>0 or self.places['inside']>0:
                if self.flagCheck.get() == False:
                    return
                if(self.places['inside']<3) and self.places['wait']>0:
                    if self.flagCheck.get() == False:
                        return
                    self.T_Start.configure(bg="yellow")
                    time.sleep(0.5)
                    self.places['inside']+=1
                    self.places['wait']-=1
                    if self.flagCheck.get() == False:
                        self.places['inside']-=1
                        self.places['wait']+=1   
                        return
                    self.showPetri()
                    time.sleep(1)  
                    continue           
                if self.places['inside'] > 0:
                    if self.flagCheck.get() == False:
                        return
                    self.T_Change.configure(bg="yellow")
                    time.sleep(0.5)
                    self.places['done']+=1
                    self.places['inside']-=1
                    if self.flagCheck.get() == False:
                        self.places['done']-=1
                        self.places['inside']+=1
                        return
                    self.showPetri()
                    time.sleep(1)
        else:
            return
    def handleSet(self):
        self.flagCheck.set(False)
        self.places['wait'] = int(self.combo_wait.get())
        self.places['inside'] = int(self.combo_inside.get())
        self.places['done'] = int(self.combo_done.get())
        self.showPetri()
        return
    def handleStart(self):
        if self.flagCheck.get()==False:
            if self.places['wait']>0 :
                if self.places['inside'] < 3:
                    self.showPetri()
                    self.places['wait']-=1
                    self.places['inside']+=1
                    self.showPetri()
                else:
                    mbox.showwarning("Warning", "The place Inside only can contain at most 3 tokens.")
            else:
                mbox.showerror("Error","The transition Start is not enable.")  
    def handleChange(self):
        if self.flagCheck.get()==False:
            if self.places['inside']>0 :
                self.showPetri()
                self.places['inside']-=1
                self.places['done']+=1
                self.showPetri()
            else:
                mbox.showerror("Error","The transition Change is not enable.")
    def showPetri(self):
        if(self.places['wait']>0):
            self.T_Start.configure(background='green')
        else:
            self.T_Start.configure(background='red')
        if(self.places['inside']>0):
            self.T_Change.configure(background='green')
        else:
            self.T_Change.configure(background='red')
        self.marking.configure(text="Current marking: [ "+f"{self.places['wait']} Wait, {self.places['inside']} Inside, {self.places['done']} Done"+"]")
        self.wait.configure(text = self.places['wait'])
        self.inside.configure(text=self.places['inside'])
        self.done.configure(text=self.places['done'])
class Item_3(tk.Frame):
    def __init__(self,parent,appController):
        tk.Frame.__init__(self,parent)
        self.places = {'free':0,'busy':0,'docu':0,'wait':0,'inside':0,'done':0}
        self.flagCheck = tk.BooleanVar()
        self.drawPetri(appController)
        self.showPetri()
    def drawPetri(self,appController):
        P = tk.Canvas(self,height= 600,width=800)
        P.configure()
        P.pack()
        ft = Font(family="Times",size = 15,weight="bold")
        tk.Label(self,text="Item 3: Superimposed network",font=ft).place(x=270,y=30)
        # Draw Places   
        create_circle(120,320,20,P)
        tk.Label(self,text = "WAIT", fg = "Black",font = ("Arial",8)).place(x=104 ,y=280)

        create_circle(250,235,20,P)
        tk.Label(self,text = "FREE", fg = "Black",font = ("Arial",8)).place(x=234 ,y=195)

        create_circle(370,320,20,P)
        tk.Label(self,text = "BUSY", fg = "Black",font = ("Arial",8)).place(x=354 ,y=280)

        create_circle(370,420,20,P)
        tk.Label(self,text = "INSIDE", fg = "Black",font = ("Arial",8)).place(x=354 ,y=380)

        create_circle(630,320,20,P)
        tk.Label(self,text = "DONE", fg = "Black",font = ("Arial",8)).place(x=614 ,y=280)

        create_circle(490,235,20,P)
        tk.Label(self,text = "DOCU", fg = "Black",font = ("Arial",8)).place(x=474,y=195)

        # Draw Flows
        P.create_line(140,320,225,320,arrow=tk.LAST)# wait to start
        P.create_line(250,255,250,300,arrow=tk.LAST)# free to start
        P.create_line(270,320,347,320,arrow=tk.LAST)# start to busy
        P.create_line(390,320,465,320,arrow=tk.LAST)# busy to change
        P.create_line(490,320,610,320,arrow=tk.LAST)# change to done
        P.create_line(490,310,490,255,arrow=tk.LAST)# change to docu
        P.create_line(470,235,390,235,arrow=tk.LAST)# docu to end
        P.create_line(380,235,270,235,arrow=tk.LAST)# end to free
        P.create_line(250,330,250,420)
        P.create_line(250,420,347,420,arrow=tk.LAST)# start to inside
        P.create_line(390,420,490,420)
        P.create_line(490,420,490,340,arrow=tk.LAST)# inside to change

        # Draw Transitions
        self.T_Start = tk.Button(self,activebackground='yellow',relief=SOLID,bd=1,height=2,width=5,command=lambda:self.handleStart())
        self.T_Start.place(x=228,y=300)
        tk.Label(self,text="START",fg="black",font=("Arial",8)).place(x=207,y=280)
        self.T_Change = tk.Button(self,activebackground='yellow',relief=SOLID,bd=1,height=2,width=5,command=self.handleChange)
        self.T_Change.place(x = 468,y=300)
        tk.Label(self,text="CHANGE",font=("Arial",8)).place(x=493,y=280)
        self.T_End = tk.Button(self,activebackground='yellow',relief=SOLID,height=2,bd=1,width=5,command=self.handleEnd)
        self.T_End.place(x=347,y=215)
        tk.Label(self,text="END",font=("Arial",8)).place(x=355,y=195)

        # Add and draw ComboBox
        tk.Label(self,text="Enter a initial marking: M0 = [",font=('Arial',10)).place(x=10,y=110)

        self.combo_wait = Combobox(self,width=5,state='readonly')
        self.combo_wait['value'] = (0,1,2,3,4,5,6,7,8,9,10)
        self.combo_wait.place(x=190,y=110)
        self.combo_wait.current(0)
        tk.Label(self,text = ".Wait, ",font=('Arial',10)).place(x=243,y=110)

        self.combo_free = Combobox(self,width=5)
        self.combo_free['value'] = (0,1,2,3,4,5,6,7,8,9,10)
        self.combo_free.place(x=290,y=110)
        self.combo_free.current(0)
        tk.Label(self,text = ".Free, ",font=('Arial',10)).place(x=343,y=110)

        self.combo_busy = Combobox(self,width=5,state='readonly')
        self.combo_busy['value'] = (0,1,2,3)
        self.combo_busy.place(x=390,y=110)
        self.combo_busy.current(0)
        tk.Label(self,text = ".Busy, ",font=('Arial',10)).place(x=443,y=110)

        self.combo_inside = Combobox(self,width=5,state='readonly')
        self.combo_inside['value'] = (0,1,2,3)
        self.combo_inside.place(x=490,y=110)
        self.combo_inside.current(0)
        tk.Label(self,text = ".Inside, ",font=('Arial',10)).place(x=543,y=110)

        self.combo_done = Combobox(self,width=5)
        self.combo_done['value'] = (0,1,2,3,4,5,6,7,8,9,10)
        self.combo_done.place(x=590,y=110)
        self.combo_done.current(0)
        tk.Label(self,text = ".Done, ",font=('Arial',10)).place(x=643,y=110)

        self.combo_docu = Combobox(self,width=5,state='readonly')
        self.combo_docu['value'] = (0,1,2)
        self.combo_docu.place(x=690,y=110)
        self.combo_docu.current(0)
        tk.Label(self,text = ".Docu ]",font=('Arial',10)).place(x=743,y=110)

        # Add some functions as checkbox, run, set, back, next
        back_button = tk.Button(self,text="Back",width=10,command=lambda: appController.showPage(Item_2))
        back_button.place(x=50,y=30)
        home_button = tk.Button(self,text = "Home", width= 10,command=lambda: appController.showPage(HomePage))
        home_button.place(x=50,y=60)
        next_button = tk.Button(self,text="Next",width=10,command=lambda: appController.showPage(Item_4))
        next_button.place(x=670,y=30)
        check_box = tk.Checkbutton(self,text="Auto firing",onvalue=1,offvalue=0,variable=self.flagCheck)
        check_box.place(x=330,y=148)
        run_button = tk.Button(self,text = "Run",width=10,command=lambda:_thread.start_new_thread(self.handleRun,()))
        run_button.place(x=420,y=148)
        set_button = tk.Button(self, text = "Set", command=self.handleSet,width=10)
        set_button.place(x=240,y=148)

        # The number of token in every place
        self.wait = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.wait.place(x = 110, y = 310)
        tk.Label(self,text="k = 10",fg = "black",font=("Arial",10)).place(x=100,y=345)

        self.free = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.free.place(x =243, y = 225)

        self.busy = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.busy.place(x = 363, y = 310)
        tk.Label(self,text="k = 3",fg = "black",font=("Arial",10)).place(x=355,y=345)

        self.inside = tk.Label(self,text= 0,fg = "black",font=("Arial",10)) 
        self.inside.place(x = 363, y = 410)
        tk.Label(self,text="k = 3",fg = "black",font=("Arial",10)).place(x=355,y=445)

        self.done = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.done.place(x = 620, y = 310)

        self.docu = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.docu.place(x = 483, y = 225)
        tk.Label(self,text="k = 2",fg = "black",font=("Arial",10)).place(x=515,y=225)

        # Show curent marking
        self.marking = tk.Message(self,relief=SOLID,borderwidth=1,width=580,text=f"Curent marking: [ {self.places['wait']} Wait, {self.places['free']} Free, {self.places['busy']} Busy, {self.places['inside']} Inside, {self.places['done']} Done, {self.places['docu']} Docu ]",font=("Time new Roman",13))
        self.marking.place(x=150,y=490)
    def handleRun(self):
        if(self.flagCheck.get()==1):
            time.sleep(1)
            while self.places['free']>0 or self.places['busy']>0 or self.places['docu']>0:
                if(self.flagCheck.get()==False):
                    return
                if self.places['free'] > 0 and self.places['wait']>0 and self.places['busy']<3:
                    if(self.flagCheck.get()==False):
                        return
                    self.T_Start.configure(bg="yellow")
                    time.sleep(0.5)
                    self.places['busy']+=1
                    self.places['free']-=1
                    self.places['wait']-=1
                    self.places['inside']+=1
                    if self.flagCheck.get() == False:
                        self.places['busy']-=1
                        self.places['free']+=1
                        self.places['wait']+=1
                        self.places['inside']-=1
                        return
                    self.showPetri()
                    time.sleep(1)
                    continue             
                if self.places['busy']>0 and self.places['inside']>0 and self.places['docu']<2 :
                    if(self.flagCheck.get()==False):
                        return
                    self.T_Change.configure(bg="yellow")
                    time.sleep(0.5)
                    self.places['busy']-=1
                    self.places['inside']-=1
                    self.places['done']+=1
                    self.places['docu']+=1
                    if self.flagCheck.get() == False:
                        self.places['busy']+=1
                        self.places['inside']+=1
                        self.places['done']-=1
                        self.places['docu']-=1
                        return
                    self.showPetri()
                    time.sleep(1)
                    continue
                if self.places['docu']>0:
                    if(self.flagCheck.get()==False):
                        return
                    self.T_End.configure(bg="yellow")
                    time.sleep(0.5)
                    self.places['docu']-=1
                    self.places['free']+=1
                    if self.flagCheck.get() == False:
                        self.places['docu']+=1
                        self.places['free']-=1
                        return
                    self.showPetri()
                    time.sleep(1)
        else:
            return
    def handleSet(self):
        self.flagCheck.set(False)
        self.places['wait'] = int(self.combo_wait.get())
        self.places['free'] = int(self.combo_free.get())
        self.places['busy'] = int(self.combo_busy.get())
        self.places['inside'] = int(self.combo_inside.get())
        self.places['done'] = int(self.combo_done.get())
        self.places['docu'] = int(self.combo_docu.get())
        if self.places['free'] <0 or self.places['done'] < 0 :
            if self.places['free'] <0:
                self.places['free'] = 0
            if self.places['done'] <0:
                self.places['done'] = 0
            mbox.showerror("Error","Invalid input: The number of tokens must be non-negative")
        if self.places['busy']!=self.places['inside']:
            mbox.showwarning('Warning','The number of patient(s) being treated is not equal to the number of specialist(s) treating for them.\nDo you want to continue?')
        self.showPetri()
        return
    def handleStart(self):
        if self.flagCheck.get()==False:
            if self.places['wait']>0 and self.places['free']>0:
                if self.places['busy']<3 and self.places['inside']<3:
                    self.showPetri()
                    self.places['wait']-=1
                    self.places['free']-=1
                    self.places['busy']+=1
                    self.places['inside']+=1
                    self.showPetri()
                else:
                    mbox.showwarning("Warning","Both of places Busy and Inside only can contain at most 3 tokens.")
            else:
                mbox.showerror("Error","The transition Start is not enable.") 
    def handleChange(self):
        if self.flagCheck.get()==False:
            if self.places['busy']>0 and self.places['inside']>0:
                if self.places['docu']<2:
                    self.showPetri()
                    self.places['busy']-=1
                    self.places['inside']-=1
                    self.places['done']+=1
                    self.places['docu']+=1
                    self.showPetri()
                else:
                    mbox.showwarning("Warning","The place Docu only can contain at most 2 tokens.")
            else:
                mbox.showerror("Error","The transition Change is not enable.")
    def handleEnd(self):
        if self.flagCheck.get()==False:
            if self.places['docu']>0:
                self.showPetri()
                self.places['docu']-=1
                self.places['free']+=1
                self.showPetri()
            else:
                mbox.showerror("Error","The transition End is not enable.")
    def showPetri(self):
        if(self.places['wait']>0 and self.places['free']>0):
            self.T_Start.configure(background='green')
        else:
            self.T_Start.configure(background='red')
        if(self.places['busy']>0 and self.places['inside']>0):
            self.T_Change.configure(background='green')
        else:
            self.T_Change.configure(background='red')
        if(self.places['docu']>0 ):
            self.T_End.configure(background='green')
        else:
            self.T_End.configure(background='red')
        self.marking.configure(text=f"Current marking: [ {self.places['wait']} Wait, {self.places['free']} Free, {self.places['busy']} Busy, {self.places['inside']} Inside, {self.places['done']} Done, {self.places['docu']} Docu ]")
        self.free.configure(text=self.places['free'])
        self.wait.configure(text = self.places['wait'])
        self.busy.configure(text=self.places['busy'])
        self.inside.configure(text = self.places['inside'])
        self.done.configure(text=self.places['done'])
        self.docu.configure(text = self.places['docu'])
class Item_4(tk.Frame):
    def __init__(self,parent,appController):
        tk.Frame.__init__(self,parent)
        self.places = {'free':0,'busy':0,'docu':0,'wait':0,'inside':0,'done':0}
        self.count = 1
        self.flag = {'set':False,'find':False}
        self.string = "Firing sequence:[]"
        self.draw(appController)
    def draw(self,appController):
        ft = Font(family="Times",size = 15,weight="bold")
        tk.Label(self,text="Item 4: Reachable marking\nApplied the specific context (with restrictions)",font=ft).place(x=220,y=30)
        # Add and draw ComboBox
        tk.Label(self,text="Enter a initial marking: M0 = [",font=('Arial',10)).place(x=10,y=110)

        self.combo_wait = Combobox(self,width=5,state='readonly')
        self.combo_wait['value'] = (0,1,2,3,4,5,6,7,8,9,10)
        self.combo_wait.place(x=190,y=110)
        self.combo_wait.current(0)
        tk.Label(self,text = ".Wait, ",font=('Arial',10)).place(x=243,y=110)

        self.combo_free = Combobox(self,width=5)
        self.combo_free['value'] = (0,1,2,3,4,5,6,7,8,9,10)
        self.combo_free.place(x=290,y=110)
        self.combo_free.current(0)
        tk.Label(self,text = ".Free, ",font=('Arial',10)).place(x=343,y=110)

        self.combo_busy = Combobox(self,width=5,state='readonly')
        self.combo_busy['value'] = (0,1,2,3)
        self.combo_busy.place(x=390,y=110)
        self.combo_busy.current(0)
        tk.Label(self,text = ".Busy, ",font=('Arial',10)).place(x=443,y=110)

        self.combo_inside = Combobox(self,width=5,state='readonly')
        self.combo_inside['value'] = (0,1,2,3)
        self.combo_inside.place(x=490,y=110)
        self.combo_inside.current(0)
        tk.Label(self,text = ".Inside, ",font=('Arial',10)).place(x=543,y=110)

        self.combo_done = Combobox(self,width=5)
        self.combo_done['value'] = (0,1,2,3,4,5,6,7,8,9,10)
        self.combo_done.place(x=590,y=110)
        self.combo_done.current(0)
        tk.Label(self,text = ".Done, ",font=('Arial',10)).place(x=643,y=110)

        self.combo_docu = Combobox(self,width=5,state='readonly')
        self.combo_docu['value'] = (0,1,2)
        self.combo_docu.place(x=690,y=110)
        self.combo_docu.current(0)
        tk.Label(self,text = ".Docu ]",font=('Arial',10)).place(x=743,y=110)

        # Add scrolled text
        self.st = scrolledtext.ScrolledText(self, width = 115, height = 24, font = ("Times New Roman",10))
        self.st.place(x=50,y=195)

        # Add some functions count, find, set, back
        back_button = tk.Button(self,text="Back",width=10,command=lambda: appController.showPage(Item_3))
        back_button.place(x=50,y=30)
        home_button = tk.Button(self,text = "Home", width= 10,command=lambda: appController.showPage(HomePage))
        home_button.place(x=50,y=60)
        next_button = tk.Button(self,text="Next",width=10,command=lambda: appController.showPage(Item_enhanced))
        next_button.place(x=670,y=30)
        find_button = tk.Button(self,text = "Find",width=10,command=self.handleFind)
        find_button.place(x=420,y=148)
        set_button = tk.Button(self, text = "Set", command=self.handleSet,width=10)
        set_button.place(x=280,y=148)
        Count_button = tk.Button(self,text="Count",width=10,command=self.handleCount)
        Count_button.place(x=570,y=148)
        self.count_text = tk.Text(self, width = 10,height=1, font = ("Times New Roman",10))
        self.count_text.place(x=660,y=152)
    def show_marking(self,wait,free,busy,inside,done,docu):
        self.st.insert(INSERT,f"Marking: [{wait}.Wait,{free}.Free,{busy}.Busy,{inside}.Inside,{done}.Done,{docu}.Docu]\n\n")
    def print_TS(self,wait,free,busy,inside,done,docu):
        self.st.insert(INSERT,self.string+'\n')
        self.show_marking(wait,free,busy,inside,done,docu)
        if (free > 0 and wait>0) or (busy>0 and inside>0) or docu>0:
            if (wait>0 and free >0) and (busy<3 and inside<3):
                str_temp = ",Start]"
                self.string = self.string[0:-1]
                self.string+=str_temp
                index = self.string.find('[')+1
                if self.string[index] == ',':
                    self.string = self.string[0:index] + self.string[index+1:]
                self.count+=1
                self.print_TS(wait-1,free-1,busy+1,inside+1,done,docu)
            if (inside>0 and busy>0) and docu <2:
                str_temp = ",Change]"
                self.string = self.string[0:-1]
                self.string+=str_temp
                self.count+=1
                self.print_TS(wait,free,busy-1,inside-1,done+1,docu+1)
            if docu>0 :           
                str_temp = ",End]"
                self.string = self.string[0:-1]
                self.string+=str_temp
                self.count+=1
                self.print_TS(wait,free+1,busy,inside,done,docu-1)
        else:
            return
    def handleCount(self):
        if self.flag['find']== True:
            self.count_text.delete("1.0","end")
            self.count_text.insert(END,f"{self.count}")
        else:
            mbox.showwarning('Warning','Please press button "Find" to count!')
    def handleFind(self):
        if self.flag['set'] == True:
            self.flag['find'] = True
            self.count = 1
            self.fixed_wait = self.places['wait']+self.places['free']
            self.fixed_free = self.places['free']
            self.st.delete('1.0',END)
            self.print_TS(self.places['wait'],self.places['free'],self.places['busy'],self.places['inside'],self.places['done'],self.places['docu'])
            self.string = "Firing sequence:[]"   
        else :
            mbox.showwarning('Waring','Please press button "Set" to find!')

    def handleSet(self):
        self.flag['set'] = True
        self.flag['find'] = False
        self.count = 1
        self.places['wait'] = int(self.combo_wait.get())
        self.places['free'] = int(self.combo_free.get())
        self.places['busy'] = int(self.combo_busy.get())
        self.places['inside'] = int(self.combo_inside.get())
        self.places['done'] = int(self.combo_done.get())
        self.places['docu'] = int(self.combo_docu.get())
        if self.places['free'] <0 or self.places['done'] < 0 :
            if self.places['free'] <0:
                self.places['free'] = 0
            if self.places['done'] <0:
                self.places['done'] = 0
            mbox.showerror("Error","Invalid input: The number of tokens must be non-negative")
        return
class Item_enhanced(tk.Frame):
    def __init__(self,parent,appController):
        tk.Frame.__init__(self,parent)
        self.places = {'free':0,'busy':0,'docu':0,'wait':0,'inside':0,'done':0,'home':0,'income':0}
        self.drawPetri(appController)
        self.showPetri()
    def drawPetri(self,appController):
        P = tk.Canvas(self,height= 600,width=800)
        P.configure()
        P.pack()
        ft = Font(family="Times",size = 15,weight="bold")
        tk.Label(self,text="Item Enhanced: MVP",font=ft).place(x=310,y=20)
        # Draw Places   

        create_circle(470,130,20,P)
        tk.Label(self,text="INCOME",fg="Black",font=("Arial",8)).place(x=451,y=90)

        create_circle(70,370,20,P)
        tk.Label(self,text="HOME",fg="Black",font=("Arial",8)).place(x=74,y=330)

        create_circle(270,370,20,P)
        tk.Label(self,text = "WAIT", fg = "Black",font = ("Arial",8)).place(x=254 ,y=330)

        create_circle(350,285,20,P)
        tk.Label(self,text = "FREE", fg = "Black",font = ("Arial",8)).place(x=334 ,y=245)

        create_circle(470,370,20,P)
        tk.Label(self,text = "BUSY", fg = "Black",font = ("Arial",8)).place(x=454 ,y=330)

        create_circle(470,470,20,P)
        tk.Label(self,text = "INSIDE", fg = "Black",font = ("Arial",8)).place(x=454 ,y=430)

        create_circle(730,370,20,P)
        tk.Label(self,text = "DONE", fg = "Black",font = ("Arial",8)).place(x=734 ,y=330)

        create_circle(590,285,20,P)
        tk.Label(self,text = "DOCU", fg = "Black",font = ("Arial",8)).place(x=574,y=245)

        # Draw Flows
        P.create_line(90,370,150,370,arrow=tk.LAST)# home to contact
        P.create_line(190,370,250,370,arrow=tk.LAST)# contact to wait

        P.create_line(190,350,330,290,arrow=tk.LAST)# contact to free
        P.create_line(330,285,170,285)
        P.create_line(170,285,170,350,arrow=tk.LAST)# free to contact


        P.create_line(290,370,325,370,arrow=tk.LAST)# wait to start
        P.create_line(350,305,350,350,arrow=tk.LAST)# free to start
        P.create_line(370,370,447,370,arrow=tk.LAST)# start to busy
        P.create_line(490,370,565,370,arrow=tk.LAST)# busy to change
        P.create_line(590,370,710,370,arrow=tk.LAST)# change to done
        P.create_line(590,360,590,305,arrow=tk.LAST)# change to docu
        P.create_line(570,285,490,285,arrow=tk.LAST)# docu to end
        P.create_line(480,285,370,285,arrow=tk.LAST)# end to free
        P.create_line(350,380,350,470)
        P.create_line(350,470,447,470,arrow=tk.LAST)# start to inside
        P.create_line(490,470,590,470)
        P.create_line(590,470,590,390,arrow=tk.LAST)# inside to change

        P.create_line(730,350,730,210)
        P.create_line(730,210,490,210,arrow=tk.LAST)# done to pay

        P.create_line(470,210,70,210)
        P.create_line(70,210,70,350,arrow=tk.LAST)# pay to home

        P.create_line(470,190,470,150,arrow=tk.LAST)# pay to income

        # Draw Transitions
        self.T_Pay = tk.Button(self,activebackground='yellow',relief=SOLID,bd=1,height=2,width=5,command=lambda:self.handlePay())
        self.T_Pay.place(x=447,y=190)
        tk.Label(self,text="PAY",fg="black",font=("Arial",8)).place(x=435,y=170)

        self.T_Contact = tk.Button(self,activebackground='yellow',relief=SOLID,bd=1,height=2,width=5,command=lambda:self.handleContact())
        self.T_Contact.place(x=150,y=350)
        tk.Label(self,text="CONTACT",fg="black",font=("Arial",8)).place(x=145,y=390)
        self.T_Start = tk.Button(self,activebackground='yellow',relief=SOLID,bd=1,height=2,width=5,command=lambda:self.handleStart())
        self.T_Start.place(x=328,y=350)
        tk.Label(self,text="START",fg="black",font=("Arial",8)).place(x=307,y=330)
        self.T_Change = tk.Button(self,activebackground='yellow',relief=SOLID,bd=1,height=2,width=5,command=self.handleChange)
        self.T_Change.place(x = 568,y=350)
        tk.Label(self,text="CHANGE",font=("Arial",8)).place(x=593,y=330)
        self.T_End = tk.Button(self,activebackground='yellow',relief=SOLID,height=2,bd=1,width=5,command=self.handleEnd)
        self.T_End.place(x=447,y=265)
        tk.Label(self,text="END",font=("Arial",8)).place(x=455,y=245)

        # Add and draw ComboBox
        tk.Label(self,text="M0 = [",font=('Arial',10)).place(x=10,y=60)
        self.combo_home = Combobox(self,width=3)
        self.combo_home['value'] = (0,1,2,3,4,5,6,7,8,9,10)
        self.combo_home.current(0)
        self.combo_home.place(x=55,y=60)
        tk.Label(self,text = ".Home, ",font=('Arial',10)).place(x=96,y=60)

        self.combo_wait = Combobox(self,width=3,state='readonly')
        self.combo_wait['value'] = (0,1,2,3,4,5,6,7,8,9,10)
        self.combo_wait.place(x=145,y=60)
        self.combo_wait.current(0)
        tk.Label(self,text = ".Wait, ",font=('Arial',10)).place(x=188,y=60)

        self.combo_free = Combobox(self,width=3)
        self.combo_free['value'] = (0,1,2,3,4,5,6,7,8,9,10)
        self.combo_free.place(x=235,y=60)
        self.combo_free.current(0)
        tk.Label(self,text = ".Free, ",font=('Arial',10)).place(x=278,y=60)

        self.combo_busy = Combobox(self,width=3,state='readonly')
        self.combo_busy['value'] = (0,1,2,3)
        self.combo_busy.place(x=325,y=60)
        self.combo_busy.current(0)
        tk.Label(self,text = ".Busy, ",font=('Arial',10)).place(x=368,y=60)

        self.combo_inside = Combobox(self,width=3,state='readonly')
        self.combo_inside['value'] = (0,1,2,3)
        self.combo_inside.place(x=415,y=60)
        self.combo_inside.current(0)
        tk.Label(self,text = ".Inside, ",font=('Arial',10)).place(x=458,y=60)

        self.combo_done = Combobox(self,width=3)
        self.combo_done['value'] = (0,1,2,3,4,5,6,7,8,9,10)
        self.combo_done.place(x=505,y=60)
        self.combo_done.current(0)
        tk.Label(self,text = ".Done, ",font=('Arial',10)).place(x=548,y=60)

        self.combo_docu = Combobox(self,width=3,state='readonly')
        self.combo_docu['value'] = (0,1,2)
        self.combo_docu.place(x=595,y=60)
        self.combo_docu.current(0)
        tk.Label(self,text = ".Docu, ",font=('Arial',10)).place(x=638,y=60)

        self.combo_income = Combobox(self,width=3)
        self.combo_income['value'] = (0,1,2,3,4,5,6,7,8,9,10)
        self.combo_income.place(x=685,y=60)
        self.combo_income.current(0)
        tk.Label(self,text = ".Income ]",font=('Arial',10)).place(x=728,y=60)

        # Add some functions as set, back, next
        back_button = tk.Button(self,text="Back",width=10,command=lambda: appController.showPage(Item_4))
        back_button.place(x=50,y=20)
        home_button = tk.Button(self,text = "Home", width= 10,command=lambda: appController.showPage(HomePage))
        home_button.place(x=670,y=20)
        set_button = tk.Button(self, text = "Set", command=self.handleSet,width=10)
        set_button.place(x=140,y=108)

        # The number of token in every place
        self.income = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.income.place(x = 460, y = 120)

        self.home = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.home.place(x = 60, y = 360)

        self.wait = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.wait.place(x = 260, y = 360)
        tk.Label(self,text="k = 10",fg = "black",font=("Arial",10)).place(x=250,y=395)

        self.free = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.free.place(x =343, y = 275)


        self.busy = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.busy.place(x = 463, y = 360)
        tk.Label(self,text="k = 3",fg = "black",font=("Arial",10)).place(x=455,y=395)

        self.inside = tk.Label(self,text= 0,fg = "black",font=("Arial",10)) 
        self.inside.place(x = 463, y = 460)
        tk.Label(self,text="k = 3",fg = "black",font=("Arial",10)).place(x=455,y=495)

        self.done = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.done.place(x = 720, y = 360)

        self.docu = tk.Label(self,text= 0,fg = "black",font=("Arial",10))
        self.docu.place(x = 583, y = 275)
        tk.Label(self,text="k = 2",fg = "black",font=("Arial",10)).place(x=615,y=275)

        # Show curent marking
        self.marking = tk.Message(self,relief=SOLID,borderwidth=1,width=670,text=f"Curent marking: [ {self.places['home']} Home, {self.places['wait']} Wait, {self.places['free']} Free, {self.places['busy']} Busy, {self.places['inside']} Inside, {self.places['done']} Done, {self.places['docu']} Docu,{self.places['income']} Income ]",font=("Time new Roman",13))
        self.marking.place(x=80,y=540)

    def handleSet(self):
        self.places['income'] = int(self.combo_income.get())
        self.places['home'] = int(self.combo_home.get())
        self.places['wait'] = int(self.combo_wait.get())
        self.places['free'] = int(self.combo_free.get())
        self.places['busy'] = int(self.combo_busy.get())
        self.places['inside'] = int(self.combo_inside.get())
        self.places['done'] = int(self.combo_done.get())
        self.places['docu'] = int(self.combo_docu.get())
        if self.places['free'] <0 or self.places['done'] < 0 or self.places['income']<0 or self.places['home']<0:
            if self.places['free'] <0:
                self.places['free'] = 0
            if self.places['done'] <0:
                self.places['done'] = 0
            if self.places['home'] <0:
                self.places['home'] = 0
            if self.places['done'] <0:
                self.places['done'] = 0
            mbox.showerror("Error","Invalid input: The number of tokens must be non-negative")
        if self.places['busy']>self.places['inside']:
            mbox.showwarning('Warning','The number of patient(s) being treated is not equal to the number of specialist(s) treating for them.\nDo you want to continue?')
        self.showPetri()
        return
    def handlePay(self):
        if self.places['done'] >0:
            self.places['done']-=1
            self.places['income']+=1
            self.places['home']+=1
            self.showPetri()
        else:
            mbox.showerror("Error",'The transition Pay is not enable.')
    def handleContact(self):
        if self.places['home']>0 and self.places['free']>0 :
            if self.places['wait'] < 10:
                self.places['home']-=1
                self.places['free']-=1
                self.places['free']+=1
                self.places['wait']+=1
                self.showPetri()
            else :
                mbox.showwarning('Warning', 'The place Wait only can contain at most 10 tokens.')
        else:
            mbox.showerror('Error','The transition Contact is not enable.')
    def handleStart(self):
        if self.places['wait']>0 and self.places['free']>0:
            if self.places['busy']<3 and self.places['inside']<3:
                self.showPetri()
                self.places['wait']-=1
                self.places['free']-=1
                self.places['busy']+=1
                self.places['inside']+=1
                self.showPetri()
            else:
                mbox.showwarning("Warning","Both of places Busy and Inside only can contain at most 3 tokens.")
        else:
            mbox.showerror("Error","The transition Start is not enable.") 
    def handleChange(self):
        if self.places['busy']>0 and self.places['inside']>0:
            if self.places['docu']<2:
                self.showPetri()
                self.places['busy']-=1
                self.places['inside']-=1
                self.places['done']+=1
                self.places['docu']+=1
                self.showPetri()
            else:
                mbox.showwarning("Warning","The place Docu only can contain at most 2 tokens.")
        else:
            mbox.showerror("Error","The transition Change is not enable.")
    def handleEnd(self):
        if self.places['docu']>0:
            self.showPetri()
            self.places['docu']-=1
            self.places['free']+=1
            self.showPetri()
        else:
            mbox.showerror("Error","The transition End is not enable.")
    def showPetri(self):
        if(self.places['done']>0 ):
            self.T_Pay.configure(background='green')
        else:
            self.T_Pay.configure(background='red')

        if(self.places['home']>0 and self.places['free']>0 ):
            self.T_Contact.configure(background='green')
        else:
            self.T_Contact.configure(background='red')

        if(self.places['wait']>0 and self.places['free']>0):
            self.T_Start.configure(background='green')
        else:
            self.T_Start.configure(background='red')
        if(self.places['busy']>0 and self.places['inside']>0):
            self.T_Change.configure(background='green')
        else:
            self.T_Change.configure(background='red')
        if(self.places['docu']>0 ):
            self.T_End.configure(background='green')
        else:
            self.T_End.configure(background='red')
        self.marking.configure(text=f"Current marking: [ {self.places['home']} Home, {self.places['wait']} Wait, {self.places['free']} Free, {self.places['busy']} Busy, {self.places['inside']} Inside, {self.places['done']} Done, {self.places['docu']} Docu, {self.places['income']} Income]")
        self.free.configure(text=self.places['free'])
        self.wait.configure(text = self.places['wait'])
        self.busy.configure(text=self.places['busy'])
        self.inside.configure(text = self.places['inside'])
        self.done.configure(text=self.places['done'])
        self.docu.configure(text = self.places['docu'])
        self.income.configure(text=self.places['income'])
        self.home.configure(text = self.places['home'])
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("ASSIGNMENT PETRI NET")
        self.geometry("800x600+350+100")
        self.resizable(width = False,height = False)
        container = tk.Frame(self)
        container.configure(bg ="#bfd6f6")
        container.pack(side="top",fill = "both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}
        for F in (HomePage,Item_1,Item_2,Item_3,Item_4,Item_enhanced):
            frame = F(container,self)
            frame.grid(row = 0,column=0,sticky="nsew")
            self.frames[F] = frame
        self.frames[HomePage].tkraise()
    
    def showPage(self,FrameClass):
        self.frames[FrameClass].tkraise()      

if __name__ == "__main__":
    app = App()
    app.mainloop()