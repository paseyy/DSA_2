# author: Jakob Freiberger - 12109786 - jakob.freiberger@student.tugraz.at

import numpy as np

def max_sub_prod(array):
    total_max = 0
    current_max = 1
    fr = 0
    to = 0
    k = 0
    for i in range(1, len(array)):
        current_max = current_max * array[i]
        if current_max > total_max:
            total_max = current_max
            fr = k
            to = i
        if current_max < 1:
            current_max = 1
            k = i+1

    return {"product": total_max, "from": fr, "to": to}


if __name__ == '__main__':
    for i in range(0, 100):
        array = np.random.uniform(low=0, high=3, size=10)
        print(array[1:10])
        max_sub = max_sub_prod(array)
        print(max_sub)