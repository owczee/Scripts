import pyautogui as auto
import pyautogui
import cv2
import sys
import random
import time

# We assume that we are taking in 5 super combat pots,
# in the first row/left first spot of second
POTS = [
    {'coords': [937, 595], 'doses': 4},
    {'coords': [1004, 599], 'doses': 4},
    {'coords': [1067, 594], 'doses': 4}
]

ABSORBS = [
    {'coords': [1004, 698], 'doses': 4},
    {'coords': [1064, 701], 'doses': 4},
    {'coords': [939, 700], 'doses': 4},
    {'coords': [936, 754], 'doses': 4},
    {'coords': [879, 758], 'doses': 4},
    {'coords': [1002, 760], 'doses': 4},
    {'coords': [1062, 755], 'doses': 4},
    {'coords': [1067, 810], 'doses': 4},
    {'coords': [1002, 812], 'doses': 4},
    {'coords': [938, 809], 'doses': 4},
    {'coords': [876, 808], 'doses': 4},
    {'coords': [879, 865], 'doses': 4},
    {'coords': [942, 862], 'doses': 4},
    {'coords': [1004, 863], 'doses': 4},
    {'coords': [1067, 865], 'doses': 4},
    {'coords': [1057, 920], 'doses': 4},
    {'coords': [1003, 918], 'doses': 4},
    {'coords': [942, 915], 'doses': 4},
    {'coords': [875, 922], 'doses': 4}
]

# Use the rock cake
RockCake = [873, 589]


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)

        timeformat = f'{mins:02d}:{secs:02d}'
        # create a countdown using countdown(seconds) seconds being how many seconds the countdown will be.
        print(timeformat, end='\n')

        time.sleep(1)
        time_sec -= 1

    print("stop")


def eat_rockcake():
    start = pyautogui.locateCenterOnScreen('rock.png', confidence=0.7)
    print(start)
    # pyautogui.click('rock.png')
    # x, y = RockCake[0], RockCake[1]
    auto.moveTo(start, duration=1, tween=pyautogui.easeInOutQuad)
    auto.click()
    time.sleep(random.randint(1, 2))


def drink_overload():
    for pot in POTS:
        # If still doses in this pot, drink. If not check next
        if pot['doses'] > 0:
            x, y = pot['coords'][0], pot['coords'][1]
            time.sleep(1)
            auto.moveTo(random.randint(x - 4, x + 4), random.randint(y - 4, y + 5), duration=1,
                        tween=pyautogui.easeInOutQuad)
            auto.click()
            pot['doses'] -= 1
            print('-10 Seconds For Overload')
            time.sleep(10)
            break


def drink_absorbs(doses):
    for _ in range(doses):
        for pot in ABSORBS:
            # If still doses in this pot, drink. If not check next
            if pot['doses'] > 0:
                x, y = pot['coords'][0], pot['coords'][1]
                auto.moveTo(random.randint(x - 4, x + 4), random.randint(y - 4, y + 5), duration=1,
                            tween=pyautogui.easeInOutQuad)
                auto.click()
                pot['doses'] -= 1
                time.sleep(random.uniform(1.5, 2.2))
                break


def main():
    print('Press Ctrl-C to quit.')

    # threshold time for repotting (seconds)

    drink_overload()

    overload_threshold = 295
    absorb_threshold = 150

    potion_threshold_multiplier = random.randint(1, 4)

    overload_start_time = time.time()
    absorb_start_time = time.time()
    drank_overload = False
    drank_absorb = False

    try:
        while True:
            print('Waiting 12-20 Seconds')
            countdown(random.randint(12, 20))
            drank_overload = False
            drank_absorb = False

            # check to see if we need to use overload.
            if (time.time() - overload_start_time) > overload_threshold:
                print('Drinking Overload')
                drink_overload()
                overload_start_time = time.time()
                drank_overload = True

            elif (time.time() - overload_start_time) < overload_threshold:
                print('Eating Rockcake')
                eat_rockcake()

            # check to see if we need to drink absorbs.
            if (time.time() - absorb_start_time) > absorb_threshold:
                print('Drinking Absorbs')
                drink_absorbs(potion_threshold_multiplier)
                absorb_start_time = time.time()
                drank_absorb = True

            if drank_absorb or drank_overload:
                auto.moveTo(873, 589, duration=1, tween=pyautogui.easeInOutQuad)

    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)


if __name__ == "__main__":
    main()
