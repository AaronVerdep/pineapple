import sys
import os
import time

# Pineapple Is an open-source universal tool for doing everything you want. Yeah! You can do everything.
# If you are reading this, God bless you so much!! Amen.

script_path = os.path.abspath(__file__)

folder_path = os.path.dirname(script_path)

if len(sys.argv) > 1:
    arg = sys.argv[1]
    if os.path.exists(f"{folder_path}/commands/{arg}"):
        with open(f'{folder_path}/commands/{arg}/main.pineapple_main', 'r'):
            os.system(f'python3 {folder_path}/commands/{arg}/main.pineapple_main')
    else:
        print('[ERROR] Command not found.')
else:
    print('Usage: pineapple <command>')
