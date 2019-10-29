
def num_ways(msg):
    if (len(msg) == 0):
        return 1
    
    
    if (len(msg) != 1):
        str2 = int(msg[0:2])
        msg2 = msg[2:len(msg)]
    msg1 = msg[1:len(msg)]
    
     
    if (str2 < 27):
        return 1 + num_ways(msg1) + num_ways(msg2)
    else:
        return 1 + num_ways(msg1) 



ev = "123"
i = num_ways(ev)
print (i)