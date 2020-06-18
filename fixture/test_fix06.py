#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest


def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")
    assert 0  # to see what was printed


if __name__ == "__main__":
    pytest.main(["-s", "test_fix06.py"])
