n: int
_res: set = set()
given: list

def solve(first: int, second: int, num):
    global n, _res, given
    if num == n:
        if first == second:
            _res.add(first + second)
        return

    solve(first + given[num], second, num + 1)
    solve(first, second + given[num], num + 1)
    solve(first, second, num + 1)

if __name__ == "__main__":
    t1, t2 = map(int, input().split())
    barbells = [int(el) for el in input().split()]
    given = [int(el) for el in input().split()]
    n = len(given)
    solve(0, 0, 0)
    res = set()
    for b in barbells:
        for weight in _res:
            res.add(b+weight)
    res = list(res)
    res.sort()
    for i in res:
        print(i)
    
    