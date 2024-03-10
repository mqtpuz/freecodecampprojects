import numpy as np
from collections import defaultdict


def calculate(input_list):

    if len(input_list) != 9:
        raise ValueError('List must contain nine numbers.')

    input_list = np.array(input_list).reshape(3, 3)
    calculations = defaultdict(lambda: [])

    functions = [np.mean, np.var, np.std, np.max, np.min, np.sum]
    parameters = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']

    for parameter, function in zip(parameters, functions):
        for i in [0, 1]:
            calculations[parameter].append(list(function(input_list, axis=i)))

        calculations[parameter].append(function(input_list))

    calculations = dict(calculations)
    return calculations
