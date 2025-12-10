import inspect
import re
from json import dumps
from pathlib import Path
from typing import Callable

CMD = "\033[97m"
ARG = "\033[0m"
ANS = "\033[94m"
OK = "\033[92m"
ERR = "\033[91m"
RST = "\033[0m"

BASE_DIR = Path(__file__).parent


def get_aoc_session():
    import browser_cookie3

    for c in browser_cookie3.chrome(domain_name="adventofcode.com"):
        if c.name == "session":
            return c.value
    raise KeyError("Could not find 'session' cookie for adventofcode.com")


def download_puzzle_input():
    # Determine caller file and corresponding paths
    caller_file = Path(inspect.stack()[1].filename)
    year = int(re.search(r"\d+", caller_file.parent.name).group(0))
    day = int(re.search(r"\d+", caller_file.stem).group(0))
    file_path = caller_file.parent / "data" / f"day{day:02}-data.txt"

    # Check if data file already exists
    if file_path.exists():
        return

    # Download data from Advent of Code
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    header = {"Cookie": f"session={get_aoc_session()}", "User-Agent": "adventofcode-input-downloader"}

    print(f"{CMD}Downloading puzzle input from {ARG}{url}{RST}")

    import requests

    response = requests.get(url, headers=header)

    # Save data to file if request was successful
    if response.status_code == 200:
        file_path.parent.mkdir(exist_ok=True)
        with open(file_path, "w") as file:
            file.write(response.text)
    else:
        print(f"{ERR}Failed to download puzzle input: HTTP {response.status_code}{RST}")
        exit(1)


def run(fn: Callable, input_file: str, *args, expected: int | str | None = None, **kwargs):
    def arg(v):
        return f"{ARG}{dumps(v)}{RST}"

    input_path = BASE_DIR / input_file

    fn_str = fn.__name__
    str_args = [arg(input_path.name)]
    str_args += [arg(v) for v in args]
    str_args += [f"{CMD}{k}={arg(v)}" for k, v in kwargs.items()]
    args_str = f"{CMD}, {RST}".join(str_args)
    print(f"{CMD}{fn_str}{CMD}({args_str}{CMD}){RST}", end="")

    if not input_path.exists():
        print(f"{CMD} -> {ERR}Not found: {input_path.relative_to(BASE_DIR)}{RST}")
        exit(1)

    answer = fn(str(input_path), *args, **kwargs)
    print(f"{CMD} -> {RST}", end="")

    if expected is None:
        print(f"{ANS}{answer}{RST}")
    elif answer == expected:
        print(f"{OK}{answer}{RST}")
    else:
        print(f"{ERR}{answer}{RST} != {OK}{expected}{RST}")
        exit(1)

    return answer
