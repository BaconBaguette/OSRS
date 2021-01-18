from ahk import AHK
from time import sleep
from random import randint, uniform

ahk = AHK()

enchant_four = [[2435,1205],[2455,1220]]

desktop_inventory = [                          [[2385,1105],[2410,1125]], [[2430,1105],[2455,1125]], [[2470,1105],[2495,1125]],
                    [[2345,1140],[2370,1160]], [[2385,1140],[2410,1160]], [[2430,1140],[2455,1160]], [[2470,1140],[2495,1160]],
                    [[2345,1175],[2370,1195]], [[2385,1175],[2410,1195]], [[2430,1175],[2455,1195]], [[2470,1175],[2495,1195]],
                    [[2345,1210],[2370,1230]], [[2385,1210],[2410,1230]], [[2430,1210],[2455,1230]], [[2470,1210],[2495,1230]],
                    [[2345,1245],[2370,1265]], [[2385,1245],[2410,1265]], [[2430,1245],[2455,1265]], [[2470,1245],[2495,1265]],
                    [[2345,1285],[2370,1305]], [[2385,1285],[2410,1305]], [[2430,1285],[2455,1305]], [[2470,1285],[2495,1305]],
                    [[2345,1320],[2370,1340]], [[2385,1320],[2410,1340]], [[2430,1320],[2455,1340]], [[2470,1320],[2495,1340]]]

pc_type = input("Desktop or Laptop?")

if pc_type.upper() == "DESKTOP":
    inventory = desktop_inventory
elif pc_type.upper() == "LAPTOP":
    # Need to add pixels for laptop
    inventory = 'laptop inventory'

def get_random_coords(coords):
    random_x = randint(coords[0][0], coords[1][0])
    random_y = randint(coords[0][1], coords[1][1])
    return [random_x, random_y] 

sleep(5)

for slot_coords in inventory:
    random_enchant_coords = get_random_coords(enchant_four)
    random_slot_coords = get_random_coords(slot_coords)

    ahk.mouse_move(random_enchant_coords[0], random_enchant_coords[1])
    ahk.click()
    sleep(uniform(0.2, 0.5))
    ahk.mouse_move(random_slot_coords[0], random_slot_coords[1])
    ahk.click()
    sleep(uniform(1.2, 1.5))


