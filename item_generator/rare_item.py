#!/usr/bin/env python3
import random
import json
import sys

with open("items.json", "r") as f:
    items = json.load(f)

with open("descriptions.json", "r") as f:
    descriptions = json.load(f)


def generate_item():
    category = random.choice(list(items.keys()))

    if category == "potions":
        potion = random.choice(items[category])
        return potion
    item = random.choice(items[category])
    
    prefix = random.choice(descriptions["prefixes"]) if random.random() < 0.5 else ""
    suffix = random.choice(descriptions["suffixes"]) if random.random() < 0.7 else ""

    return " ".join(word for word in [prefix, item, suffix] if word)


def main():
    if len(sys.argv) != 2:
        print("Usage: ./rare_items.py <numOfItems>")
        sys.exit()
    try:
        num_items = int(sys.argv[1])
        for _ in range(num_items):
            print(generate_item())
    except ValueError:
        print("Please enter a number on the next go around")
        sys.exit()


if __name__=="__main__":
    main()