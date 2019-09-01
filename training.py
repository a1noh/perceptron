import random

class Point(object):
    x = 0.0
    y = 0.0
    label = 0

    def __init__(self):
        x = random.randint(0, 250)
        y = random.randint(0, 250)
        if (x > y):
            label = 1
        else:
            label = -1