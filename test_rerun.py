#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest


class TestRerun():

    def reverse(self, string):
        return string[::-1]

    def test_reverse(self):
        string = "good"
        assert self.reverse(string) == "doog"

        another_string = "itest"
        assert self.reverse(another_string) == "tsetii"

    def test_equal(self):
        assert 2 == 2
