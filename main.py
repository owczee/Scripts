import mouse as auto
import sys
import random
import time

# We assume that we are taking in 5 super combat pots,
# in the first row/left first spot of second
POTS = [
    {'coords': [625, 398], 'doses': 1},
    {'coords': [667, 394], 'doses': 1},
    {'coords': [710, 394], 'doses': 1}
]

ABSORBS = [
    {'coords': [586, 608], 'doses': 4},
    {'coords': [627, 608], 'doses': 4},
    {'coords': [668, 609], 'doses': 4},
    {'coords': [624, 576], 'doses': 4},
    {'coords': [582, 573], 'doses': 4},
    {'coords': [665, 570], 'doses': 4},
    {'coords': [666, 537], 'doses': 4},
]

# Use the rock cake
RockCake = [585, 391]


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
    print("using rockcake")
    x, y = RockCake[0], RockCake[1]
    auto.move(random.randint(x - 4, x + 4), random.randint(y - 4, y + 5), 0.5)
    auto.click()
    time.sleep(random.randint(1, 2))
    auto.click()
    time.sleep(random.randint(1, 2))
    auto.click()
    time.sleep(random.randint(1, 2))
    auto.click()
    time.sleep(random.randint(1, 2))
    auto.click()
    time.sleep(random.randint(1, 2))
    auto.click()
    time.sleep(random.randint(1, 2))
    auto.click()
    time.sleep(random.randint(1, 2))
    auto.click()



def drink_overload(doses):
    for _ in range(doses):
        for pot in POTS:
            # If still doses in this pot, drink. If not check next
            if pot['doses'] > 0:
                x, y = pot['coords'][0], pot['coords'][1]
                time.sleep(1)
                auto.move(random.randint(x - 4, x + 4), random.randint(y - 4, y + 5), 0.5)
                auto.click()
                print("drinking overload")
                pot['doses'] -= 1
                time.sleep(1)
                break


def drink_absorbs(doses):
    for _ in range(doses):
        for pot in ABSORBS:
            # If still doses in this pot, drink. If not check next
            if pot['doses'] > 0:
                x, y = pot['coords'][0], pot['coords'][1]
                auto.move(random.randint(x - 4, x + 4), random.randint(y - 4, y + 5), 0.5)
                auto.click()
                pot['doses'] -= 1
                print("drinking absorb")
                time.sleep(random.uniform(1.5, 2.2))
                break


def main():

    print('Press Ctrl-C to quit.')

    # threshold time for repotting (seconds)
    overload_threshold = random.randint(300, 330)
    absorb_threshold = random.randint(80, 90)

    potion_threshold_multiplier = random.randint(1, 4)

    drank_overload = False
    drank_absorb = False
    drink_overload(1)
    drink_absorbs(4)
    eat_rockcake()

    overload_start_time = time.time()
    absorb_start_time = time.time()


    try:
        while True:
            countdown((random.randint(55, 65)))
            drank_overload = False
            drank_absorb = False

            # check to see if we need to use overload.
            if (time.time() - overload_start_time) > overload_threshold:
                drink_overload(potion_threshold_multiplier)
                overload_start_time = time.time()
                drank_overload = True

            # check to see if we need to drink absorbs.
            if (time.time() - absorb_start_time) > (absorb_threshold):
                drink_absorbs(potion_threshold_multiplier)
                absorb_start_time = time.time()
                potion_threshold_multiplier = random.randint(1, 4)
                drank_absorb = True

            if drank_absorb or drank_overload:
                x, y = RockCake[0], RockCake[1]
                auto.move(random.randint(x - 4, x + 4), random.randint(y - 4, y + 5), 0.5)

            eat_rockcake()


    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)


if __name__ == "__main__":
    main()