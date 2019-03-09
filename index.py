import sys
import numpy as np

import names

print("\n\nName Generator")
print('='*50)

def get_gender():
    while True:
        print('\n\nDo you want a male or female name? (m/f)')
        gender = input('>> ').lower()

        if gender not in ['m', 'male','f', 'female']:
            print('Sorry, at this time only male and female names are supported.')
            print('='*50)
        else:
            return gender

def get_name(gender):
    if gender in ['m', 'male']:
        first = names.first_m[np.random.randint(len(names.first_m))]
    else:
        first = names.first_f[np.random.randint(len(names.first_f))]
    last = names.last[np.random.randint(len(names.last))]

    return [first, last]


def name_print(name):
    print(f'\n\n\033[91m{name[0]} {name[1]}\033[0m')
    print('='*50)

def main():
    while True:
        gender = get_gender()
        name = get_name(gender)
        name_print(name)

        print('\n\nDo you want to play again? [y/n]')
        ans = input('>> ').lower()
        if ans in ['n', 'no']:
            print('Good bye!')
            input('Press enter to exit...')
            break


main()

# Ask for male or female GENDER

# grab random first name FIRST

# grab random last name LAST

# \n\n
# print name and file=sys.stderr
# \n\n

# ask them if they want to play again

# if no then say enter to exit
