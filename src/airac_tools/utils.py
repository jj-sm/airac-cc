import re


def format_cycle(cycle: str) -> str:
    """
    Returns a human-readable AIRAC cycle string, e.g. 'AIRAC 24/08' for '2408'.
    """
    if not re.fullmatch(r"\d{4}", cycle):
        raise ValueError("Invalid cycle number format")
    year = cycle[:2]
    num = cycle[2:]
    return f"AIRAC {year}/{num}"


def parse_cycle(cycle: str) -> tuple[int, int]:
    """
    Parses a cycle string into (year, cycle_number), e.g. '2408' -> (2024, 8)
    """
    if not re.fullmatch(r"\d{4}", cycle):
        raise ValueError("Invalid cycle number format")
    year = 2000 + int(cycle[:2])
    number = int(cycle[2:])
    return year, number


def is_valid_cycle_format(cycle: str) -> bool:
    """
    Checks if a cycle string is the correct 4-digit format (YYCC).
    """
    return bool(re.fullmatch(r"\d{4}", cycle))
