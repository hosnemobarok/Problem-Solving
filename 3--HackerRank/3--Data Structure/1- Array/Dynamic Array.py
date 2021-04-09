def dynamicArray(n, queries):
    # Write your code here
    seqlist = [[] for _ in range(n)]

    lastAnswar = 0
    result = []
    for q, x, y in queries:
        seq = (x ^ lastAnswar) % n
        if q is 1:
            seqlist[seq].append(y)
        if q is 2:
            size = len(seqlist[seq])
            lastAnswar = seqlist[seq][y % size]
            result.append(lastAnswar)
    return result


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    result = dynamicArray(n, queries)
    print('\n'.join(map(str, result)))
