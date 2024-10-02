#!/usr/bin/env python3

import io
import sys
import runpy
import pytest

class TestAppPy:
    def test_prints_hello_world(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        runpy.run_path("lib/app.py")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Hello World! Pass this test, please.\n"
