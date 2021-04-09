def runner_up_score(li):
    result = sorted(set(li))[-2]
    return result


if __name__=="__main__":
    n = int(input())
    li = list(map(int, input().split()))
    print(runner_up_score(li))
