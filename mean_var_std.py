import numpy as np
from matplotlib.cbook import flatten

inputA = [1,2,3,4,5,6,7,8,9]

def calculate(a):
    converted_list = np.reshape(a, (3,3))
    myDict = {
        'mean': [np.mean(converted_list, axis=0), np.mean(converted_list, axis=1), np.mean(converted_list.flatten())],
        'variance': [np.var(converted_list, axis=0), np.var(converted_list, axis=1), np.var(converted_list.flatten())],
        'standard deviation': [np.std(converted_list, axis=0), np.std(converted_list, axis=1), np.std(converted_list.flatten())],
        'max': [np.max(converted_list, axis=0), np.max(converted_list, axis=1), np.max(converted_list.flatten())],
        'min': [np.min(converted_list, axis=0), np.min(converted_list, axis=1), np.min(converted_list.flatten())],
        'sum': [np.sum(converted_list, axis=0), np.sum(converted_list, axis=1), np.sum(converted_list.flatten())]
    }
    return myDict

calculate(inputA)