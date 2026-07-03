#!/usr/bin/env python3
"""Compatibility wrapper for the full Monitoring PDF index generator."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


SCRIPT = Path(__file__).with_name("generate-pdf-indexes.py")


if __name__ == "__main__":
    raise SystemExit(subprocess.call([sys.executable, str(SCRIPT), *sys.argv[1:]]))
