import time
import psutil
import subprocess
import pygetwindow as gw

# ======================================================================
# Copyright (c) 2025 suuhm. All Rights Reserved.
# This software is provided "as is", without any warranty of any kind.
# Inspired by excellent work of:
# https://github.com/EthyMoney/Sennheiser-EPOS-USB-BusyLight-Control
# ======================================================================

# Function to set the color
def set_color(color):
    led_script_path = r"epos-busylight-ng.py" # UNC_WIN_Path: r"C:\Users\..\..\epos-busylight-ng.py"
    if color == "red":
        subprocess.run(["python", led_script_path, "red", "--on"])
    elif color == "green":
        subprocess.run(["python", led_script_path, "green", "--on"])

def monitor_teams():
    # Define combined keyword array (WIP! BETA)
    keywords = [
        ['Activity', 'Aktivität'],  # Activity in English and German
        ['Chat'],                   # Chat
        ['Calendar', 'Kalender'],   # Calendar in English and German
        ['Channel', 'Kanäle'],      # Teams
        ['Calls', 'Anrufe']         # Calls in English and German
    ]
    
    while True:
        teams_process = None
        for proc in psutil.process_iter(['name', 'pid']):
            if proc.info['name'] == "ms-teams.exe":
                teams_process = proc
                break

        if teams_process:
            # Get the window title of the Teams process using pygetwindow
            window_titles = gw.getWindowsWithTitle("Microsoft Teams") 
            
            if window_titles:
                window_title = window_titles[0].title 
                print(f"Teams window title: {window_title}")

                color_set = False
                for keyword_pair in keywords:
                    if any(keyword in window_title for keyword in keyword_pair):
                        # If any keyword from the pair is found in the title, set color to green
                        set_color("green")
                        color_set = True
                        break
                
                if not color_set:
                    # If no match is found, set color to red
                    set_color("red")
            else:
                print("Teams window not found.")

        else:
            print("Teams is not active.")

        # Check the window title every 2 seconds
        time.sleep(2)

monitor_teams()
