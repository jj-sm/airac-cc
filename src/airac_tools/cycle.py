from datetime import datetime, timedelta, timezone
import re

_AIRAC_START_2000 = datetime(2000, 1, 27, tzinfo=timezone.utc)


def get_first_airac_of_year(year: int) -> datetime:
    """
    Return the first AIRAC cycle start date for the provided year.
    ICAO AIRAC cycles are defined as every 28 days from Jan 28, 1999.
    """
    base = datetime(1999, 1, 28, tzinfo=timezone.utc)
    d = datetime(year, 1, 1, tzinfo=timezone.utc)

    delta_days = (d - base).days
    cycles_since_base = (delta_days + 27) // 28
    first_cycle = base + timedelta(days=cycles_since_base * 28)
    return first_cycle


def _cycle_date_from_number(year: int, cycle: int) -> datetime:
    # Returns the start date of the given AIRAC cycle in a given year
    base = get_first_airac_of_year(year)
    return base + timedelta(days=(cycle - 1) * 28)


def _cycle_number_from_date(date: datetime) -> tuple[int, int]:
    if date.tzinfo is None:
        raise ValueError("date must be timezone-aware (use UTC)")
    year = date.year
    first_cycle_start = get_first_airac_of_year(year)
    if date < first_cycle_start:
        # Belongs to previous year's last cycles
        year -= 1
        first_cycle_start = get_first_airac_of_year(year)
    delta = (date - first_cycle_start).days
    cycle = (delta // 28) + 1
    if cycle < 1:
        cycle = 1
    elif cycle > 13:
        cycle = 13
    return (year, cycle)


def get_current_cycle(date: datetime = None) -> str:
    date = date or datetime.now(timezone.utc)
    year, cycle = _cycle_number_from_date(date)
    return f"{str(year)[2:]}{cycle:02d}"


def get_next_cycle(date: datetime = None) -> str:
    date = date or datetime.now(timezone.utc)
    year, cycle = _cycle_number_from_date(date)
    if cycle == 13:
        year += 1
        cycle = 1
    else:
        cycle += 1
    return f"{str(year)[2:]}{cycle:02d}"


def get_previous_cycle(date: datetime = None) -> str:
    date = date or datetime.now(timezone.utc)
    year, cycle = _cycle_number_from_date(date)
    if cycle == 1:
        year -= 1
        cycle = 13
    else:
        cycle -= 1
    return f"{str(year)[2:]}{cycle:02d}"


def get_cycle_start_date(cycle: str) -> datetime:
    if not is_valid_cycle(cycle):
        raise ValueError("Invalid cycle string")
    year = int("20" + cycle[:2])
    cycle_num = int(cycle[2:])
    return _cycle_date_from_number(year, cycle_num)


def get_cycle_end_date(cycle: str) -> datetime:
    return get_cycle_start_date(cycle) + timedelta(days=27, hours=23, minutes=59, seconds=59)


def date_to_cycle(date: datetime) -> str:
    if date.tzinfo is None:
        raise ValueError("date must be timezone-aware (use UTC)")
    return get_current_cycle(date)


def cycle_to_date(cycle: str) -> datetime:
    return get_cycle_start_date(cycle)


def is_valid_cycle(cycle: str) -> bool:
    return re.fullmatch(r"\d{4}", cycle) and 1 <= int(cycle[2:]) <= 13


def is_date_in_cycle(date: datetime, cycle: str) -> bool:
    if date.tzinfo is None:
        raise ValueError("date must be timezone-aware (use UTC)")
    start = get_cycle_start_date(cycle)
    end = start + timedelta(days=27, hours=23, minutes=59, seconds=59)
    return start <= date <= end


def list_cycles(year: int) -> list[str]:
    return [f"{str(year)[2:]}{i:02d}" for i in range(1, 14)]


def cycles_between(start_cycle: str, end_cycle: str) -> list[str]:
    if not (is_valid_cycle(start_cycle) and is_valid_cycle(end_cycle)):
        raise ValueError("Invalid cycle(s)")
    cycles = []
    s_year, s_num = int("20" + start_cycle[:2]), int(start_cycle[2:])
    e_year, e_num = int("20" + end_cycle[:2]), int(end_cycle[2:])
    while (s_year, s_num) <= (e_year, e_num):
        cycles.append(f"{str(s_year)[2:]}{s_num:02d}")
        if s_num == 13:
            s_year += 1
            s_num = 1
        else:
            s_num += 1
    return cycles


def dates_between(start_cycle: str, end_cycle: str) -> list[datetime]:
    return [get_cycle_start_date(c) for c in cycles_between(start_cycle, end_cycle)]


def cycle_offset(cycle: str, offset: int) -> str:
    if not is_valid_cycle(cycle):
        raise ValueError("Invalid cycle")
    year = int("20" + cycle[:2])
    num = int(cycle[2:])
    total = (year - 2000) * 13 + (num - 1) + offset
    if total < 0:
        raise ValueError("Resulting cycle before AIRAC epoch.")
    new_year = 2000 + (total // 13)
    new_num = (total % 13) + 1
    return f"{str(new_year)[2:]}{new_num:02d}"


def format_cycle(cycle: str) -> str:
    from .utils import format_cycle
    return format_cycle(cycle)