import pytest
from datetime import datetime, timezone, timedelta
from airac_tools import cycle as core

def _dt(y, m, d):
    return datetime(y, m, d, tzinfo=timezone.utc)

@pytest.mark.parametrize("cycle, expected", [
    ("2601", _dt(2026, 1, 22)),
    ("2602", _dt(2026, 2, 19)),
    ("2603", _dt(2026, 3, 19)),
    ("2604", _dt(2026, 4, 16)),
    ("2605", _dt(2026, 5, 14)),
    ("2606", _dt(2026, 6, 11)),
    ("2607", _dt(2026, 7, 9)),
    ("2608", _dt(2026, 8, 6)),
    ("2609", _dt(2026, 9, 3)),
    ("2610", _dt(2026, 10, 1)),
    ("2611", _dt(2026, 10, 29)),
    ("2612", _dt(2026, 11, 26)),
    ("2613", _dt(2026, 12, 24)),
    ("2701", _dt(2027, 1, 21)),
    ("2702", _dt(2027, 2, 18)),
    ("2703", _dt(2027, 3, 18)),
    ("2704", _dt(2027, 4, 15)),
    ("2705", _dt(2027, 5, 13)),
    ("2706", _dt(2027, 6, 10)),
    ("2707", _dt(2027, 7, 8)),
    ("2708", _dt(2027, 8, 5)),
    ("2709", _dt(2027, 9, 2)),
    ("2710", _dt(2027, 9, 30)),
    ("2711", _dt(2027, 10, 28)),
    ("2712", _dt(2027, 11, 25)),
    ("2713", _dt(2027, 12, 23)),
    ("2801", _dt(2028, 1, 20)),
    ("2802", _dt(2028, 2, 17)),
    ("2803", _dt(2028, 3, 16)),
    ("2804", _dt(2028, 4, 13)),
    ("2805", _dt(2028, 5, 11)),
    ("2806", _dt(2028, 6, 8)),
    ("2807", _dt(2028, 7, 6)),
    ("2808", _dt(2028, 8, 3)),
    ("2809", _dt(2028, 8, 31)),
    ("2810", _dt(2028, 9, 28)),
    ("2811", _dt(2028, 10, 26)),
    ("2812", _dt(2028, 11, 23)),
    ("2813", _dt(2028, 12, 21)),
    ("3013", _dt(2030, 12, 19)),
])
def test_cycle_start_dates_extended(cycle, expected):
    assert core.get_cycle_start_date(cycle) == expected

@pytest.mark.parametrize("date, expected_cycle", [
    (_dt(2026, 1, 22), "2601"),
    (_dt(2026, 2, 18), "2601"),
    (_dt(2026, 2, 19), "2602"),
    (_dt(2026, 3, 18), "2602"),
    (_dt(2026, 3, 19), "2603"),
    (_dt(2026, 4, 15), "2603"),
    (_dt(2026, 4, 16), "2604"),
    (_dt(2026, 12, 24), "2613"),
    (_dt(2027, 1, 21), "2701"),
    (_dt(2028, 12, 21), "2813"),
])
def test_date_to_cycle_extended(date, expected_cycle):
    assert core.date_to_cycle(date) == expected_cycle

def test_cycle_end_date():
    # Check that end date is 27 days, 23:59:59 after start
    c = "2601"
    start = core.get_cycle_start_date(c)
    end = core.get_cycle_end_date(c)
    assert (end - start).days == 27
    assert (end - start).seconds == 86399

def test_is_valid_cycle():
    assert core.is_valid_cycle("2601")
    assert not core.is_valid_cycle("2614")
    assert not core.is_valid_cycle("26A1")
    assert not core.is_valid_cycle("260")
    assert not core.is_valid_cycle("26001")

def test_is_date_in_cycle():
    c = "2601"
    start = core.get_cycle_start_date(c)
    end = core.get_cycle_end_date(c)
    assert core.is_date_in_cycle(start, c)
    assert core.is_date_in_cycle(end, c)
    assert not core.is_date_in_cycle(start - timedelta(days=1), c)
    assert not core.is_date_in_cycle(end + timedelta(seconds=1), c)

def test_cycle_offset():
    assert core.cycle_offset("2601", 1) == "2602"
    assert core.cycle_offset("2601", 12) == "2613"
    assert core.cycle_offset("2601", 13) == "2701"
    assert core.cycle_offset("2601", -1) == "2513"
    assert core.cycle_offset("2601", 0) == "2601"

def test_list_cycles():
    cycles = core.list_cycles(2026)
    assert cycles[0] == "2601"
    assert cycles[-1] == "2613"
    assert len(cycles) == 13

def test_cycles_between():
    cycles = core.cycles_between("2601", "2603")
    assert cycles == ["2601", "2602", "2603"]
    cycles = core.cycles_between("2612", "2702")
    assert cycles[0] == "2612"
    assert cycles[-1] == "2702"
    assert len(cycles) == 4

def test_dates_between():
    dates = core.dates_between("2601", "2603")
    assert dates[0] == core.get_cycle_start_date("2601")
    assert dates[-1] == core.get_cycle_start_date("2603")
    assert len(dates) == 3

