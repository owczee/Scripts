from pyHM import mouse as auto
import time
import sys

#looping

def main():
    try:
        while True:
         #   print("starting in 1 second")
            time.sleep(2)
            print(auto.get_current_position())

    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)

if __name__ == "__main__":
    main()
