"""Old School Runescape NMZ Training Bot
Written by Cole Boothman, April 2018 (Updated April 2020)
UPDATE APRIL 2020: This is a bot for AFK training in NMZ for OSRS.
The bot will flick your hp prayer, drink pots and absorbs pots.
To run:
- needs to be configured for each computer. Uncomment the coordinate section
and fill in the coordinates by using the center of each icon in OSRS that
is needed. (quick pray icon and inv slots)
- make sure you set the threshold for combat pots repot time, and absorbs.
for absorbs, time the amount of time it takes for the monsters to drain 1
dose of absorb pot and use that as a reference (add like 5-10 secs extra).
- boot up Runelite, and make sure you snap the window and always run it in
this place on the screen, since the coordinates will rely on this.
- go in nmz, rock cake to 1hp, then run the script.
The absorb pots randomly wait between 1-4 'thresholds' that you've set and 
will drink the proper amount of doses associated with the threshold multipler.
Enjoy!
"""
import mouse as auto
import sys
import random
import time

# We assume that we are taking in 5 super combat pots, 
# in the first row/left first spot of second
POTS = [
    {'coords': [625, 398], 'doses': 4},
    {'coords': [667, 394], 'doses': 4},
    {'coords': [710, 394], 'doses': 4}
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


# FOR FINDING COORDS ON SCREEN
# try:
#     while True:
#         x, y = auto.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr),
#         print('\b' * (len(positionStr) + 2)),
#         sys.stdout.flush()
# except KeyboardInterrupt:
#     print('\n')


def countdown(time_sec):
    while time_sec:

        mins, secs = divmod(time_sec, 60)

        timeformat = f'{mins:02d}:{secs:02d}'
        # create a countdown using countdown(seconds) seconds being how many seconds the countdown will be.
        print(timeformat, end='/r')

        time.sleep(1)
        time_sec -= 1

    print("stop")


def eat_rockcake():
    x, y = RockCake[0], RockCake[1]
    #rocktimer = countdown(random.randint(70, 80))
    print("using rockcake")
    # Weird behaviour with using the auto.click=(clicks=2) but below works.
    auto.click()
    countdown(random.randint(1,5))
    auto.click()
    countdown(random.randint(1,5))
    auto.click()


def drink_overload():
    for pot in POTS:
        # If still doses in this pot, drink. If not check next
        if pot['doses'] > 0:
            x, y = pot['coords'][0], pot['coords'][1]
            auto.move(random.randint(x - 4, x + 4), random.randint(y - 4, y + 5), 0.5)
            auto.click()
            print("drinking overload")
            pot['doses'] -= 1
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
    #countdown(10)
    drink_overload()
    absorb_threshold_multiplier = random.randint(1, 4)
    overload_start_time = time.time()
    absorb_start_time = time.time()
    # threshold time for repotting (seconds)
    overload_threshold = random.randint(300, 330)
    absorb_threshold = random.randint(100, 800)

    drank_pots = False
    try:
        while True:
            # hp resets every min, so we reset every 45-50 seconds.
            # If we drank pots (mainly absorbs) that'll take some time... so reset faster
            time.sleep(random.randint(35, 40)) if drank_pots else time.sleep(random.randint(45, 50))
            eat_rockcake()
            drank_pots = False

            # check to see if we need to use overload.
            if (time.time() - overload_start_time) > overload_threshold:
                drink_overload()
                overload_start_time, drank_pots = time.time(), True

            # check to see if we need to drink absorbs.
            if (time.time() - absorb_start_time) > (absorb_threshold * absorb_threshold_multiplier):
                drink_absorbs(absorb_threshold_multiplier)
                absorb_start_time, absorb_threshold_multiplier = time.time(), random.randint(1, 4)
                drank_pots = True

            # if we drank a pot, move back to prayer orb
            if drank_pots:
                auto.move(RockCake, 0.5)

    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)


if __name__ == "__main__":
    main()