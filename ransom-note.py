#!/usr/bin/python3
# Idea: use hashmap


def ransom_note(magazine, ransom):
    w_dict = {}
    for word in magazine:
        if word not in w_dict:
            w_dict[word] = 1
        else:
            w_dict[word] += 1
    for word in ransom:
        if word not in w_dict:
            return False
        else:
            w_dict[word] -= 1
            if (w_dict[word] < 0):
                return False
    return True


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
