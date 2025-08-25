#!/usr/bin/env python3
import random
import sys

"""

A utility to roll dice and get randomized numbers

Usage: ./roll_dice.py <num of Dice>d<dice sides>
    Ex: ./roll_dice.py 3d12

"""

def roll_dice(num: int):
    return random.randint(1, num)


def roll_dice_x_times(num_dice: int, dice: int):
    """
    
    roll a x sided dice y number of times

    """

    results = [roll_dice(dice) for _ in range(num_dice)]
    print(f"Rolls: {results} | Total: {sum(results)}")

def main():

    if (len(sys.argv) != 2):
        print("Usage: ./roll_dice.py <num of dice>d<dice to roll>")
        sys.exit()
    argument = sys.argv[1:]

    #checks
    if 'd' not in argument[0]:
        print("Usage: ./roll_dice.py <num of dice>d<dice to roll>")
        sys.exit()
    try:
        #split based on 'd'
        nums = argument[0].split('d')
        num_dice = int(nums[0])
        dice = int(nums[1])
        if (num_dice <= 0 or dice <= 0):
            print("Number of dice and sides must be positive integers")
            sys.exit(1)
        roll_dice_x_times(num_dice, dice)
    except ValueError:
        print("Usage: ./roll_dice.py <num of dice>d<dice to roll>")
        sys.exit()
    

if __name__=="__main__":
    main()