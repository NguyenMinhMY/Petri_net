from tkinter import *
from tkinter.ttk import *
import tkinter
import tkinter.messagebox as mbox
import time
import _thread

def main():
    # Create a window to execute the program.
    window = tkinter.Tk()
    window.title("Item 2: Patient network")
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

    create_circle(120,200,20,P)
    tkinter.Label(window,text = "WAIT", fg = "Black",font = ("Arial",8)).place(x=104 ,y=160)

    create_circle(370,200,20,P)
    tkinter.Label(window,text = "INSIDE", fg = "Black",font = ("Arial",8)).place(x=354 ,y=160)

    create_circle(630,200,20,P)
    tkinter.Label(window,text = "DONE", fg = "Black",font = ("Arial",8)).place(x=614 ,y=160)

    # Draw Flows
    P.create_line(140,200,225,200,arrow=tkinter.LAST)# wait to start
    P.create_line(270,200,347,200,arrow=tkinter.LAST)# start to inside
    P.create_line(390,200,465,200,arrow=tkinter.LAST)# inside to change
    P.create_line(490,200,610,200,arrow=tkinter.LAST)# change to done
    P.pack()

    # Add ComboBox
    lbl = tkinter.Label(window,text="Enter a initial marking: M0 = [",font=('Arial',10)).place(x=5,y=10)

    combo_wait = Combobox(window,width=5,state='readonly')
    combo_wait['value'] = (0,1,2,3,4,5,6,7,8,9,10)
    combo_wait.place(x=185,y=10)
    combo_wait.current(0)
    tkinter.Label(window,text = ".Wait, ",font=('Arial',10)).place(x=238,y=10)

    combo_inside = Combobox(window,width=5,state='readonly')
    combo_inside['value'] = (0,1,2,3)
    combo_inside.place(x=285,y=10)
    combo_inside.current(0)
    tkinter.Label(window,text = ".Inside, ",font=('Arial',10)).place(x=338,y=10)

    combo_done = Combobox(window,width=5)
    combo_done['value'] = (0,1,2,3,4,5,6,7,8,9,10)
    combo_done.place(x=385,y=10)
    combo_done.current(0)
    tkinter.Label(window,text = ".Done ]",font=('Arial',10)).place(x=438,y=10)
    
    # The number of token in every place
    w0 = tkinter.Label(window,text= 0,fg = "black",font=("Arial",10))   # w0: WAIT
    w0.place(x = 110, y = 190)
    tkinter.Label(window,text="k = 10",fg = "black",font=("Arial",10)).place(x=100,y=225)

    w1 = tkinter.Label(window,text= 0,fg = "black",font=("Arial",10))   # w1: INSIDE
    w1.place(x = 363, y = 190)
    tkinter.Label(window,text="k = 3",fg = "black",font=("Arial",10)).place(x=355,y=225)

    w2 = tkinter.Label(window,text= 0,fg = "black",font=("Arial",10))   # w2: DONE
    w2.place(x = 620, y = 190)

    # Create List of number of places and flag check
    places = [0,0,0]
    flag_check = tkinter.BooleanVar()
    flag_check.set(False)
    check_button = Checkbutton(window,text="Auto firing",onvalue=1,offvalue=0,variable=flag_check).place(x=580,y=13)

    # Handle Start (click to fire)
    def handle_T_Start(x):
        if flag_check.get()==False:
            if x[0]>0:
                if x[1] <3:
                    show(x)
                    x[0]-=1
                    x[1]+=1
                    show(x)
                else:
                    mbox.showwarning("Waring","Abala Trap")
            else:
                mbox.showerror("Error","The transition Start is not enable.") 
    def handle_T_Start_1():
        handle_T_Start(places)
        return
    # Add transition Start
    T_Start = tkinter.Button(window,activebackground='yellow',relief=SOLID,bd=1,height=2,width=5,command=handle_T_Start_1)
    T_Start.place(x=228,y=180)
    tkinter.Label(window,text="START",fg="black",font=("Arial",8)).place(x=228,y=160)

    # Handle Change (click to fire)
    def handle_T_Change(x):
        if flag_check.get()==False:
            if x[1]>0 :
                show(x)
                x[1]-=1
                x[2]+=1
                show(x)
            else:
                mbox.showerror("Error","The transition Change is not enable.")
    def handle_T_Change_1():
        handle_T_Change(places)
        return
    # Add transition Change
    T_Change = tkinter.Button(window,activebackground='yellow',relief=SOLID,bd=1,height=2,width=5,command=handle_T_Change_1)
    T_Change.place(x = 468,y=180)
    tkinter.Label(window,text="CHANGE",font=("Arial",8)).place(x=468,y=160)

    ####################################################################################
    ######################## Helping function while run ################################
    ####################################################################################
    def show(x):
        if(x[0]!=0):
            T_Start.configure(background='green')
        else:
            T_Start.configure(background='red')
        if(x[1]!=0):
            T_Change.configure(background='green')
        else:
            T_Change.configure(background='red')
        marking.configure(text="Current marking: [ "+f"{x[0]} Wait, {x[1]} Inside, {x[2]} Done"+"]")
        w0.configure(text = x[0])
        w1.configure(text=x[1])
        w2.configure(text=x[2])

    # Handle Set (Set a initial marking)
    def handleSet(x):
        x[0] = int(combo_wait.get())
        x[1] = int(combo_inside.get())
        x[2] = int(combo_done.get())
        show(x)
        return
    def handleSet_1():
        flag_check.set(False)
        handleSet(places)
        return  
    # Add set button
    set_button = Button(window, text = "Set", command=handleSet_1,width=5)
    set_button.place(x=530,y=10)

    # Handle Run (Running)
    def handleRun(x):      
        time.sleep(1)
        if(flag_check.get()==True):
            while x[0]>0 or x[1]>0:
                if flag_check.get() == False:
                    return
                if(x[1]<3) and x[0]>0:
                    if flag_check.get() == False:
                        return
                    T_Start.configure(bg="yellow")
                    time.sleep(0.5)
                    x[1]+=1
                    x[0]-=1
                    show(x)
                    time.sleep(1)  
                    continue           
                if x[1] > 0:
                    if flag_check.get() == False:
                        return
                    T_Change.configure(bg="yellow")
                    time.sleep(0.5)
                    x[2]+=1
                    x[1]-=1
                    show(x)
                    time.sleep(1)
        else:
            return
    def handleRun_1():
        handleRun(places)
        return

    # Add run button ()
    run_button = Button(window,text = "Run",width=5,command=lambda:_thread.start_new_thread(handleRun_1,())).place(x=670,y=10)

    # Show current marking
    marking = tkinter.Message(window,relief=SOLID,borderwidth=1,width=500,text="Current marking: [ "+f"{places[0]} Wait, {places[1]} Inside, {places[2]} Done"+"]",font=("Time new Roman",13))
    marking.place(x=230,y=270)

    window.mainloop()
if __name__ == "__main__":
    main()