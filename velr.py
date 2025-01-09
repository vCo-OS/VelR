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

def fake_git_clone():
    repo_url = "https://github.com/vCo-OS/VelR"
    cool_print(f"Cloning into 'VelR'...")
    time.sleep(1)
    cool_print(f"remote: Enumerating objects: 42, done.", delay=0.03)
    time.sleep(0.5)
    cool_print(f"remote: Counting objects: 100% (42/42), done.", delay=0.03)
    time.sleep(0.5)
    cool_print(f"remote: Compressing objects: 100% (32/32), done.", delay=0.03)
    time.sleep(0.5)
    cool_print(f"remote: Total 42 (delta 10), reused 42 (delta 10), pack-reused 0", delay=0.03)
    time.sleep(0.5)
    cool_print(f"Receiving objects: 100% (42/42), 1.23 MiB | 2.45 MiB/s, done.", delay=0.03)
    time.sleep(0.5)
    cool_print(f"Resolving deltas: 100% (10/10), done.", delay=0.03)
    time.sleep(0.5)
    cool_print(f"Checking out files: 100% (12/12), done.", delay=0.03)

def main():
    clear_screen()

    cool_print(":: Booting Arch Linux ::", delay=0.07)
    time.sleep(1)

    cool_print("[ INFO ] Initializing system...")
    time.sleep(1)

    cool_print("[ INFO ] To get started, clone the repository:")
    cool_print("    git clone https://github.com/vCo-OS/VelR\n", delay=0.08)
    time.sleep(1)

    cool_print("[ INFO ] Starting clone process...\n", delay=0.08)
    time.sleep(1)

    fake_git_clone()

    cool_print("\n[ INFO ] Booting Rec Room...", delay=0.1)
    time.sleep(1)

    cool_print("\n[ INFO ] Opening link: https://rec.net/user/anonymousmouse52", delay=0.1)
    time.sleep(1)

    # Open the link using the webbrowser module (cross-platform)
    webbrowser.open("https://rec.net/user/anonymousmouse52")

if __name__ == "__main__":
    main()
