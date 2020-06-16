#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest


@pytest.fixture()
def login():
    print("输入账号，密码先登录")
