#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest


@pytest.mark.flaky(reruns=1)
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("2+4", 4),
    ("6*9", 42),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

if __name__ == '__main__':
    # pytest.main(['--html=./report/report.html'])
    # pytest.main(['--reruns', '1'])
    pytest.main(['test_math_operation.py', '--html=./report/report.html'])
    # pytest.main()
