"""Generate a random name of either gender"""
import numpy as np
import names

print("\n\nName Generator")
print('='*50)

def get_gender():
    """Gets an answer of male or female

    Parameters
    ----------
    None

    Returns
    -------
    gender : str
        Input answer of either male or female.
        Acceptable options: {'m', 'male', 'f', 'female'}

    Example
    -------
    >>>> x = gender()
    >>>> x
    ...
    'male'

    """
    while True:
        print('\n\nDo you want a male or female name? (m/f)')
        gender = input('>> ').lower()

        if gender not in ['m', 'male', 'f', 'female']:
            print('Sorry, at this time only male and female names are supported.')
            print('='*50)
        else:
            return gender

def get_name(gender):
    """Gets random first and last name

    Parameters
    ----------
    gender : str
        Options: {'m', 'male', 'f', 'female'}

    Returns
    -------
    [first, last] : list
        `first` and `last` variables created from module 'names'

    Example
    -------
    >>>> gender = 'male'
    >>>> names = get_name(gender)
    >>>> names
    ...
    ['Jane', 'Doe']

    """
    if gender in ['m', 'male']:
        first = names.first_m[np.random.randint(len(names.first_m))]
    else:
        first = names.first_f[np.random.randint(len(names.first_f))]
    last = names.last[np.random.randint(len(names.last))]

    return [first, last]


def name_print(name):
    """Displays a formatted name

    Parameters
    ----------
    name : list
        Length of list needs to equal 2
        name[0] is first name
        name[1] is last name

    Returns
    -------
    None

    Example
    -------
    >>>> name = ['Jane', 'Doe']
    >>>> name_print(name)
    ...
    Jane Doe
    ==================================================


    """
    print(f'\n\n\033[91m{name[0]} {name[1]}\033[0m')
    print('='*50)

def main():
    """Main function to run game

    """
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
