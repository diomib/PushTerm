import os
import subprocess
import sys

def launch_terminal_script():
    script = os.path.abspath("terminal_ui.py")

    if sys.platform.startswith('win'):
        # Open new cmd window, run the Python script, keep window open with a pause prompt at the end
        cmd = f'start cmd /k "python \"{script}\" & echo. & echo Press any key to exit... & pause"'
        subprocess.Popen(cmd, shell=True)
    elif sys.platform.startswith('darwin'):
        # macOS: open Terminal app and run python3 script
        subprocess.Popen(["osascript", "-e", f'tell app "Terminal" to do script "python3 {script}"'])
    elif sys.platform.startswith('linux'):
        # Linux: open gnome-terminal and run python3 script
        subprocess.Popen(["gnome-terminal", "--", "python3", script])
    else:
        print("Unsupported platform. Please run 'terminal_ui.py' manually.")

if __name__ == "__main__":
    launch_terminal_script()
