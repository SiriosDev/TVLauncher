#!/usr/bin/env python3
"""Generate the release manifest for the TVLauncher IPK."""

import hashlib
import io
import json
import sys
import tarfile
from pathlib import Path


def read_data_archive(ipk_path: Path) -> bytes:
    """Read data.tar.gz from the Debian ar archive used by an IPK."""
    with ipk_path.open("rb") as ipk:
        if ipk.read(8) != b"!<arch>\n":
            raise ValueError(f"Invalid IPK archive: {ipk_path}")

        while header := ipk.read(60):
            if len(header) != 60 or header[58:60] != b"`\n":
                raise ValueError(f"Invalid ar member header in: {ipk_path}")

            name = header[:16].decode("ascii").strip().rstrip("/")
            size = int(header[48:58].decode("ascii").strip())
            member = ipk.read(size)
            if len(member) != size:
                raise ValueError(f"Truncated ar member: {name}")
            if size % 2:
                ipk.seek(1, 1)
            if name == "data.tar.gz":
                return member

    raise ValueError(f"data.tar.gz not found in IPK: {ipk_path}")


def calculate_installed_size(ipk_path: Path) -> int:
    """Return the uncompressed byte size of regular files in data.tar.gz."""
    data_archive = read_data_archive(ipk_path)
    with tarfile.open(fileobj=io.BytesIO(data_archive), mode="r:gz") as archive:
        return sum(
            member.size for member in archive.getmembers() if member.isfile()
        )


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: generate-manifest.py <ipk> <manifest>")

    ipk_path = Path(sys.argv[1])
    manifest_path = Path(sys.argv[2])
    appinfo_path = Path("src/appinfo.json")

    if not ipk_path.is_file():
        raise SystemExit(f"IPK not found: {ipk_path}")
    if not appinfo_path.is_file():
        raise SystemExit(f"App info not found: {appinfo_path}")

    appinfo = json.loads(appinfo_path.read_text(encoding="utf-8"))
    package_size = ipk_path.stat().st_size
    package_hash = hashlib.sha256(ipk_path.read_bytes()).hexdigest()
    size_kib = max(1, (package_size + 1023) // 1024)
    installed_size = calculate_installed_size(ipk_path)

    manifest = {
        "id": appinfo["id"],
        "version": appinfo["version"],
        "type": "native",
        "title": appinfo["title"],
        "appDescription": (
            "A simple, minimalist LG webOS TV app launcher for custom launchers "
            "lacking system app support or requiring alternative layout organization."
        ),
        "iconUri": (
            "https://raw.githubusercontent.com/siriosdev/TVLauncher/main/"
            "src/largeIcon.png"
        ),
        "sourceUrl": "https://github.com/siriosdev/TVLauncher",
        "rootRequired": False,
        "ipkUrl": ipk_path.name,
        "ipkHash": {"sha256": package_hash},
        "ipkSize": size_kib,
        "installedSize": installed_size,
    }

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
