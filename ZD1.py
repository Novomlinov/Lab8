#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def negative():
    print("Отрицательное")

def positive():
    print("Положительное")

def test():
    t = int(input())
    if t > 0:
        positive()
    else:
        negative()

if __name__ == '__main__':
    test()