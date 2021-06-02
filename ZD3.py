#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def mltpl():
    a = 1
    inp = 1
    while inp != 0:
        a *= inp
        inp = int(input())
    print(a)

if __name__ == '__main__':
    mltpl()