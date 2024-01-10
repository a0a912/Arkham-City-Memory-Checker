from plyer import notification
import psutil

import time
'''
# Function to send a notification
def send_notification(message):
    notification.notify(
        title='Test Notification',
        message=message,
        app_name='TestApp',
        timeout=10  # Notification timeout in seconds
    )

# Send a test notification with the current time
current_time = time.strftime("%Y-%m-%d %H:%M:%S")
send_notification(f"Test notification - Current time: {current_time}")

# Function to get a list of processes containing a specific string
def get_processes_by_name(name):
    processes = []
    for process in psutil.process_iter(['pid', 'name']):
        if name.lower() in process.info['name'].lower():
            processes.append(process)
    return processes

# Get a list of processes containing the string "steam"
steam_processes = get_processes_by_name("steam")

# Display process details
for process in steam_processes:
    print("------------------------------")
    print(f"Process Name: {process.info['name']}")
    print(f"PID: {process.info['pid']}")
    print(f"Memory Usage: {process.memory_info().rss / (1024 ** 2):.2f} MB")
    print("------------------------------")
'''
def send_notification(message):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    notification.notify(
        title='Test Notification about memory',
        message=f'{message} and current time is {current_time}',
        app_name='TestApp',
        timeout=10  # Notification timeout in seconds
    )

# Function to get a list of processes containing a specific string
def get_processes_by_name(name):
    processes = []
    for process in psutil.process_iter(['pid', 'name']):
        if name.lower() in process.info['name'].lower():
            processes.append(process)
    return processes

def display_process_details(process):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print("------------------------------")
    print(f"Process Name: {process.info['name']}")
    print(f"PID: {process.info['pid']}")
    print(f"Memory Usage: {process.memory_info().rss / (1024**2):.2f} MB")
    print(f"current time is {current_time}")
    print("------------------------------")
'''
while True:
    time.sleep(1)
    # Get a list of processes containing the string "steam"
    steam_processes = get_processes_by_name("steam")
    for process in steam_processes:
        display_process_details(process)
        current_memory = process.memory_info().rss / (1024**2)
        if current_memory > 500:
            send_notification(f"{process.name()} is taking up {current_memory}")
'''
while True:

    # Get a list of processes containing the string "batmanAC"
    batman_processes = get_processes_by_name("batmanAC")
    print(f"length of process is {len(batman_processes)}")
    if batman_processes:
        for process in batman_processes:
            display_process_details(process)
            current_memory = process.memory_info().rss / (1024 ** 2)
            time.sleep(120)
            if current_memory > 2800:
                send_notification(f"{process.name()} is taking up {current_memory}")
    else:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"No Batman Process found at {current_time}")
        time.sleep(10)
