#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest


# 函数式(不在类中的用例)


def setup_function():
    print("setup_function：每个用例开始前都会执行")


def teardown_function():
    print("teardown_function：每个用例结束后都会执行")


def test_one():
    print("正在执行----test_one")
    x = "this"
    assert 'h' in x


def test_two():
    print("正在执行----test_two")
    x = "hello"
    assert hasattr(x, 'check')


def test_three():
    print("正在执行----test_three")
    a = "hello"
    b = "hello world"
    assert a in b


if __name__ == "__main__":
    # -s 参数是为了显示用例的打印信息. -q 参数只显示结果，不显示过程
    # pytest.main()
    pytest.main(["-s", "test_function.py"])
    # pytest.main(["-s", '-q', "test_function.py"])
