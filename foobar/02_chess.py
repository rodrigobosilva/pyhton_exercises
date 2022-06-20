chess = [
    [ 0,  1,  2,  3,  4,  5,  6,  7],
    [ 8,  9, 10, 11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20, 21, 22, 23],
    [24, 25, 26, 27, 28, 29, 30, 31],
    [32, 33, 34, 35, 36, 37, 38, 39],
    [40, 41, 42, 43, 44, 45, 46, 47],
    [48, 49, 50, 51, 52, 53, 54, 55],
    [56, 57, 58, 59, 60, 61, 62, 63]
]

moves = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]


def printmap():
    for row in chess:
        print('----------------------------------------')
        for data in row:
            print(f' {data: >2} |', end='')
        print()
            #print(f'{data : >2} = chess[{int(data/8)}][{data%8}]')
    print('----------------------------------------')
    print()


def jumps(alfa, beta):
    tent = [[alfa]]
    idx = 0
    while idx < len(tent):
        idy = 0
        tent.append([])
        while idy < len(tent[idx]):
            x = int(tent[idx][idy]/8)
            y = int(tent[idx][idy]%8)
            for entry in moves:
                newx, newy = entry
                #print(f'newx = {newx}')
                #print(f'newy = {newy}')
                #print(f'[x + newx] = {(x + newx)} [y + newy] = {(y + newy)}')
                if x + newx < 0 or x + newx > 7 or y + newy < 0 or y + newy > 7:
                    continue
                else:
                    tent[idx + 1].append(chess[x + newx][y + newy])
            idy += 1
        if beta in tent[idx + 1]:
            break
        else:
            idx += 1
    jumps = len(tent) - 1
    return jumps


if __name__ == '__main__':

    printmap()
    print(f'Insert starting number:')
    start = int(input(' >> '))
    print(f'Insert ending number:')
    end = int(input(' >> '))
    print(f'The number of jumps from {start} to {end} is {jumps(start,end)}.')

    '''
    for x in range(0, 64):
        for y in range(0, 64):
            print(x,y)
            print(jumps(x,y))
    '''