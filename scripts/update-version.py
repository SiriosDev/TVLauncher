#!/usr/bin/env python3
"""Update the application version in src/appinfo.json."""

import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2 or not sys.argv[1]:
        raise SystemExit("usage: update-version.py <version>")

    appinfo_path = Path("src/appinfo.json")
    if not appinfo_path.is_file():
        raise SystemExit(f"App info not found: {appinfo_path}")

    appinfo = json.loads(appinfo_path.read_text(encoding="utf-8"))
    appinfo["version"] = sys.argv[1]
    appinfo_path.write_text(
        json.dumps(appinfo, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
