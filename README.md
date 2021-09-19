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
   settings/create_env.py`.

### Running
 * Run the data scraper using `poetry run python collect.py` from the root of
   the project.

### Creating a service
 1. Add a `#!` to the top of `collect.py`, pointing towards the Poetry Python
    environment. This may be something like
    `#!/home/yourname/.cache/pypoetry/virtualenvs/esp32-weather-station-data-collector-RK_KB3Mo-py3.8/bin/python`.
 1. Create a file called
    `/etc/systemd/system/weather-station-api-data-collector.service`. Add this
    code and adjust as needed:
    ```
    [Unit]
    Description=Weather station API data collector

    [Service]
    ExecStart=/home/yourname/projects/weather-station-api-data-collector/collect.py

    [Install]
    WantedBy=multi-user.target
    ```

 * Start: `sudo systemctl start weather-station-api-data-collector`.
 * Check status: `sudo systemctl status weather-station-api-data-collector`.
 * Run on startup: `sudo systemctl enable weather-station-api-data-collector`.
