def lessThan(lst, n):
    if lst == []:
        return []
    if lst[0] < n:
        return [lst[0]] + lessThan(lst[1:], n)
    else:
        return lessThan(lst[1:], n)
