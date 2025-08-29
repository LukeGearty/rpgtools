import random
import json

with open("loot.json", "r") as f:
    items = json.load(f)


def generate_gold():
    range = items["gold"]
    return random.randint(range["min"], range["max"])


def random_chance(percentage, item):
    if random.random() < percentage:
        loot = items[item]
        return random.choice(loot)
    else:
        return None


def generate_treasure():
    # 30 % chance of generating treasure
    percentage = 0.3
    item = "treasure"
    return random_chance(percentage, item)


def generate_potions():
    # 50% chance of getting potions
    percentage = 0.5
    item = "potions"

    return random_chance(percentage, item)


def generate_junk():
    junk = items["junk"]
    return random.choice(junk)



def main():
    print(f"Gold: {generate_gold()}")

    treasure = generate_treasure()
    if treasure is not None:
        print(f"Treasure: {treasure}")
    potion = generate_potions()
    if potion is not None:
        print(f"Potion: {potion}")
    print(f"Junk: {generate_junk()}")


if __name__=="__main__":
    main()