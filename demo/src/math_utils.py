def clamp(value, minimum, maximum):
    if minimum > maximum:
        raise ValueError("minimum cannot be greater than maximum")
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value
