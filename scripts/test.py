def poc(target):
    if target.startswith('a'):
        return True
    if target.startswith('b'):
        return False
    if target.startswith('c'):
        return None
    if target.startswith('d'):
        return [1, 2, 3]
    if target.startswith('e'):
        return set([1, 2, 3])
    if target.startswith('f'):
        return 'startswith f'
    if target.startswith('g'):
        return 123
    if target.startswith('h'):
        return 0
