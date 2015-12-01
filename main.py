#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#
#  Copyright 2015 Arjun <Arjun@SNSD>
#

import List
import collections

#   Shift
#       Correctly Implemented Sort
#           (a-n, 0-z) -> (0-z, a-n)
#       Improperly Implemented Sort
#           (a-n, 0-z) -> (0-z, a-n)
#   ZeroIndex
#       Index+1 Correctly Implemented Sort
#           (0, a-z)
#       Index+1 Incorrectly Implemented Sort
#           (0, a-z)
#   Swap
#       Correctly Implemented Sort, swap 0
#           (a-z) -> (0, a-z)
#       Incorrectly Implemented Sort, swap 0
#           (a-z) -> (0, a-z)

def run(list, times):
    fileshg = open('ShiftGood-'+str(len(list))+'-'+str(times)+'.txt', 'w')
    fileshb = open('ShiftBad-'+str(len(list))+'-'+str(times)+'.txt', 'w')
    filezig = open('ZeroIndexGood-'+str(len(list))+'-'+str(times)+'.txt', 'w')
    filezib = open('ZeroIndexBad-'+str(len(list))+'-'+str(times)+'.txt', 'w' )
    fileswg = open('SwapGood-'+str(len(list))+'-'+str(times)+'.txt', 'w')
    fileswb = open('SwapBad-'+str(len(list))+'-'+str(times)+'.txt', 'w')
    for x in range (0, times):
        goodList = List.GoodShuffle(list[:])
        badList = List.BadShuffle(list[:])

        goodShiftedList = shiftList(goodList[:])
        fileshg.write(diffBetween(goodShiftedList))
        fileshg.write("\n")

        badShiftedList = shiftList(badList[:])
        fileshb.write(diffBetween(badShiftedList))
        fileshb.write("\n")

        goodSwappedList = swapZero(goodList[:])
        fileswg.write(diffBetween(goodSwappedList))
        fileswg.write("\n")

        badSwappedList = swapZero(badList[:])
        fileswb.write(diffBetween(badSwappedList))
        fileswb.write("\n")

        zeroIndexGood = list[:1] + List.GoodShuffle(list[1:])
        filezig.write(diffBetween(zeroIndexGood))
        filezig.write("\n")

        zeroIndexBad = list[:1] + List.BadShuffle(list[1:])
        filezib.write(diffBetween(zeroIndexBad))
        filezib.write("\n")

def diffBetween(list):
    return str(list.index(1))

def shiftList(list):
    return list[list.index(0):] + list[:list.index(0)]

def swapZero(list):
    zero = list.index(0)
    list[zero], list[0] = list[0], list[zero]
    return list

def main():
    run(List.create(25), 100000)
main()
