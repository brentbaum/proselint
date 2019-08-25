"""Tests for legal.shall check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.legal import shall as chk


class TestCheck(Check):
    """The test class for legal.shall."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for legal.shall."""
        assert self.passes("""You will not pass.""")
        assert not self.passes("""You shall not pass.""")
