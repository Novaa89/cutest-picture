"""cutest-picture-01 entry: copy the picture beside this file to /output/entry.png.

The picture is entry.png in this repository. The grader runs this program in a
fresh container with no network, a read-only repository and a writable /output.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
# An empty MAKEFUN_OUTPUT_DIR means the same as unset: fall back to /output.
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.png"))
