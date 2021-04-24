def mean(values):
    return sum(values) / len(values)

def median(values):
    n = len(values)
    sorted_values = sorted(values)
    if n % 2 == 0:
        return (sorted_values[(n / 2) - 1] + sorted_values[n / 2]) / 2
    else:
        return sorted_values[n / 2]