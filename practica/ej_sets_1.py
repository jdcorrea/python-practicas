if __name__ == '__main__':
    s = set([1, 2, 3])
    t = set([3, 4, 5])

    print(s.union(t))
    print(s.intersection(t))
    print(s.difference(t))
    print(t.difference(s))
    print(1 in s)
    print(1 in t)
    print(1 not in t)
    print(1 not in t)
