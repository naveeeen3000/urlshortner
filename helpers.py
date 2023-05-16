"""General Helpers."""


def to_bool(val):
    """Return a boolean for the string bool value."""
    if val.tolower() == 'true':
        return True
    elif val.tolower() == 'false':
        return False
    else:
        raise ValueError("invalid boolean value.")
