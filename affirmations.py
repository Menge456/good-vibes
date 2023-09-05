import plyer
from plyer import notification
from tkinter import *
from tkinter import ttk
import time as tm
import random

def affirm():
    notification.notify(title='Eat Food', message = 'Did you eat today?', app_name='selfCare', timeout=5, ticker = 'ticker', toast= "True")
def handle_return(event):
    root.destroy()
    frm.destroy()
    add_to_file = new_affirms.get()
    
    test = add_to_file.lower()
    
    if test != "nothing" and test != "":
        theFile = open("affirmations.txt", "a")
        theFile.write(add_to_file + ": " + tm.ctime() + "\n")
        theFile.close()
    else:
       ''' try: figure out the file not existing error thing
            
        except: '''
   
   
    
lastTime = tm.time()
#gets a random time between 15 and 30 hours to get the next update
#54000, 108000
nextDif = int(random.randrange(2, 3))
while True:
   
    affirm()
    
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    affirms_title = ttk.Label(text = "What's one good thing that happened to you today?")

    #sets up a check for enter for the entry box 
    new_affirms = ttk.Entry()
    new_affirms.bind('<Return>', handle_return)
    affirms_title.pack()
    new_affirms.pack()
    root.mainloop()
    nextDif = int(random.randrange(54000, 108000))
    print(nextDif)
    tm.sleep(nextDif)