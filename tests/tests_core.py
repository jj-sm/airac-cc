import pytest
from datetime import datetime, timedelta, timezone
from src.airac_tools import cycle as core


def test_valid_cycle():
    assert core.is_valid_cycle('2301')
    assert not core.is_valid_cycle('2314')
    assert not core.is_valid_cycle('23AB')


def test_get_current_cycle():
    # 2023-08-10 is AIRAC 2308 (approx, adjust if needed)
    dt = datetime(2023, 8, 10, tzinfo=timezone.utc)
    assert core.get_current_cycle(dt).startswith('23')


def test_cycle_conversion():
    assert core.date_to_cycle(datetime(2024, 1, 25, tzinfo=timezone.utc)) == '2401'
    assert core.cycle_to_date('2401').year == 2024


def test_offset_and_format():
    assert core.cycle_offset('2301', 1) == '2302'
    assert core.cycle_offset('2301', -1) == '2213'
    assert core.format_cycle('2302') == 'AIRAC 23/02'


def test_list_cycles():
    cycles = core.list_cycles(2023)
    assert cycles[0] == '2301'
    assert cycles[-1] == '2313'
    assert len(cycles) == 13


def test_is_date_in_cycle():
    start = core.get_cycle_start_date('2302')
    end = core.get_cycle_end_date('2302')
    assert core.is_date_in_cycle(start, '2302')
    assert core.is_date_in_cycle(end, '2302')
    assert not core.is_date_in_cycle(start - timedelta(days=1), '2302')
