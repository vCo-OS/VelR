import time
import sys
import os
import webbrowser

def cool_print(message, delay=0.05):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation():
    spinner = "|/-\\"
    for _ in range(10):
        for frame in spinner:
            sys.stdout.write(f"\r[    ] {frame} Loading...")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r[ OK ] Loading complete.         \n")

def linux_loading_effect():
    loading_texts = [
        "[ OK ] Initializing system...",
        "[ OK ] Loading kernel modules...",
        "[ OK ] Verifying file system integrity...",
        "[ OK ] Mounting root filesystem...",
        "[ OK ] Starting udev services...",
        "[ OK ] Activating swap partitions...",
        "[ OK ] Configuring network interfaces...",
        "[ OK ] Starting system logging daemon...",
        "[ OK ] Enabling user-space modules...",
        "[ OK ] Finalizing boot sequence...",
    ]
    for text in loading_texts:
        cool_print(text, delay=0.07)
        time.sleep(0.3)

def error_message():
    cool_print("[ !! ] ERROR: Missing critical dependencies!", delay=0.1)
    time.sleep(0.5)
    cool_print("[ !! ] Attempting fallback recovery...")

    for i in range(3, 0, -1):
        sys.stdout.write(f"\r[ !! ] Recovery in {i}...")
        sys.stdout.flush()
        time.sleep(1)
    print("\r[ !! ] Fallback recovery failed.              ")

def run_appimage():
    """Simulates running the app image."""
    clear_screen()
    cool_print("ERROR: This machine is not certified to run Project Velocity!", delay=0.07)
    time.sleep(1)
    cool_print("Returning to machine...")
    time.sleep(2)
    sys.exit(1)

def display_hint():
    """Provides a hint about the Easter egg."""
    cool_print("\n[ HINT ] Curious about hidden functionality?")
    cool_print("[ HINT ] Try running the script with a special argument...")
    cool_print("[ HINT ] Maybe '--appimage' will reveal something?\n", delay=0.1)

def main():
    # Check if the script is run as a standalone "AppImage"
    if len(sys.argv) > 1 and sys.argv[1] == "--appimage":
        run_appimage()
        return

    clear_screen()

    cool_print(":: Booting Arch Linux ::", delay=0.07)
    time.sleep(1)

    loading_animation()
    linux_loading_effect()

    error_message()
    time.sleep(1)

    cool_print("\n[ INFO ] Booting Rec Room...", delay=0.1)
    time.sleep(1)

    cool_print("\n[ INFO ] Opening link: https://rec.net/user/anonymousmouse52", delay=0.1)
    time.sleep(1)

    # Display the hint for the Easter egg
    display_hint()

    # Open the link using the webbrowser module (cross-platform)
    webbrowser.open("https://rec.net/user/anonymousmouse52")

if __name__ == "__main__":
    main()
