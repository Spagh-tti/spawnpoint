import time
import sys

# Rainbow colors (using ANSI escape codes)
colors = [
    '\033[31m',  # Red
    '\033[33m',  # Orange
    '\033[32m',  # Green
    '\033[36m',  # Cyan
    '\033[34m',  # Blue
    '\033[35m',  # Magenta
]

# Reset color code
reset = '\033[0m'

# Main loop
try:
    color_index = 0
    while True:
        # Print the string with current color
        print(f"{colors[color_index]}rainbow{reset}")
        
        # Move to next color (loop back to start after magenta)
        color_index = (color_index + 1) % len(colors)
        
        # Pause for 0.1 seconds
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("\nProgram stopped.")
