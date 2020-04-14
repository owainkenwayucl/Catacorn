import kittylib as kl
import time

speed = [60,90,120,180]
measure = [4,3,6]

m = 0
s = 0

count = 0
while True:    
    start = time.monotonic()

    lpressed = False
    rpressed = False

    while kl.touch_right_ear.value:
        rpressed = True
        kl.right_eye(kl.green)

    while kl.touch_left_ear.value:
        lpressed = True
        kl.left_eye(kl.green)

    if (rpressed):
        m = (m+1) % len(measure)	
#        print(measure[m])

    if (lpressed):
        s = (s+1) % len(speed)
#        print(speed[s])

    gap = 60/speed[s]
    
    if (count%measure[m] == 0):
       kl.left_eye(kl.black)
       kl.paws.duty_cycle = 20000
       kl.eye_corners.duty_cycle = 10000
    kl.right_eye(kl.black)
    time.sleep(0.05)
    kl.left_eye(kl.dark_white)
    kl.right_eye(kl.dark_white)
    kl.paws.duty_cycle = 10000
    kl.eye_corners.duty_cycle = 20000

    if (count%2 == 0):
       kl.tail_inner.duty_cycle = 20000
       kl.tail_outer.duty_cycle = 5000
    else:
       kl.tail_inner.duty_cycle = 5000
       kl.tail_outer.duty_cycle = 20000


    count += 1
    finish = time.monotonic()
    time.sleep(max(0,gap - (finish - start)))
