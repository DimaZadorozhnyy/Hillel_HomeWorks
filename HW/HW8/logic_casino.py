from itertools import product
import json


all_comb_list = []
for i in product("ABCDEFGHIX", repeat=3):
    combination_options = ''.join(i)
    all_comb_list.append(combination_options)
all_comb_dict = {}
all_comb_dict = all_comb_dict.fromkeys(all_comb_list)
with open("asd.json", 'w') as file:
    json.dump(all_comb_dict, file, indent=4)


