from tkinter import *
from tkinter.ttk import *
import tkinter
import tkinter.messagebox as mbox
import time
import _thread

def main():
    # Create a window to execute the program.
    window = tkinter.Tk()
    window.configure(bg="red")
    window.title("Item 3: Superimposed network")
    window.geometry("800x600+350+100")
    window.resizable(False,False)

    # Draw Places
    def create_circle(x, y, r, canvasName): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1)
    P = Canvas(window,height= 600,width=800,)

    create_circle(120,220,20,P)
    tkinter.Label(window,text = "WAIT", fg = "Black",font = ("Arial",8)).place(x=104 ,y=180)

    create_circle(250,135,20,P)
    tkinter.Label(window,text = "FREE", fg = "Black",font = ("Arial",8)).place(x=234 ,y=95)

    create_circle(370,220,20,P)
    tkinter.Label(window,text = "BUSY", fg = "Black",font = ("Arial",8)).place(x=354 ,y=180)

    create_circle(370,320,20,P)
    tkinter.Label(window,text = "INSIDE", fg = "Black",font = ("Arial",8)).place(x=354 ,y=280)

    create_circle(490,135,20,P)
    tkinter.Label(window,text = "DOCU", fg = "Black",font = ("Arial",8)).place(x=474,y=95)

    create_circle(630,220,20,P)
    tkinter.Label(window,text = "DONE", fg = "Black",font = ("Arial",8)).place(x=614 ,y=180)

    # Draw Flows
    P.create_line(140,220,225,220,arrow=tkinter.LAST)# wait to start
    P.create_line(250,155,250,200,arrow=tkinter.LAST)# free to start
    P.create_line(270,220,347,220,arrow=tkinter.LAST)# start to busy
    P.create_line(390,220,465,220,arrow=tkinter.LAST)# busy to change
    P.create_line(490,220,610,220,arrow=tkinter.LAST)# change to done
    P.create_line(490,210,490,155,arrow=tkinter.LAST)# change to docu
    P.create_line(470,135,390,135,arrow=tkinter.LAST)# docu to end
    P.create_line(380,135,270,135,arrow=tkinter.LAST)# end to free
    P.create_line(250,230,250,320)
    P.create_line(250,320,347,320,arrow=tkinter.LAST)# start to inside
    P.create_line(390,320,490,320)
    P.create_line(490,320,490,240,arrow=tkinter.LAST)# inside to change
    P.pack()

    # Add ComboBox
    lbl = tkinter.Label(window,text="Enter a initial marking: M0 = [",font=('Arial',10)).place(x=5,y=10)

    combo_wait = Combobox(window,width=5,state='readonly')
    combo_wait['value'] = (0,1,2,3,4,5,6,7,8,9,10)
    combo_wait.current(0)
    combo_wait.place(x=185,y=10)
    tkinter.Label(window,text = ".Wait, ",font=('Arial',10)).place(x=238,y=10)

    combo_free = Combobox(window,width=5,state='readonly')
    combo_free['value'] = (0,1,2,3,4,5)
    combo_free.place(x=285,y=10)
    combo_free.current(0)
    tkinter.Label(window,text = ".Free,",font=('Arial',10)).place(x=338,y=10)

    combo_busy = Combobox(window,width=5,state='readonly')
    combo_busy['value'] = (0,1,2,3)
    combo_busy.place(x=385,y=10)
    combo_busy.current(0)
    tkinter.Label(window,text = ".Busy,",font=('Arial',10)).place(x=438,y=10)

    combo_inside = Combobox(window,width=5,state='readonly')
    combo_inside['value'] = (0,1,2,3)
    combo_inside.place(x=485,y=10)
    combo_inside.current(0)
    tkinter.Label(window,text = ".Inside, ",font=('Arial',10)).place(x=538,y=10)

    combo_done = Combobox(window,width=5)
    combo_done['value'] = (0,1,2,3,4,5,6,7,8,9,10)
    combo_done.place(x=585,y=10)
    combo_done.current(0)
    tkinter.Label(window,text = ".Done,",font=('Arial',10)).place(x=638,y=10)

    combo_docu = Combobox(window,width=5,state='readonly')
    combo_docu['value'] = (0,1,2)
    combo_docu.place(x=685,y=10)
    combo_docu.current(0)
    tkinter.Label(window,text = ".Docu]",font=('Arial',10)).place(x=738,y=10)

    # The number of token in every place
    w0 = tkinter.Label(window,text= 0,fg = "black",font=("Arial",10))   # w0: WAIT
    w0.place(x = 110, y = 210)
    tkinter.Label(window,text="k = 10",fg = "black",font=("Arial",10)).place(x=100,y=245)

    w1 = tkinter.Label(window,text= 1,fg = "black",font=("Arial",10))   # w1: FREE
    w1.place(x = 243, y = 125)
    tkinter.Label(window,text="k = 5",fg = "black",font=("Arial",10)).place(x=190,y=125)

    w2 = tkinter.Label(window,text= 0,fg = "black",font=("Arial",10))   # w2: BUSY
    w2.place(x = 363, y = 210)
    tkinter.Label(window,text="k = 3",fg = "black",font=("Arial",10)).place(x=355,y=245)

    w3 = tkinter.Label(window,text= 0,fg = "black",font=("Arial",10))   # w3: INSIDE
    w3.place(x = 363, y = 310)
    tkinter.Label(window,text="k = 3",fg = "black",font=("Arial",10)).place(x=355,y=345)

    w4 = tkinter.Label(window,text= 0,fg = "black",font=("Arial",10))   # w4: DONE
    w4.place(x = 620, y = 210)

    w5 = tkinter.Label(window,text= 0,fg = "black",font=("Arial",10))   # w5: DOCU
    w5.place(x = 483, y = 125)
    tkinter.Label(window,text="k = 2",fg = "black",font=("Arial",10)).place(x=515,y=125)

    # Create List of number of places and flag check
    places = [0,0,0,0,0,0]              # List of places: wait, free, busy, inside, done, docu
    flag_check = tkinter.BooleanVar()
    flag_check.set(False)
    # Add checkbox
    check_button = Checkbutton(window,text="Auto firing",onvalue=1,offvalue=0,variable=flag_check).place(x=280,y=48)

    

    ####################################################
    ################## Helping function ################
    ####################################################
    def show(x):
        if(x[0]!=0 and x[1]!=0):
            T_Start.configure(background='green')
        else:
            T_Start.configure(background='red')
        if(x[2]!=0 and x[3]!=0):
            T_Change.configure(background='green')
        else:
            T_Change.configure(background='red')
        if(x[5]!=0 ):
            T_End.configure(background='green')
        else:
            T_End.configure(background='red')
        marking.configure(text="M = { "+f"{x[0]} Wait, {x[1]} Free, {x[2]} Busy, {x[3]} Inside, {x[4]} Done, {x[5]} Docu"+"}")
        w1.configure(text=x[1])
        w0.configure(text = x[0])
        w2.configure(text=x[2])
        w3.configure(text = x[3])
        w4.configure(text=x[4])
        w5.configure(text = x[5])

    # Handle Start (click to fire)
    def handle_T_Start(x):
        if flag_check.get()==False:
            if x[0]>0 and x[1]>0:
                show(x)
                x[0]-=1
                x[1]-=1
                x[2]+=1
                x[3]+=1
                show(x)
            elif x[2]>3 and x[3]>3:
                mbox.showwarning("Warning","bala..............")
            else:
                mbox.showerror("Error","The transition Start is not enable.") 
    def handle_T_Start_1():
        handle_T_Start(places)
        return
    # Add transition Start
    T_Start = tkinter.Button(window,activebackground='yellow',relief=SOLID,bd=1,height=2,width=5,command=handle_T_Start_1)
    T_Start.place(x=228,y=200)
    tkinter.Label(window,text="START",fg="black",font=("Arial",8)).place(x=207,y=180)

    # Handle Change (click to fire)
    def handle_T_Change(x):
        if flag_check.get()==False:
            if x[2]!=0 and x[3]!=0:
                show(x)
                x[2]-=1
                x[3]-=1
                x[4]+=1
                x[5]+=1
                show(x)
            elif x[5]>2:
                mbox.showwarning("Warning","bala..............")
            else:
                mbox.showerror("Error","The transition Change is not enable.")
    def handle_T_Change_1():
        handle_T_Change(places)
        return
    # Add transition Change
    T_Change = tkinter.Button(window,activebackground='yellow',relief=SOLID,bd=1,height=2,width=5,command=handle_T_Change_1)
    T_Change.place(x = 468,y=200)
    tkinter.Label(window,text="CHANGE",font=("Arial",8)).place(x=493,y=180)

    # Handle End (click to fire)
    def handle_T_End(x):
        if flag_check.get()==False:
            if x[5]!=0:
                show(x)
                x[5]-=1
                x[1]+=1
                show(x)
            else:
                mbox.showerror("Error","The transition End is not enable.")
    def handle_T_End_1():
        handle_T_End(places)
        return
    # Add transition End
    T_End = tkinter.Button(window,activebackground='yellow',relief=SOLID,height=2,bd=1,width=5,command=handle_T_End_1)
    T_End.place(x=347,y=115)
    tkinter.Label(window,text="END",font=("Arial",8)).place(x=355,y=95)

    # Handle Set ( Set a initial marking)
    def handleSet(x):        
        x[0] = int(combo_wait.get())
        x[1] = int(combo_free.get())
        x[2] = int(combo_busy.get())
        x[3] = int(combo_inside.get())
        x[4] = int(combo_done.get())
        x[5] = int(combo_docu.get())
        if x[2]!=x[3]:
            mbox.showwarning('Warning','The number of patient(s) being treated is not equal to the number of specialist(s) treating for them.\nDo you want to continue?')
        show(x)
        return
    def handleSet_1():
        flag_check.set(False)
        handleSet(places)
        return  
    # Add button
    set_button = Button(window, text = "Set", command=handleSet_1).place(x=180,y=45)

    # Handle Run (Running)
    def handleRun(x):      
        if(flag_check.get()==True):
            if x[0]<0 or x[1]<0 or x[2]<0 or x[3]<0 or x[4]<0 or x[5]<0:
                return
            if(x[0]<=0 or x[1] <=0) and (x[1]<=0 or x[2]<=0) and x[5]<=0:
                return
            time.sleep(1)
            fixed_free = x[1]+x[2]+x[5]
            while x[0]>0 or x[1]!=fixed_free :                      # while wait>=0 or free!=fixed_free
                if flag_check.get() == False:
                    return
                if x[1]>0 and x[0]>0:
                    if x[2]<3 and x[3]<3:
                        if flag_check.get()==False:
                            return
                        T_Start.configure(bg="yellow")
                        time.sleep(0.5)
                        x[0]-=1
                        x[1]-=1
                        x[2]+=1
                        x[3]+=1
                        show(x)
                        time.sleep(1)
                        continue
                if x[2]>0 and x[3]>0:
                    if x[5]<2:
                        if flag_check.get() == False:
                            return
                        T_Change.configure(bg="yellow")
                        time.sleep(0.5)
                        x[2]-=1
                        x[3]-=1
                        x[4]+=1
                        x[5]+=1
                        show(x)
                        time.sleep(1)
                        continue
                if x[5]>0:
                    if flag_check.get()==False:
                        return
                    T_End.configure(bg="yellow")
                    time.sleep(0.5)
                    x[1]+=1
                    x[5]-=1
                    show(x)
                    time.sleep(1)
                if (x[0]==0 or x[1] ==0) and (x[2]==0 or x[3]==0) and x[5]==0:
                    return
            else:
                return
    def handleRun_1():
        handleRun(places)
        return
    # Add run buttob
    run_button = Button(window,text = "Run",command=lambda:_thread.start_new_thread(handleRun_1,())).place(x=380,y=45)

    # Show curent marking
    marking = tkinter.Message(window,relief=SOLID,borderwidth=1,width=500,text="Curent marking: [ "+f"{places[0]} Wait, {places[1]} Free, {places[2]} Busy, {places[3]} Inside, {places[4]} Done, {places[5]} Docu"+"]",font=("Time new Roman",13))
    marking.place(x=150,y=400)

    window.mainloop()
if __name__ == "__main__":
    main()