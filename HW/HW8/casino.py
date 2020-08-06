import random
import json


def take_combination():
    with open('comb.json', 'r') as file:
        my_comb = json.load(file)
    return my_comb


count_points = 0
player = "1"
if __name__ == "__main__":
    while player == "1":
        player = input("Нажмите 1, чтобы играть или другой символ чтобы престать играть")
        random_keys = random.choice(list(take_combination().items()))
        print(random_keys)
        count_points += random_keys[1]
        print(f"Количество очков - {count_points}")
print(f"В общем вы набрали {count_points} очков")
