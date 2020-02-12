import time
import datetime as dt
import tkinter
from tkinter import messagebox
from tkinter import simpledialog
import winsound

# hide main window
root = tkinter.Tk()
root.withdraw()

total_pomodoros = 0

# Formulating the pomodoro slots
t_now = dt.datetime.now() #Fetch current time
t_pom = 25*60 #Default time for pomodoro slot 
t_delta = dt.timedelta(0, t_pom) #Default time for pomodoro in minutes
t_fut = t_now + t_delta #Ending time of pomodoro slot                             
delta_sec = 5*60 #Break time for pomodoro
t_fin = t_now + dt.timedelta(0, t_pom+delta_sec) #Total time for pomodoro including break

'''
#Creating a website blocker
# Changing the hosts file in C:\Windows\System32\drivers\etc folder allows to redirect any IP address to our local host
# Hence, preventing it to be accessed

hosts_path = r'C:\Windows\System32\drivers\etc'
redirect_path = "127.0.0.1"
# check paths are read correctly by pc
print("-"*40+f"\nCurrent host path: \n{hosts_path}"+"\n"+"-"*40)

#List of websites that are distracting and should not be opened during pomodoro slot
website_list = ["www.facebook.com",
                "facebook.com", ]


def add_websites(filepath):
    """
    This function adds the websites to the block list when the pomodoro slot starts
    """
    with open(filepath+"/hosts", "r+") as dummy_file:
        content = dummy_file.read()
        # Now, we need to check if the websites are already in the content. If they are
        # don't do anything. If they are not, go add them
        for website in website_list:
            if website in content: 
                pass
            else:
                dummy_file.write(redirect_path+"\t"+website+"\n")
                
def remove_websites(filepath):
    """
    This function removes the websites from the block list after the pomodoro slot is over
    """
    with open(filepath+"/hosts", "r+") as file:
        # content is now a list with strings for each line in the text file
        content = file.readlines()
        file.seek(0)
        # iterate through lines of conent.
        for lines in content:
            # If the website string is not in the line, boolean will be True, therefore, write that line again
            if not any(website in lines for website in website_list):
                file.write(lines)
                # print('written')
        # truncating a file deletes everything forward from the point it ended at
        file.truncate()


print(f"Bug check 0: \nt_now: {t_now}\nt_fut: {t_fut}")
'''
# Crafting the GUI
messagebox.showinfo("Pomodoro Timer Started!", "\nIt is now "+t_now.strftime("%H:%M") +
                    " hrs. \nTimer set for 25 mins.")

# Implementation of the heart of the pomodoro concept
while True:
    # When the pomodoro slot is going on
    if t_now < t_fut:
        #Block the websites
        '''
        add_websites(hosts_path)
        '''
        pass

    #During the break
    elif t_fut <= t_now <= t_fin:
        
        for i in range(10):
                winsound.Beep((i+100), 500)
        #Unblock the websites
        '''       
        remove_websites(hosts_path)
        '''
        
    
    else:
        #Alert that on completion of break
        for i in range(10):
            winsound.Beep((i+100), 500)
        '''
        remove_websites(hosts_path)
        '''

        #Check if the user wants to continue for a new pomodoro session
        usr_ans = messagebox.askyesno("Pomodoro Slot is over!", "Do you want to start another pomodoro slot?")
        total_pomodoros += 1
        if usr_ans == True:
            t_now = dt.datetime.now()
            t_fut = t_now + dt.timedelta(0, t_pom)
            t_fin = t_now + dt.timedelta(0, t_pom+delta_sec)
            continue
        elif usr_ans == False:
            messagebox.showinfo("Current Pomodoro Session is over", "\nIt is now "+timenow +"\nYou took "+str(total_pomodoros)+" pomodoro slots today!")
            break
    # check every 3 seconds and update current time
    time.sleep(20)
    t_now = dt.datetime.now()
    timenow = t_now.strftime("%H:%M")


