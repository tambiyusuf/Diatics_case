import numpy as np 
import json
import matplotlib.pyplot as plt 
from Animals import Sheep, Wolf, Cow, Hen, Lion, Hunter, Cockerel
from util import unique_positions
import random 
import math 
import time 
with open("counts.json", "r") as f:
    species_counts = json.load(f)

class_map = {
    "Sheep": Sheep,
    "Wolf": Wolf,
    "Cow": Cow,
    "Hen": Hen,
    "Cockerel": Cockerel,
    "Lion": Lion,
    "Hunter": Hunter
}

positions = unique_positions(sum(species["count"] for species in species_counts))
animals = []

for i in species_counts:
    Class = class_map[i["class"]]
    count = i["count"]
    gender = i.get("gender", None)
    for _ in range(count):
        x, y = positions.pop(0)
        if Class in [Hen, Cockerel, Hunter]:
            animal = Class(x, y)
        else:
            animal = Class(x, y, gender=gender)
        animals.append(animal)
        

print("Toplam hayvan sayısı:", len(animals))

grid = np.zeros((500,500), dtype=int)

for animal in animals:
    x, y = animal.get_location()
    grid[x, y] = animal.code

for step in range(1000):
    print(f"\n--- Adım {step+1} ---")

    # Hareket
    for animal in animals:
        if not animal.alive:
            continue
        axis = random.choice(['dx', 'dy'])
        direction = random.choice([-1, 1])
        if axis == 'dx':
            animal.move(dx=direction)
        else:
            animal.move(dy=direction)

    # Avcı
    for animal in animals:
        if animal.code == 6 and animal.alive:
            hx, hy = animal.get_location()
            for target in animals:
                if target is animal or not target.alive:
                    continue
                tx, ty = target.get_location()
                distance = math.sqrt((hx - tx) ** 2 + (hy - ty) ** 2)
                if distance <= 8:
                    target.alive = False
                    print(f"Avcı {animal.type} ({hx},{hy}), {target.type} ({tx},{ty}) avladı.")

    # Aslan
    for animal in animals:
        if animal.code == 5 and animal.alive:
            lx, ly = animal.get_location()
            for target in animals:
                if target is animal or not target.alive:
                    continue
                if target.code in [2, 0]:  # Cow(2), Sheep(0)
                    tx, ty = target.get_location()
                    distance = math.sqrt((lx - tx) ** 2 + (ly - ty) ** 2)
                    if distance <= 5:
                        target.alive = False
                        print(f"Aslan {animal.type} ({lx},{ly}), {target.type} ({tx},{ty}) avladı.")

    # Kurt
    for animal in animals:
        if animal.code == 1 and animal.alive:
            wx, wy = animal.get_location()
            for target in animals:
                if target is animal or not target.alive:
                    continue
                if target.code in [3, 4, 0]:  # Hen(3), Cockerel(4), Sheep(0)
                    tx, ty = target.get_location()
                    distance = math.sqrt((wx - tx) ** 2 + (wy - ty) ** 2)
                    if distance <= 4:
                        target.alive = False
                        print(f"Kurt {animal.type} ({wx},{wy}), {target.type} ({tx},{ty}) avladı.")




    # Üreme 
    new_borns = []
    checked_pairs = set()
    mated_animals = set()
    occupied_positions = set((a.x, a.y) for a in animals if a.alive)

    for i, a1 in enumerate(animals):
        if not a1.alive or id(a1) in mated_animals:
            continue
        for j, a2 in enumerate(animals):
            if i >= j or not a2.alive or id(a2) in mated_animals:
                continue
            if a1.type == a2.type and hasattr(a1, 'gender') and hasattr(a2, 'gender') and a1.gender != a2.gender:
                pair_key = tuple(sorted([id(a1), id(a2)]))
                if pair_key in checked_pairs:
                    continue
                dist = math.sqrt((a1.x - a2.x) ** 2 + (a1.y - a2.y) ** 2)
                if dist <= 3:
                    checked_pairs.add(pair_key)
                    mated_animals.add(id(a1))
                    mated_animals.add(id(a2))
                    genders = ["Male", "Female"]
                    new_gender = random.choice(genders)
                    
                    while True:
                        new_x = random.randint(0, 499)
                        new_y = random.randint(0, 499)
                        if (new_x, new_y) not in occupied_positions:
                            occupied_positions.add((new_x, new_y))
                            break
                    
                    if a1.type in ["Hen", "Cockerel"]:
                        if new_gender == "Male":
                            Class = Cockerel
                            new_borns.append(Class(new_x, new_y))
                            print(f"{a1.type} ({a1.x},{a1.y}) ve {a2.type} ({a2.x},{a2.y}) çiftleşti, yeni doğan: Cockerel ({new_x},{new_y})")
                        else:
                            Class = Hen
                            new_borns.append(Class(new_x, new_y))
                            print(f"{a1.type} ({a1.x},{a1.y}) ve {a2.type} ({a2.x},{a2.y}) çiftleşti, yeni doğan: Hen ({new_x},{new_y})")
                    else:
                        Class = type(a1)
                        new_borns.append(Class(new_x, new_y, new_gender))
                        print(f"{a1.type} ({a1.x},{a1.y}) ve {a2.type} ({a2.x},{a2.y}) çiftleşti, yeni doğan: {a1.type} ({new_x},{new_y}, {new_gender})")
                    break

    
    animals.extend(new_borns)
    
    # Rapor
    type_counts = {}
    for animal in animals:
        if animal.alive:
            t = animal.type
            type_counts[t] = type_counts.get(t, 0) + 1
    print(f"Canlı tür sayıları: {type_counts}")
    print(f"Toplam canlı: {sum(type_counts.values())}")
    time.sleep(0.5)

print("\nSimülasyon tamamlandı.")