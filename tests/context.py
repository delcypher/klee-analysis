"""
Context ensures that we are using exactly this version of kleeparser for the tests
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# pylint: disable=unused-import
import kleeparser

TEST_RUNNERDIR = r"C:\Users\ghast\Desktop\out\workdir-0"
