def mean(values):
    """
    finds the mean value of values
    :param values: the numbers to use for calculations
    :return: the mean
    """
    return sum(values) / len(values)


def median(values):
    """
    finds the median of values
    :param values: the numbers to use for calculations
    :return: the median
    """
    n = len(values)
    sorted_values = sorted(values)
    if n % 2 == 0:
        return (sorted_values[(n / 2) - 1] + sorted_values[n / 2]) / 2
    else:
        return sorted_values[n // 2]
