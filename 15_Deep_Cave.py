import random, sys, time

# Set up the constants:
WIDTH = 70
PAUSE_AMOUNT = 0.05


print('Deep Cave program')
print('Press Ctrl-C to stop.')
time.sleep(2)

left_width = 20
gap_width = 10

while True:
    # Display the tunnel segment:
    right_width = WIDTH - gap_width - left_width
    print(('#' * left_width) + (' ' * gap_width) + ('#' * right_width))

    # Check for Ctrl-C press during the brief pause:
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()   # When Ctrl-C is pressed, end the program.

    # Adjust the left side width:
    dice_roll = random.randint(1,6)
    if dice_roll == 1 and left_width > 1:
        left_width -= 1   # Decrease left side width.
    elif dice_roll == 2 and left_width + gap_width < WIDTH - 1:
        left_width += 1   # Increase left side width.
    else:
        pass   # Do nothing; no change in left side width.

    # Adjust the gap width:
    dice_roll = random.randint(1,6)
    if dice_roll == 1 and gap_width > 1:
        gap_width -= 1   # Decrease gap width.
    elif dice_roll == 2 and left_width + gap_width < WIDTH - 1:
        gap_width += 1   # Increase gap width.
    else:
        pass   # Do nothing; no change in gap width.

