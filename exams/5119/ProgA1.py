import csv

headers = []
clients = []
filename = "vendas.csv"

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    headers = next(csvreader)
    for row in csvreader:
        clients.append(row)


def biggestname():
    max = None
    for client in clients:
        if max is None:
            max = client
        else:
            if len(client[1]) > len(max[1]):
                max = client
    maxs = []
    for client in clients:
        if len(client[1]) == len(max[1]):
            maxs.append(client)
    return maxs


def checkwords():
    words = []
    for client in clients:
        count = 1
        x = 0
        while x < len(client[1]):
            if ' ' == client[1][x]:
                count += 1
            x += 1
        words.append(count)
    x = 0
    idx = 0
    max = int(words[x])
    while x < len(words):
        if max < int(words[x]):
            max = int(words[x])
            idx = x
        x += 1
    maxclient = clients[idx]
    idx = 0
    maxclients = []
    for entries in words:
        if max == entries:
            maxclients.append(clients[idx])
        idx += 1
    return maxclients


def sort():
    trade = True
    while trade:
        trade = False
        idx = 0
        while idx < len(clients) - 1:
            if float(clients[idx][3]) > float(clients[idx+1][3]):
                clients[idx], clients[idx+1] = clients[idx + 1], clients[idx]
                trade = True
            idx += 1
    return clients


def sortname():
    trade = True
    while trade:
        trade = False
        idx = 0
        while idx < len(clients) - 1:
            if clients[idx][1] > clients[idx+1][1]:
                clients[idx], clients[idx + 1] = clients[idx + 1], clients[idx]
                trade = True
            if clients[idx][1] == clients[idx+1][1]:
                if float(clients[idx][3]) > float(clients[idx + 1][3]):
                    clients[idx], clients[idx + 1] = clients[idx + 1], clients[idx]
            idx += 1
    return clients


if __name__ == '__main__':
    print(f'Numero de clientes = {len(clients)}.')
    print()
    print(f'Cliente(s) com o nome mais comprido:')
    for entries in biggestname():
        print(entries)
    print()
    print(f'Cliente(s) com mais palavras no nome:')
    for entries in checkwords():
        print(entries)
    print()
    print('Clientes por ordem crescente de divida:')
    for entries in sort():
        print(entries)
    print()
    print('Clientes por ordem crescente de nome e divida:')
    for entries in sortname():
        print(entries)
    print()
