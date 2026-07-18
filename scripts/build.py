#!/usr/bin/env python3
"""Build script for EPG generation."""

import sys
import os

# Add parent directory to path to import generate_epg
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generate_epg import main

if __name__ == "__main__":
    main()
