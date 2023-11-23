def to_check_piling(test_cases):
    results = []

    for n, sl in test_cases:
        while len(sl) > 1 and (sl[0] >= sl[-1]):
            a = sl.pop(0) if sl[0] >= sl[-1] else sl.pop()

            if sl and (sl[0] > a or sl[-1] > a):
                results.append("No")
                break
        else:
            results.append("Yes")

    return results
