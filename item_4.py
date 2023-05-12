from tkinter import *
from tkinter.ttk import *
import tkinter
import tkinter.messagebox as mbox
from tkinter import scrolledtext

def main():
    window = Tk()
    window.title("Item 4: Reachable marking")
    window.geometry("800x600+350+100")
    window.resizable(False,False)

    # Add scrolled text
    st = scrolledtext.ScrolledText(window, width = 115, height = 27, font = ("Times New Roman",10))
    st.place(x=50,y=95)

    # Add textbox
    count_text = tkinter.Text(window, width = 10,height=1, font = ("Times New Roman",10))
    count_text.place(x=660,y=49)

    # add combobox to set initial marking
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

    combo_done = Combobox(window,width=5,state='readonly')
    combo_done['value'] = (0,1,2,3,4,5,6,7,8,9,10)
    combo_done.place(x=585,y=10)
    combo_done.current(0)
    tkinter.Label(window,text = ".Done,",font=('Arial',10)).place(x=638,y=10)

    combo_docu = Combobox(window,width=5,state='readonly')
    combo_docu['value'] = (0,1,2)
    combo_docu.place(x=685,y=10)
    combo_docu.current(0)
    tkinter.Label(window,text = ".Docu]",font=('Arial',10)).place(x=738,y=10)

    ########################################################
    places = [0,0,0,0,0,0] # wait,free,busy,inside,done,docu
    str = "Firing sequence:[]"
    count = [1]
    flag = [FALSE,FALSE] # flag[0]: flag_set, flag[1]: flag_find
    # Function

    def show_marking(wait,free,busy,inside,done,docu):
        st.insert(INSERT,f"Marking: [{wait}.Wait,{free}.Free,{busy}.Busy,{inside}.Inside,{done}.Done,{docu}.Docu]\n\n")
    def print_TS(wait,free,busy,inside,done,docu,str,fixed_wait,fixed_free,count):
        st.insert(INSERT,str+'\n')
        show_marking(wait,free,busy,inside,done,docu)
        if fixed_wait!=done or free !=fixed_free:
            if (wait>0 and free >0) and (busy<3 and inside<3):
                str_temp = ",Start]"
                str = str[0:-1]
                str+=str_temp
                index = str.find('[')+1
                if str[index] == ',':
                    str = str[0:index] + str[index+1:]
                count[0]+=1
                print_TS(wait-1,free-1,busy+1,inside+1,done,docu,str,fixed_wait,fixed_free,count)
            if (inside>0 and busy>0) and docu <2:
                str_temp = ",Change]"
                str = str[0:-1]
                str+=str_temp
                count[0]+=1
                print_TS(wait,free,busy-1,inside-1,done+1,docu+1,str,fixed_wait,fixed_free,count)
            if docu>0 :           
                str_temp = ",End]"
                str = str[0:-1]
                str+=str_temp
                count[0]+=1
                print_TS(wait,free+1,busy,inside,done,docu-1,str,fixed_wait,fixed_free,count)
        else:
            return
    def handle_Set(places):
        places[0] = int(combo_wait.get())
        places[1] = int(combo_free.get())
        places[2] = int(combo_busy.get())
        places[3] = int(combo_inside.get())
        places[4] = int(combo_done.get())
        places[5] = int(combo_docu.get())
    def handle_Set_1():
        flag[0] = TRUE
        flag[1] = FALSE
        count[0] = 1
        handle_Set(places)

    def handle_find(places):
        fixed_wait = places[0]+places[1]
        fixed_free = places[1]
        st.delete('1.0',END)
        print_TS(places[0],places[1],places[2],places[3],places[4],places[5],str,fixed_wait,fixed_free,count)
    def handle_find_1():
        if flag[0] == TRUE:
            flag[1] = TRUE
            count[0] = 1
            handle_find(places)
        else :
            mbox.showwarning('Waring','Please press button "Set" to find!')

    def handle_count():
        if flag[1]==TRUE:
            count_text.delete("1.0","end")
            count_text.insert(END,f"{count[0]}")
        else:
            mbox.showwarning('Warning','Please press button "Find" to count!')
    # Add button
    Set_button = Button(window,text="Set",command=handle_Set_1)
    Set_button.place(x=280,y=45)

    Find_button = Button(window,text="Find",command=handle_find_1)
    Find_button.place(x=380,y=45)

    Count_button = Button(window,text="Count",command=handle_count)
    Count_button.place(x=580,y=45)


    window.mainloop()

if __name__ == "__main__":
    main()