import random


def is_sorted(ls):
    for i in range(len(ls)-1):
        if ls[i] > ls[i + 1]:
            return False
    return True


def bogo_sort(ls):
    sorted_ls = list(ls)
    while(not is_sorted(sorted_ls)):
        random_indicies = []

        for i in range(len(ls)):
            random_index = random.randint(0, len(ls)-1)
            # make sure there are no duplicate values in random_indicies
            while(random_index in random_indicies):
                random_index = random.randint(0, len(ls)-1)
            random_indicies.append(random_index)

        # print(random_indicies)

        for i in range(len(ls)):
            sorted_ls[random_indicies[i]] = ls[i]

    return sorted_ls
