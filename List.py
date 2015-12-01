#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#
#  Copyright 2015 Arjun <Arjun@SNSD>
#
import random

def create(size):
    list = []
    for x in range(0, size):
        list.append(x)
    return list

def GoodShuffle(list):
    for i, x in enumerate(list):
        j = random.randrange(i,len(list))
        list[i], list[j] = list[j], list[i]
    return list

def BadShuffle(list):
    for i, x in enumerate(list):
        j = random.randrange(0,len(list))
        list[i], list[j] = list[j], list[i]
    return list
