#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    # pytest.param("2+4", 6, marks=pytest.mark.xfail),
    pytest.param("6*9", 42, marks=pytest.mark.xfail),  # 预期失败，若运行结果为失败则未xfailed,反之则为xpassed
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


if __name__ == '__main__':
    # pytest.main(['--html=./report/report.html'])
    # pytest.main(['--reruns', '1'])
    # pytest.main(['test_math_operation.py', '--html=./report/report.html'])
    pytest.main(['-s', 'test_math_operation.py'])
