from heapq import heappush, heappop, heapify


def cookies(k, A):
    count = 0
    heapify(A)

    try:
        while A[0] <= k:
            count += 1
            sm = (1 * heappop(A)) + (2 * heappop(A))
            heappush(A, sm)

    except IndexError:
        if count == 100000:
            return count - 1
        return -1

    return count


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    print(str(result) + '\n')
