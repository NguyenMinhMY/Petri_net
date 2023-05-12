def print_TS(wait,free,busy,inside,done,docu):
    if (free > 0 and wait>0) or (busy>0 and inside>0) or docu>0:
        if (wait>0 and free >0) and (busy<3 and inside<3):
            count[0]+=1
            print_TS(wait-1,free-1,busy+1,inside+1,done,docu)
        if (inside>0 and busy>0) and docu <2:
            count[0]+=1
            print_TS(wait,free,busy-1,inside-1,done+1,docu+1)
        if docu>0 :           
            count[0]+=1
            print_TS(wait,free+1,busy,inside,done,docu-1)
    else:
        return

count = [1]
fixed_wait = 4
fixed_free = 1
print_TS(3,1,0,0,1,0)
print(count)