#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest

'''
** 作者：上海-悠悠 QQ交流群：588402570**
'''


@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页")


def test_s1():
    print("用例1：搜索python-1")


def test_s2(open):
    print("用例2：搜索python-2")


def test_s3():
    print("用例3：搜索python-3")


if __name__ == "__main__":
    pytest.main(["-s", "test_fix03.py"])
    # pytest.main(["-q", "test_fix03.py"])
