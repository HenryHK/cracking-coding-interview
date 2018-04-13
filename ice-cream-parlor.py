#!/usr/bin/python3


def solve(arr, money):
    map = {}
    index = 1
    for price in arr:
        if price in map:
            map[price] += [index]
        else:
            map[price] = [index]
        index += 1
    index_1 = 1
    for price in arr:
        if (money - price) in map:
            if (money-price) == price:
                if len(map[price]) > 1:
                    print(map[price][0], map[price][1])
                    return
            else:
                print(map[price][0], map[money-price][0])
                return
