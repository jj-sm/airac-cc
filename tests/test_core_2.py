import pytest
from datetime import datetime, timezone
from airac_tools import cycle as core

@pytest.mark.parametrize("cycle, expected", [
    # 2024
    ('2401', datetime(2024, 1, 25, tzinfo=timezone.utc)),
    ('2402', datetime(2024, 2, 22, tzinfo=timezone.utc)),
    ('2403', datetime(2024, 3, 21, tzinfo=timezone.utc)),
    ('2404', datetime(2024, 4, 18, tzinfo=timezone.utc)),
    ('2405', datetime(2024, 5, 16, tzinfo=timezone.utc)),
    ('2406', datetime(2024, 6, 13, tzinfo=timezone.utc)),
    ('2407', datetime(2024, 7, 11, tzinfo=timezone.utc)),
    ('2408', datetime(2024, 8, 8, tzinfo=timezone.utc)),
    ('2409', datetime(2024, 9, 5, tzinfo=timezone.utc)),
    ('2410', datetime(2024, 10, 3, tzinfo=timezone.utc)),
    ('2411', datetime(2024, 10, 31, tzinfo=timezone.utc)),
    ('2412', datetime(2024, 11, 28, tzinfo=timezone.utc)),
    ('2413', datetime(2024, 12, 26, tzinfo=timezone.utc)),
    # 2025
    ('2501', datetime(2025, 1, 23, tzinfo=timezone.utc)),
    ('2502', datetime(2025, 2, 20, tzinfo=timezone.utc)),
    ('2503', datetime(2025, 3, 20, tzinfo=timezone.utc)),
    ('2504', datetime(2025, 4, 17, tzinfo=timezone.utc)),
    ('2505', datetime(2025, 5, 15, tzinfo=timezone.utc)),
    ('2506', datetime(2025, 6, 12, tzinfo=timezone.utc)),
    ('2507', datetime(2025, 7, 10, tzinfo=timezone.utc)),
    ('2508', datetime(2025, 8, 7, tzinfo=timezone.utc)),
    ('2509', datetime(2025, 9, 4, tzinfo=timezone.utc)),
    ('2510', datetime(2025, 10, 2, tzinfo=timezone.utc)),
    ('2511', datetime(2025, 10, 30, tzinfo=timezone.utc)),
    ('2512', datetime(2025, 11, 27, tzinfo=timezone.utc)),
    ('2513', datetime(2025, 12, 25, tzinfo=timezone.utc)),
])
def test_cycle_start_dates(cycle, expected):
    assert core.get_cycle_start_date(cycle) == expected

@pytest.mark.parametrize("date, expected_cycle", [
    (datetime(2024, 1, 25, tzinfo=timezone.utc), '2401'),
    (datetime(2024, 2, 21, tzinfo=timezone.utc), '2401'),  # day before next cycle
    (datetime(2024, 2, 22, tzinfo=timezone.utc), '2402'),
    (datetime(2024, 3, 20, tzinfo=timezone.utc), '2402'),
    (datetime(2024, 3, 21, tzinfo=timezone.utc), '2403'),
])
def test_date_to_cycle(date, expected_cycle):
    assert core.date_to_cycle(date) == expected_cycle