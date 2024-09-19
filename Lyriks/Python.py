import time

lyrics_with_custom_delays = [
    (0, "Who would  have ever knew", 4.1),
    (4, "That we would ever be more than friends?", 4.5),
    (9, "We're real worldwide, breaking all the rules", 2),
    (14, "She like a song played again and again", 2),
    (20, "(That girl) like something off a poster", 1),
    (24, "(That girl) is a dime they say", 2),
]

def print_lyrics():
    start_time = time.time() 
    for timestamp, line, custom_delay in lyrics_with_custom_delays:
        current_time = time.time() - start_time  
        if current_time < timestamp:
            time.sleep(timestamp - current_time)  

        for word in line.split(): 
            for char in word:  
                print(char, end='', flush=True) 
                time.sleep(0.09)  

            print(' ', end='', flush=True)  

        print()  
        time.sleep(custom_delay)  


print_lyrics()