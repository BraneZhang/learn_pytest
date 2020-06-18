#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture()
def login():
    print("输入账号，密码先登录")


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )


@pytest.fixture
def cmdopt(request):
    # 获取pytest_addoption中的值
    return request.config.getoption("--cmdopt")
