def add_One (arr,size):
    #print (arr)
    if (size == -1):
        arr.append(0)
        arr[0] = 1
        return 
      
    if(arr[size] == 9):
        arr[size] = 0
        add_One(arr,size-1)
    else:
        arr[size] += 1
        return


ev = [0]
add_One(ev,len(ev)-1)
print (ev)