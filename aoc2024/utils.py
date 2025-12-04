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


def run(fn: Callable, input_file: str, *args, expected: int | None = None, **kwargs):
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
