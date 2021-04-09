class Solve(object):
    def truckTour(petrolpumps):
        d = {}
        dis = 0
        l = len(petrolpumps)
        for i in range(l):
            dis += (petrolpumps[i][0] - petrolpumps[i][1])
            d[dis] = i

        return d[min(d)] + 1


if __name__ == '__main__':

    n = int(input())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = Solve.truckTour(petrolpumps)

    print(str(result) + '\n')
