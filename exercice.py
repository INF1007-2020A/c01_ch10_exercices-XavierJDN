#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import math

# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(start = -1.13, stop = 2.5, num = 64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    a = np.zeros([len(cartesian_coordinates),2]) 
    for i, _ in enumerate(a):
        a[i] = (np.arctan2(cartesian_coordinates[i][1] / cartesian_coordinates[i][0]),
                (cartesian_coordinates[i][0] ** 2 + cartesian_coordinates[i][1] ** 2)** 1/2)
        print(a)
    return a

def find_closest_index(values: np.ndarray, number: float) -> int:
    return sorted([(i,values[i]) for i,el in enumerate(values)], key = lambda el: abs(number - el))[0][0]


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
    # coordinate_conversion(np.array([1,2]))
    # find_closest_index(np.array([1,3,5,8,10]), 2.2)