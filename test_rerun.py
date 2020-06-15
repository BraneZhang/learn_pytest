#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest


class TestRerun():

    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize('val',[
        8,10
    ])
    def test_num(self, val):
        assert val == 16
