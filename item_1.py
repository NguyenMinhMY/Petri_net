from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.messagebox as mbox
import time
import _thread
from typing import Container

if __name__ == "__main__":
    # Create a window to execute the program.
    window = tk.Tk()
    window.title("Item 1: Specialist network")
    window.geometry("800x600+350+100")
    window.resizable(False,False)

    container= tk.Frame()
    container.pack()
    # Draw Places
    def create_circle(x, y, r, canvasName): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1)

    P = Canvas(container,height= 600,width=800)

    create_circle(250,115,20,P)
    tk.Label(container,text = "FREE", fg = "Black",font = ("Arial",8)).place(x=234 ,y=75)

    create_circle(370,200,20,P)
    tk.Label(container,text = "BUSY", fg = "Black",font = ("Arial",8)).place(x=354 ,y=160)

    create_circle(490,115,20,P)
    tk.Label(container,text = "DOCU", fg = "Black",font = ("Arial",8)).place(x=474,y=75)

    # Draw Flows
    P.create_line(250,135,250,180,arrow=tk.LAST)# free to start
    P.create_line(270,200,347,200,arrow=tk.LAST)# start to busy
    P.create_line(390,200,465,200,arrow=tk.LAST)# busy to change
    P.create_line(490,190,490,135,arrow=tk.LAST)# change to docu
    P.create_line(470,115,390,115,arrow=tk.LAST)# docu to end
    P.create_line(380,115,270,115,arrow=tk.LAST)# end to free
    P.pack()

    # Add and draw ComboBox
    lbl = tk.Label(container,text="Enter a initial marking: M0 = [",font=('Arial',10)).place(x=5,y=10)
    combo_free = Combobox(container,width=5,state='readonly')
    combo_free['value'] = (0,1,2,3,4,5)
    combo_free.place(x=185,y=10)
    combo_free.current(0)
    tk.Label(container,text = ".Free, ",font=('Arial',10)).place(x=238,y=10)

    combo_busy = Combobox(container,width=5,state='readonly')
    combo_busy['value'] = (0,1,2,3)
    combo_busy.place(x=285,y=10)
    combo_busy.current(0)
    tk.Label(container,text = ".Busy, ",font=('Arial',10)).place(x=338,y=10)

    combo_docu = Combobox(container,width=5,state='readonly')
    combo_docu['value'] = (0,1,2)
    combo_docu.place(x=385,y=10)
    combo_docu.current(0)
    tk.Label(container,text = ".Docu ]",font=('Arial',10)).place(x=438,y=10)

    # The number of token in every place
    w0 = tk.Label(container,text= 0,fg = "black",font=("Arial",10))   # w0: FREE
    w0.place(x =243, y = 105)
    tk.Label(container,text="k = 5",fg = "black",font=("Arial",10)).place(x=190,y=105)

    w1 = tk.Label(container,text= 0,fg = "black",font=("Arial",10))   # w1: BUSY
    w1.place(x = 363, y = 190)
    tk.Label(container,text="k = 3",fg = "black",font=("Arial",10)).place(x=355,y=225)

    w2 = tk.Label(container,text= 0,fg = "black",font=("Arial",10))   # w2: DOCU
    w2.place(x = 483, y = 105)
    tk.Label(container,text="k = 2",fg = "black",font=("Arial",10)).place(x=515,y=105)

    # Create List of number of places and flag check
    places = [0,0,0]
    flag_check = tk.BooleanVar()
    flag_check.set(False)
    check_button = Checkbutton(container,text="Auto firing",onvalue=1,offvalue=0,variable=flag_check).place(x=580,y=13)

    # Handle Start (click to fire)
    def handle_T_Start(x):
        if flag_check.get()==False:
            if x[0]!=0 :
                if x[1] < 3:
                    show(x)
                    x[0]-=1
                    x[1]+=1
                    show(x)
                else:
                    mbox.showwarning("Warning", "Hiện cái gì đây")
            else:
                mbox.showerror("Error","The transition Start is not enable.") 
    def handle_T_Start_1():
        handle_T_Start(places)
        return
    # Add transition start
    T_Start = tk.Button(container,activebackground='yellow',relief=SOLID,bd=1,height=2,width=5,command=handle_T_Start_1)
    T_Start.place(x=228,y=180)
    tk.Label(container,text="START",fg="black",font=("Arial",8)).place(x=207,y=160)

    # Handle Change (click to fire)
    def handle_T_Change(x):
        if flag_check.get()==False:
            if x[1]!=0:
                if x[2]<2:
                    show(x)
                    x[2]+=1
                    x[1]-=1
                    show(x)
                else:
                    mbox.showwarning("Warning"," Abala trap.")
            else:
                mbox.showerror("Error","The transition Change is not enable.")
    def handle_T_Change_1():
        handle_T_Change(places)
        return
    # Add transition change
    T_Change = tk.Button(container,activebackground='yellow',relief=SOLID,bd=1,height=2,width=5,command=handle_T_Change_1)
    T_Change.place(x = 468,y=180)
    tk.Label(container,text="CHANGE",font=("Arial",8)).place(x=493,y=160)

    # Handle End  (click to fire)
    def handle_T_End(x):
        if flag_check.get()==False:
            if x[2]!=0:
                show(x)
                x[2]-=1
                x[0]+=1
                show(x)
            else:
                mbox.showerror("Error","The transition End is not enable.")
    def handle_T_End_1():
        handle_T_End(places)
        return
    # Add and draw transition End
    T_End = tk.Button(container,activebackground='yellow',relief=SOLID,height=2,bd=1,width=5,command=handle_T_End_1)
    T_End.place(x=347,y=95)
    tk.Label(container,text="END",font=("Arial",8)).place(x=355,y=75)

    ####################################################################################
    ######################## Helping function while run ################################
    ####################################################################################

    # Function to show petri net again.
    def show(x):
        if(x[0]!=0):
            T_Start.configure(background='green')
        else:
            T_Start.configure(background='red')
        if(x[1]!=0):
            T_Change.configure(background='green')
        else:
            T_Change.configure(background='red')
        if(x[2]!=0 ):
            T_End.configure(background='green')
        else:
            T_End.configure(background='red')
        marking.configure(text=f"Current marking: [ {x[0]} Free, {x[1]} Busy, {x[2]} Docu ]")
        w0.configure(text=x[0])
        w1.configure(text=x[1])
        w2.configure(text = x[2])

    # Handle Set (Set a initial marking)
    def handleSet(x):
        x[0] = int(combo_free.get())
        x[1] = int(combo_busy.get())
        x[2] = int(combo_docu.get())
        show(x)
        return

    def handleSet_1():
        flag_check.set(False)
        handleSet(places)
        return  
    # Add set button
    set_button = Button(container, text = "Set", command=handleSet_1,width=5)
    set_button.place(x=530,y=10)

    # Handle Run (Running)
    def handleRun(x):      
        if(flag_check.get()==1):
            time.sleep(1)
            while x[0]!=0 or x[1]!=0 or x[2]!=0:
                if x[0] > 0 and x[1]<3:
                    if(flag_check.get()==0):
                        return
                    T_Start.configure(bg="yellow")
                    time.sleep(0.5)
                    x[1]+=1
                    x[0]-=1
                    show(x)
                    time.sleep(1)
                    continue             
                if x[1]>0 and x[2]<2 :
                    if(flag_check.get()==0):
                        return
                    T_Change.configure(bg="yellow")
                    time.sleep(0.5)
                    x[1]-=1
                    x[2]+=1
                    show(x)
                    time.sleep(1)
                    continue
                if x[2]>0:
                    if(flag_check.get()==0):
                        return
                    T_End.configure(bg="yellow")
                    time.sleep(0.5)
                    x[2]-=1
                    x[0]+=1
                    show(x)
                    time.sleep(1)
        else:
            return
    def handleRun_1():
        handleRun(places)
        return
    # Add run button
    run_button = Button(container,text = "Run",width=5,command=lambda:_thread.start_new_thread(handleRun_1,())).place(x=670,y=10)

    # Show current marking
    marking = tk.Message(container,relief=SOLID,borderwidth=1 ,text=f"Current marking: [ {places[0]} Free, {places[1]} Busy, {places[2]} Docu]",font=("Time new Roman",13),width=400)
    marking.place(x=210,y=270)

    window.mainloop()