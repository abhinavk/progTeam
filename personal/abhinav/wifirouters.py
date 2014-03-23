# Wifi Router


def dist(x, y):
    z = ((float(x[0])-int(y[0]))**2+(int(x[1])-int(y[1]))**2)**0.5
    return round(z, 6)

t = int(input())  # No of test cases
for _ in range(t):
    routers, users = tuple(input().split(' '))
    routers, users = int(routers), int(users)
    router = [input().split(' ') for i in range(routers)]
    user = [input().split(' ') for i in range(users)]
    udist = []
    rdist = [0]
    for i in range(users):
        udist.append(min([dist(router[j], user[i]) for j in range(routers)]))
    if routers > 1:
        for i in range(routers):
            rdist.append(min([dist(router[j], router[i]) for j in range(routers)
                         if i is not j]))
        rdist = max(rdist)
    print(max(max(udist), max(rdist)))
