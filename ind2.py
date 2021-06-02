#!/usr/bin/env python3
# -*- coding: utf-8 -*

import json


def xz():
    with open('he1', 'r') as f:
        text = json.load(f)
        sentences = text.split(".")

    for sentence in sentences:
        if word in sentence:
            print(sentence)
            with open('he2', 'w') as f:
                json.dump(sentence, f)

if __name__ == '__main__':
    word = input("Введите слово:")
    xz()