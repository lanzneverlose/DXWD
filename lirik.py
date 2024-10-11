from time import sleep
import time
import sys

def print_lirik():
    line = [
        ("sudahlah kali ini aku kalah",0.10),
        ("kehilangan mahkota",0.09),
        ("kau dan dia pemenang nya,0.07),]
        
    delays=[2, 2.3, 3.2, 1,] 
    
    for i, (line, char_delay) in enumerate(line):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')
print_lirik()
            
        
        
        
