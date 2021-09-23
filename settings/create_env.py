from pathlib import Path

ENV_DEFAULT = f"""WEATHER_STATION_API_URL=http://192.168.0.101:80
WEATHER_STATION_API_ENDPOINT=/all
CSV_SAVE_LOCATION={Path().resolve()}/data/
POLLING_TIME=30
TZ=Europe/London
"""


def create_env(env_file):
    env_file.write_text(ENV_DEFAULT)
    env_file.chmod(0o600)
    print(f"Created {env_file}")


if __name__ == "__main__":
    env_file = Path(".env")
    if env_file.exists():
        print(f"{env_file} already exists!")
    else:
        create_env(env_file)
