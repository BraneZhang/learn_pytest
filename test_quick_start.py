#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def reverse(string):
    return string[::-1]

def test_reverse():
    string = "good"
    assert reverse(string) == "doog"

    another_string = "itest"
    assert reverse(another_string) == "tsetii"
