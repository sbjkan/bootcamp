def mean(values):
    """Compute the mean of a sequence of numbers."""
    return sum(values) / len(values)

def median(values):
    """Return median of sequence of numbers."""
    sorted_values = sorted(values)
    return sorted_values[len(values//2)]
