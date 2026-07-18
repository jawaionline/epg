import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CHANNELS = ROOT / "config" / "channels.xml"

OUTPUT = ROOT / "output"

EPG = ROOT / "iptv-org"


def run(cmd, cwd=None):
    print(f"\n>>> {' '.join(cmd)}")
    subprocess.check_call(cmd, cwd=cwd)


print("=" * 50)
print("EPG Builder")
print("=" * 50)

#
# Clone IPTV-Org jika belum ada
#

if not EPG.exists():

    run([
        "git",
        "clone",
        "--depth",
        "1",
        "https://github.com/iptv-org/epg.git",
        str(EPG)
    ])

#
# Install
#

run(["npm", "install"], cwd=EPG)

#
# Copy channels.xml
#

shutil.copy(
    CHANNELS,
    EPG / "channels.xml"
)

#
# Jalankan grabber
#

run([
    "npm",
    "run",
    "grab",
    "--",
    "--channels=channels.xml",
    "--output=guide.xml"
], cwd=EPG)

#
# Output
#

OUTPUT.mkdir(exist_ok=True)

shutil.copy(
    EPG / "guide.xml",
    OUTPUT / "epg.xml"
)

print()

print("DONE")

print()

print("Output :", OUTPUT / "epg.xml")