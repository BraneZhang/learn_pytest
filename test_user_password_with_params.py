#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest
import pytest_rerunfailures
import json

users = json.loads(open('./users.test.json', 'r').read())


class TestUserPasswordWithParam(object):
    @pytest.fixture(params=users)
    def user(self, request):
        return request.param

    @pytest.mark.flaky(reruns=1)
    def test_user_password(self, user):
        passwd = user['password']
        assert len(passwd) >= 6
        msg = "user %s has a weak password" % (user['name'])
        assert passwd != 'password', msg
        assert passwd != 'password123', msg


if __name__ == '__main__':
    # pytest.main(['--html=./report/report.html'])
    # pytest.main(['--reruns', '1'])
    pytest.main(['test_user_password_with_params.py', '--html=./report/report.html'])
    # pytest.main()
