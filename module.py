from random import randint


def set_enemy_health():
    return randint(80, 120)


def get_lite_attack():
    return randint(2, 5)


def get_mid_attack():
    return randint(15, 25)


def get_hard_attack():
    return randint(30, 40)


def compare_values(enemy_health, user_total_attack):
    point_difference = abs(enemy_health - user_total_attack)
    return point_difference <= 10


# Keep the old spelling available for existing imports.
compare_valumes = compare_values


def get_user_attack():
    total = 0
    attacks_types = {
        'lite': get_lite_attack,
        'mid': get_mid_attack,
        'hard': get_hard_attack,
    }

    for _ in range(5):
        input_attack = input('Введи тип атаки (lite, mid, hard): ').strip().lower()
        while input_attack not in attacks_types:
            print('Неизвестная атака. Выбери lite, mid или hard.')
            input_attack = input('Введи тип атаки (lite, mid, hard): ').strip().lower()
        attack_value = attacks_types[input_attack]()
        print(f'Количество очков твоей атаки: {attack_value}.')
        total += attack_value
    return total


def run_game():
    enemy_health = set_enemy_health()
    print(f'Очки здоровья противника: {enemy_health}.')
    user_total_attack = get_user_attack()
    print(f'Тобой нанесён урон противнику равный {user_total_attack}.')
    print(f'Очки здоровья противника до твоей атаки: {enemy_health}.')
    if compare_values(enemy_health, user_total_attack):
        print('Ура! Победа за тобой!')
    else:
        print('В этот раз не повезло :( Бой проигран.')
    yes_no = {
        'y': True,
        'n': False,
    }
    replay = input('Чтобы сыграть ещё раз, введи "y"; '
                   'если не хочешь продолжать игру, введи "n": ').strip().lower()
    while replay not in yes_no:
        print('Неизвестная команда. Введи y или n.')
        replay = input('Сыграть ещё раз? (y/n): ').strip().lower()
    return yes_no[replay]
