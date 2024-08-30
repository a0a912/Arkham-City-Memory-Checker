from plyer import notification
import psutil

import time

#Return current date and time
def get_current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")


#This function sends a desktop notification letting me know Arkham City is close to crashing.
def send_notification(message):
    notification.notify(
        title='Arkham City Memory Alert',
        message=f'{message} and current time is {get_current_time()}',
        app_name='TestApp',
        timeout=10  # Notification timeout in seconds
    )

# Function to get a list of processes containing a specific string. I use this to get info on Arkham City's process
def get_processes_by_name(name):
    processes = []
    for process in psutil.process_iter(['pid', 'name']):
        if name.lower() in process.info['name'].lower():
            processes.append(process)
    return processes

#This function outputs info regarding the Arkham City Process to the terminal.
def display_process_details(process):
    print("------------------------------")
    print(f"Process Name: {process.info['name']}")
    print(f"PID: {process.info['pid']}")
    print(f"Memory Usage: {process.memory_info().rss / (1024**2):.2f} MB")
    print(f"current time is {get_current_time()}")
    print("------------------------------")

while True:

    # Get a list of processes containing the string "batmanAC"
    batman_processes = get_processes_by_name("batmanAC")
    #Check if the process is running
    print(f"length of process is {len(batman_processes)}")
    if batman_processes:
        #If Arkham City is running:
        for process in batman_processes:
            #Print info regarding the process to the terminal:
            display_process_details(process)
            #Get the current amount of memory being used
            current_memory = process.memory_info().rss / (1024 ** 2)
            #if the game is taking up 2.8GB of memory, send a notification. Otherwise, check again in 2 minutes
            if current_memory > 2800:
                send_notification(f"{process.name()} is taking up {current_memory}")
            #Sleep for 2 minutes
            time.sleep(120)

    else:
        #If Batman Arkham City isn't running, check again in 5 seconds
        print(f"No Batman Process found at {get_current_time()}. Checking again in 5 seconds.")
        time.sleep(5)
