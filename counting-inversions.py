# /usr/bin/python3

counter = 0


def merge(a, b):
    global counter
    pointer_a = 0
    pointer_b = 0
    length = len(a) + len(b)
    result = []
    for i in range(length):
        if pointer_a == len(a) and pointer_b < len(b):
            result += b[pointer_b:]
            return result
        if pointer_b == len(b) and pointer_a < len(a):
            result += a[pointer_a:]
            counter += len(a) - pointer_a
            return result
        if (a[pointer_a] <= b[pointer_b]):
            result.append(a[pointer_a])
            pointer_a += 1
        else:
            result.append(b[pointer_b])
            counter += 1
            pointer_b += 1
    return result


def merge_sort(a):
    if len(a) == 1:
        return a
    else:
        return merge(merge_sort(a[0:len(a)//2]), merge_sort(a[len(a)//2:]))


print(merge_sort([2, 1, 3, 1, 2]))
print(counter)
