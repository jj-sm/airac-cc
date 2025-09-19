# airac-tools

**airac-tools** is a Python package for working with ICAO AIRAC (Aeronautical Information Regulation And Control) cycles.  
It provides a variety of utilities to determine cycle dates, validate cycle strings, perform conversions, iterate over cycles, and more.

---

## Features

- **Cycle Information Functions**
  - `get_current_cycle(date: datetime = None) -> str`: Get the current AIRAC cycle for a given date.
  - `get_next_cycle(date: datetime = None) -> str`: Get the next AIRAC cycle after a given date.
  - `get_previous_cycle(date: datetime = None) -> str`: Get the previous AIRAC cycle.
  - `get_cycle_start_date(cycle: str) -> datetime`: Get the start date of a given AIRAC cycle.
  - `get_cycle_end_date(cycle: str) -> datetime`: Get the end date of a given AIRAC cycle.

- **Date Conversion Functions**
  - `date_to_cycle(date: datetime) -> str`: Convert any date to its corresponding AIRAC cycle.
  - `cycle_to_date(cycle: str) -> datetime`: Convert an AIRAC cycle to its start date.

- **Validation Functions**
  - `is_valid_cycle(cycle: str) -> bool`: Check if a given cycle string (like `'2309'`) is valid.
  - `is_date_in_cycle(date: datetime, cycle: str) -> bool`: Check if a date falls within a specific cycle.

- **Listing/Iteration Functions**
  - `list_cycles(year: int) -> list[str]`: List all AIRAC cycles for a given year.
  - `cycles_between(start_cycle: str, end_cycle: str) -> list[str]`: List all cycles between two cycles.
  - `dates_between(start_cycle: str, end_cycle: str) -> list[datetime]`: List start dates for each cycle in a range.

- **Utility Functions**
  - `cycle_offset(cycle: str, offset: int) -> str`: Returns the cycle offset by N cycles.
  - `format_cycle(cycle: str) -> str`: Returns a human-readable cycle string.

---

## Installation

Install from PyPI (when published):

```bash
pip install airac-tools
```

Or install locally (for development):

```bash
git clone https://github.com/jj-sm/airac-tools.git
cd airac-tools
pip install .
```

---

## Usage

```python
from airac_tools import cycle

# Get current AIRAC cycle
current_cycle = cycle.get_current_cycle()
print(cycle)  # e.g., '2308'

# List all cycles in 2025
cycles_2025 = cycle.list_cycles(2025)
print(cycles_2025)  # ['2501', ..., '2513']

# Convert date to cycle
from datetime import datetime, timezone
cycle_2 = cycle.date_to_cycle(datetime(2024, 8, 10, tzinfo=timezone.utc))
print(cycle)  # e.g., '2408'

# Get cycle start/end dates
start = cycle.get_cycle_start_date('2408')
end = cycle.get_cycle_end_date('2408')
print(start, end)

# Check if date is within a cycle
cycle.is_date_in_cycle(datetime(2024, 8, 10, tzinfo=timezone.utc), '2408')  # True

# Cycle offset
cycle.cycle_offset('2408', 2)  # '2410'

# Format cycle
from airac_tools import utils
print(utils.format_cycle('2408'))  # 'AIRAC 24/08'
```

---

## Development

- Clone the repository and install in editable mode:
  ```bash
  pip install -e .
  ```
- Run tests with:
  ```bash
  pytest
  ```
- Code is formatted with [PEP8](https://pep8.org/).
- Contributions and issues are welcome!

[//]: # (---)

[//]: # ()
[//]: # (## Continuous Integration and Publishing)

[//]: # ()
[//]: # (- Tests are run automatically via GitHub Actions on every push and pull request.)

[//]: # (- Publishing to PyPI is automated on release tags &#40;see `.github/workflows/publish.yml`&#41;.)

[//]: # (- To publish, make sure your PyPI credentials are set as repository secrets &#40;`PYPI_USERNAME`, `PYPI_PASSWORD`&#41;, then push a tag:  )

[//]: # (  ```bash)

[//]: # (  git tag v0.1.0)

[//]: # (  git push --tags)

[//]: # (  ```)

---

## License

MIT License.

---

## Acknowledgements

AIRAC cycle rules are based on ICAO documentation and public sources.
