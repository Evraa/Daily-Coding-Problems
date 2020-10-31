def slowestKey(self, releaseTimes, keysPressed) -> str:
    freq_map = dict()
    last_press = 0
    max_press = 0
    chars_max = None
    for i, press in enumerate(releaseTimes):
        press_time = press - last_press
        last_press = press
        
        if keysPressed[i] in freq_map.keys(): 
            freq_map[keysPressed[i]] += press_time
        else:
            freq_map[keysPressed[i]] = press_time
            
        press_time = freq_map[keysPressed[i]]
        if press_time > max_press:
            max_press = press_time
            if keysPressed[i] != chars_max:
                chars_max = (keysPressed[i])
                
        elif press_time == max_press:
            if keysPressed[i] > chars_max:
                chars_max = (keysPressed[i])
        

    return chars_max