import random


def generate_ub_data(start=1500, end=800, steps=10):
    """Generate a list of decreasing values with a few abrupt drops."""
    values = [start]
    current = start
    for i in range(1, steps):
        # Add a big drop 2–3 times
        if i in random.sample(range(1, steps - 1), 3):
            drop = random.randint(80, 200)
        else:
            drop = random.randint(5, 30)
        current = max(end, current - drop)
        values.append(current)
    return values
