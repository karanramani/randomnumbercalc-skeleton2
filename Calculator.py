import random
import math
from random import sample
import numpy as np
import scipy.stats as st
import statistics

def mean_main (a):
    x = statistics.mean(a)
    return x


class Calculator:
    result = 0

    def mean(a):
        result = mean_main(a)
        return result