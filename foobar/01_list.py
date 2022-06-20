ArrayOne = [3, 4, 8, 11, -3, 1]
ArrayTwo = [1, 4, 11, 3, 7, -3, 10]


def compare(one, two):
    diff = []

    repeat = 0
    while repeat in range(0,2):
        x = 0
        while x < len(one):
            y = 0
            while y < len(two):
                if one[x] == two[y]:
                    break
                else:
                    if y == len(two) - 1:
                        diff.append(one[x])
                    y += 1
            x += 1
        repeat += 1
        one, two = two,one

    diff = sorted(diff)
    return diff


if __name__ == '__main__':
    print(f'Different numbers in both lists:')
    print(compare(ArrayOne, ArrayTwo))