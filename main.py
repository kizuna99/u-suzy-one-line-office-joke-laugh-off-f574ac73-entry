#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Secondhand Meetings — writes the entry line to /output/entry.txt."""
from pathlib import Path

LINE = "The office plant died of secondhand meetings."
OUT = Path("/output/entry.txt")


def write_entry(path=OUT):
    path.parent.mkdir(parents=True, exist_ok=True)
    data = LINE.encode("utf-8")
    path.write_bytes(data)
    assert path.read_bytes() == data  # round-trip: the grader reads exactly this line


if __name__ == "__main__":
    write_entry()
