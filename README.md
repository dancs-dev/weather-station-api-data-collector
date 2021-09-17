# Portfolio
Python-based API data collector. Intended for use with the
[esp32-weather-station](https://github.com/dancs-dev/esp32-weather-station).

Requests data from the API at regular intervals (set in `.env`) and saves it to
a CSV file. A CSV file is created each day.


## How to use

### Installation
 * Ensure Python >= 3.8 is available for your system.
 * Install [Poetry](https://github.com/python-poetry/poetry#installation) (if
   you do not already have it installed).
 * [Install and run pre-commit](https://pre-commit.com/) if you intend to make
   commits.

### Environment and configuration
 * Create the virtual environment using `poetry install` while in the root of
   the repo directory.
 * Create a default `.env` file using `poetry run python
   /settings/create_env.py`.

### Running
 * Run the data scraper using `poetry run python collect.py` from the root of
   the project.
