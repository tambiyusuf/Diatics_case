import random

def unique_positions(n, area_size=500):
    coords = set()
    while len(coords) < n:
        x = random.randint(0, area_size - 1)
        y = random.randint(0, area_size - 1)
        coords.add((x, y))
    return list(coords)
