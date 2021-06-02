#!/usr/bin/env python3
# -*- coding: utf-8 -*-


pi = 3.141592

def circle(r):
    return r * r * pi

def cylinder(h, r):
    print("1. S.full\n2. S.partial")
    ans = int(input())
    if ans == 1:
        print(2*circle(r) + 2*r*h*pi)
    elif ans == 2:
        print(2*r*h*pi)
    else:
        print("wehfiewhfuiewhf")

if __name__ == '__main__':
    r = int(input())
    h = int(input())
    cylinder(h, r)