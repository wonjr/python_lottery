from random import randint

def generate_input_numbers(n):
    numbers = []

    while len(numbers) < n:
        new_number = int(input("1 ~ 45 사이의 숫자 입력"))
        if new_number not in numbers:
            numbers.append(new_number)
        else:
            print("이미 선택하신 숫자입니다. 다시 입력해주세요.")
            continue
    return numbers

def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        new_number = randint(1, 45)
        if new_number not in numbers:
            numbers.append(new_number)

    return numbers


def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


def count_matching_numbers(numbers, winning_numbers):
    cnt = 0
    for i in numbers:
        if i in winning_numbers:
            cnt += 1
    return cnt


def check(numbers, winning_numbers):
    cnt = count_matching_numbers(numbers, winning_numbers[:6])
    b_cnt = count_matching_numbers(numbers, winning_numbers[6:])
    if cnt == 6:
        return 1000000000
    elif cnt == 5 and b_cnt == 1:
        return 50000000
    elif cnt == 5:
        return 1000000
    elif cnt == 4:
        return 50000
    elif cnt == 3:
        return 5000
    else:
        return 0