from os import system
import re
from itertools import product
from random import choice


class C:
    G = '\033[92m'
    E = '\033[0m'
    Y = '\033[93m'
    R = '\033[91m'
    B = '\033[1m'
    P = '\033[95m'
    BLUE = '\033[94m'


def string_to_number(string):
    sst = u = g = o = 0
    #
    if 's' in string[:3].lower():
        sst += 4
        string = re.sub(r'{S,s}', 'x', string)
    if 'r' in string[:3]:
        u += 4
    if 'w' in string[:3]:
        u += 2
    if 'x' in string[:3]:
        u += 1
    #
    if 's' in string[3:6].lower():
        sst += 2
        string = re.sub(r'{S,s}', 'x', string)
    if 'r' in string[3:6]:
        g += 4
    if 'w' in string[3:6]:
        g += 2
    if 'x' in string[3:6]:
        g += 1
    #
    if 't' in string[6:].lower():
        sst += 1
        string = re.sub(r'{S,s}', 'x', string)
    if 'r' in string[6:]:
        o += 4
    if 'w' in string[6:]:
        o += 2
    if 'x' in string[6:]:
        o += 1
    return f'{sst}{u}{g}{o}'


def number_to_string(number):
    _PERMISSION = ['---', '--x', '-w-', '-wx', 'r--', 'r-x', 'rw-', 'rwx']
    result = []
    for i in str(number)[1:]:
        result.extend(item for item in _PERMISSION[int(i)])
    #
    number = int(str(number)[0])
    if number >= 4:
        number -= 4
        result[2] = 's' if result[2] == 'x' else 'S'
    if number >= 2:
        number -= 2
        result[5] = 's' if result[5] == 'x' else 'S'
    if number == 1:
        result[8] = 't' if result[8] == 'x' else 'T'
    return ''.join(result)


def read_high_score():
    with open('data.log', 'r') as log_file:
        for line in log_file.readlines():
            if '$' in line:
                return int(line[1:-2])
        return 0


def write_high_score(high_score):
    previous_data = []
    with open('data.log', 'r') as log_file:
        for line in log_file.readlines():
            if '$' not in line:
                previous_data.append(line)
    with open('data.log', 'w') as log_file:
        log_file.write(f'${high_score}$\n')
        for item in previous_data:
            log_file.write(item)


def get_log():
    log_list = []
    with open('data.log', 'r') as log_file:
        for line in log_file.readlines():
            if '$' not in line:
                log_list.append(line[:-1])
    return log_list


def generate_random_number():
    NUMS = '01234567'
    list_all_nums = []
    list_all_nums.extend(''.join(it) for it in product(NUMS, NUMS, NUMS, NUMS))
    while True:
        random_number = choice(list_all_nums)
        if choice(list_all_nums) not in get_log():
            return random_number


def write_used_number(number):
    with open('data.log', 'a') as log_file:
        log_file.write(number + '\n')


def generate_random_string():
    return number_to_string(generate_random_number())


if __name__ == '__main__':
    IS_GAME_FINISHED = False
    CURRENT_SCORE = 0
    HIGH_SCORE = read_high_score()
    system('clear')
    print(C.B + 'Welcome to Linux Permission Game!')
    print('Please select the game mode:')
    print('1.Give me the permission number & ask me the string notation')
    print('2.Give me the permission string & ask me the number notation' + C.E)
    print(C.P + f'Your high score: {HIGH_SCORE}' + C.E)
    try:
        game_type = int(input(C.BLUE + '> ' + C.E))
        while not IS_GAME_FINISHED:
            if game_type == 1:
                FLAG = True
                random_permission = generate_random_number()
                print(C.B + f'What is the string notation of {random_permission}?' + C.E)
                while FLAG:
                    user_input = input(C.BLUE + '> ' + C.E)
                    if user_input == number_to_string(random_permission):
                        CURRENT_SCORE += 1
                        print(C.G + 'Correct!')
                        print(f'Current score: {CURRENT_SCORE}' + C.E)
                        write_used_number(random_permission)
                        FLAG = False
                    elif user_input.lower() == 'q':
                        FLAG = False
                        IS_GAME_FINISHED = True
                        if CURRENT_SCORE > HIGH_SCORE:
                            print(C.G + f'Congratulations! You have broken your record: {CURRENT_SCORE}' + C.E)
                            write_high_score(CURRENT_SCORE)
                    elif user_input.lower() == 's':
                        FLAG = False
                    elif user_input.lower() == 'h':
                        print(C.Y + f'You should enter the string notation of the given number ({random_permission}).')
                        test_random_number = generate_random_number()
                        print(f"For example if the number was '{test_random_number}', you should enter '{number_to_string(test_random_number)}'." + C.E)
                    else:
                        print(C.R + 'Wrong!')
                        print("Try again or press 'q' to quit, 's' to skip, 'h' for help." + C.E)
            elif game_type == 2:
                FLAG = True
                random_permission = generate_random_string()
                print(C.B + f'What is the number notation of {random_permission}?' + C.E)
                while FLAG:
                    user_input = input(C.BLUE + '> ' + C.E)
                    if user_input == string_to_number(random_permission):
                        CURRENT_SCORE += 1
                        print(C.G + 'Correct!')
                        print(f'Current score: {CURRENT_SCORE}' + C.E)
                        write_used_number(string_to_number(random_permission))
                        FLAG = False
                    elif user_input.lower() == 'q':
                        FLAG = False
                        IS_GAME_FINISHED = True
                        if CURRENT_SCORE > HIGH_SCORE:
                            print(C.G + f'Congratulations! You have broken your record: {CURRENT_SCORE}' + C.E)
                            write_high_score(CURRENT_SCORE)
                    elif user_input.lower() == 's':
                        FLAG = False
                    elif user_input.lower() == 'h':
                        print(C.Y + f'You should enter the number notation of the given string ({random_permission}).')
                        test_random_string = generate_random_string()
                        print(f"For example if the string was '{test_random_string}', you should enter '{string_to_number(test_random_string)}'." + C.E)
                    else:
                        print(C.R + 'Wrong!')
                        print("Try again or press 'q' to quit, 's' to skip, 'h' for help." + C.E)
            else:
                print(C.R + 'Please enter a valid number!' + C.E)
                game_type = int(input(C.BLUE + '> ' + C.E))
        else:
            print(C.Y + 'The gane has been finished!' + C.E)
    except Exception as e:
        print(C.R + 'Oh no! something went wrong!')
        print(e.message)
