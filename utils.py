import datetime


def inverse_dict(dictionary):
    return {v: k for k, v in dictionary.items()}


def can_convert_to_int(value) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False


def can_convert_to_datetime(year: int, week: int) -> bool:
    try:
        datetime.date.fromisocalendar(year, week, 1)
        return True
    except ValueError:
        return False


def floor_subset(number, subset):
    subset = sorted(subset)
    for value in reversed(subset):
        if number >= value:
            return value
    return subset[0] if subset else None


def ceil_subset(number, subset):
    subset = sorted(subset)
    for value in subset:
        if number <= value:
            return value
    return subset[-1] if subset else None
