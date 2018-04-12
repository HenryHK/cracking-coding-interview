#!/usr/bin/python3
# Idea: keep a map
contacts = {}
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if (op == "add"):
        length = len(contact)
        counter = 0
        while counter < length:
            if contacts.__contains__(contact[0:counter+1]):
                contacts[contact[0:counter+1]] += 1
            else:
                contacts[contact[0:counter+1]] = 1
            counter += 1
    if (op == "find"):
        if contacts.get(contact):
            print(contacts.get(contact))
        else:
            print(0)
