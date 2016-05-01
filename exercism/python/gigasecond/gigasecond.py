from datetime import timedelta


def add_gigasecond(dt):
    return dt + timedelta(seconds=1e9)
