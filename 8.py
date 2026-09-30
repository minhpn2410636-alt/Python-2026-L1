def extract_even(l):
    result = []

    for i in l:
        if i % 2 == 0:
            result.append(i)

    return result

l = [1, 4, 5, -1, 10]

print(extract_even(l))