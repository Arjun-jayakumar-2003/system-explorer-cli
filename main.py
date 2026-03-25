#!/usr/bin/env python3
     
import os
import shutil
import psutil
from datetime import datetime

current_path = os.getcwd()


def ls(path):
    if os.path.exists(path) and os.path.isdir(path):
            items = sorted(os.listdir(path))
            for item in items:
                full_path = os.path.join(path , item)
            
                if os.path.isdir(full_path):
                    print(f"{item}/")
                else:
                    print(f"{item}")
    else:
            print("Invalid Directory")
    


    
def formatted_size(size):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        else:
            size /= 1024
    
    
def current_working_directory():
    path = current_path
    print(f"Current working directory is : {path}")
    ls(path)
    
    
    
    
def custom_directory():
    path = input("Enter absolute path to directory: ").strip()
    print(f"Given directory is : {path}")
    ls(path)



def list_files():
    print("\n Choose an option: ")
    print("1. Print files in current working directory")
    print("2. Print files in another directory")
    print("q. Quit")
        
    sub_choice = input("Enter your choice: ").strip().lower()
    
    if sub_choice == "1":
        current_working_directory()
    elif sub_choice == "2":
        custom_directory()
    elif sub_choice == "q" or sub_choice == "quit":
        print("Exiting Sub Menu....")

    
    
def disk_usage():
    total, used, free = shutil.disk_usage("/")
    print(f"Total space = {formatted_size(total)}")
    print(f"Used space = {formatted_size(used)}")
    print(f"Free space = {formatted_size(free)}")   
    
    
def running_process():
    lines = []
    
    lines.append("PID\tNAME")
    lines.append("-" * 25)
    
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            lines.append(f"{proc.info['pid']}\t{proc.info['name']}")
        except(psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    output = "\n".join(lines)
    print(output)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("process_log.txt", "a") as f:
        f.write(f"\n[{timestamp}]\n")
        f.write(output + "\n")
# NOTE:
# Log file is created in the current working directory.
# Running the script from different locations will create separate log files.           
            
            
while True:
    print("\n Choose an option: ")
    print("1.List Files")
    print("2.Show Disk Usage")
    print("3.Show Running Processes")
    print("q.Quit")
    
    main_choice = input("Enter your choice: ").strip().lower()
    
    if main_choice == "1":
        list_files()
    elif main_choice == "2":
        disk_usage()
    elif main_choice == "3":
        running_process()
    elif main_choice == "q" or main_choice == "quit":
        print("Exiting...")
        break
    else:
        print("Invalid Choice... Try Again")
        
            
            
            
        
            
        
        
    
        
