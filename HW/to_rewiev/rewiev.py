import random


def who_win(num_1, num_2):
    if num_1 > num_2:
        return f'сумма бросков первого играка {num_1}, а второго {num_2}, первый игрок победил'
    elif num_2 > num_1:
        return f'сумма бросков первого играка {num_1}, а второго {num_2}, второй игрок победил'
    else:
        return f'сумма бросков первого играка {num_1}, а второго {num_2}, ничья))'


sum_1 = 0
sum_2 = 0
attempts = 10

if __name__ == "__main__":
    while attempts != 0:
        for i in range(attempts):
            player_1 = input('Что-бы бросить кубики нажмите "1"\n')
            player_2 = input('Что-бы бросить кубики нажмите "1"\n')
            if player_2 != '1' or player_1 != '1':
                attempts = 0
                print("Кто-то отказался бросать кубики\n", who_win(sum_1, sum_2))
                break

            random_number_1 = random.randint(2, 12)
            print(f'Первому игроку выпало {random_number_1}')
            random_number_2 = random.randint(2, 12)
            print(f'Второму игроку выпало {random_number_2}')
            sum_1 += random_number_1
            sum_2 += random_number_2
            attempts -= 1
            print(f'У вас {attempts} попыток!\n')
            if attempts == 0:
                print(who_win(sum_1, sum_2))
            if random_number_1 == random_number_2:
                attempts += 1
                print('Ничья, перебрасываем!!!!\n')
                break
