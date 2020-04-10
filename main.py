# Candy the Catacorn
# By @GalaxyAllieCat
# https://github.com/MermaidAllie/Candy-the-Catacorn

# Library seperation by Owain Kenway

# Let's go read a few libraries. Catacorns want knowledge!
from kittylib import *

# Setup everything we use :D
number_stars = 2
n = 30
k = 1
d = 1
i = 30
j = 255

stars = eyes

# Main Loop
while True:    
    n = n + k
    if n > 255:
        k = -1
        n = 255
    if n < 30:
        k = 1
        n = 30
    for s in range(number_stars):
        stars[s] = (20, 0, int(n / 3))
    paws.duty_cycle = 350 - int(n / 2)
    eye_corners.duty_cycle = n * 50
    tail_inner.duty_cycle = n * 30
    tail_outer.duty_cycle = n * 20
    while touch_right_ear.value:
        i = i + d
        j = j - d
        if i > 255 or j < 30:
            i = 255
            j = 30
            d = -1
        if i < 30 or j > 255:
            i = 30
            j = 255
            d = 1
        for s in range(number_stars):
            stars[s] = (191, 0, i)
        paws.duty_cycle = j ** 2
        tail_inner.duty_cycle = i ** 2
        tail_outer.duty_cycle = j ** 2
        eye_corners.duty_cycle = i ** 2
        time.sleep(0.01)
    while touch_left_ear.value:
        eye_pattern = random.randint(0, 3)
        if eye_pattern == 0:
            stars[0] = (180, 0, 255)
            stars[1] = (0, 0, 0)
            time.sleep(random.uniform(0, 0.2))
        if eye_pattern == 1:
            stars[0] = (0, 0, 0)
            stars[1] = (180, 0, 255)
            time.sleep(random.uniform(0, 0.2))
        if eye_pattern == 2:
            stars[0] = (0, 0, 0)
            stars[1] = (0, 0, 0)
            time.sleep(random.uniform(0, 0.2))
        if eye_pattern == 3:
            stars[0] = (180, 0, 255)
            stars[1] = (180, 0, 255)
            time.sleep(random.uniform(0, 0.2))
        eye_corners.duty_cycle = random.choice([0, 65535])
        tail_inner.duty_cycle = random.choice([0, 65535])
        tail_outer.duty_cycle = random.choice([0, 65535])
        paws.duty_cycle = random.choice([0, 65535])
    time.sleep(0.01)
