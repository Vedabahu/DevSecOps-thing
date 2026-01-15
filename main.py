import argparse
import sys
from typing import Callable
from cal import div, sub, add, multiply as mul

# Command registry: single source of truth
COMMANDS: dict[str, tuple[str, Callable[[float, float], float]]] = {
    "add": ("Add two numbers", add),
    "sub": ("Subtract two numbers", sub),
    "mul": ("Multiply two numbers", mul),
    "div": ("Divide two numbers", div),
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Simple CLI calculator")

    subparsers = parser.add_subparsers(dest="command", required=True)

    for name, (help_text, func) in COMMANDS.items():
        cmd_parser = subparsers.add_parser(name, help=help_text)
        cmd_parser.add_argument("x", type=float)
        cmd_parser.add_argument("y", type=float)
        cmd_parser.set_defaults(func=func)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        result = args.func(args.x, args.y)
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
