"""
Unit and regression test for the science_tools_test package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import science_tools_test


def test_science_tools_test_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "science_tools_test" in sys.modules
