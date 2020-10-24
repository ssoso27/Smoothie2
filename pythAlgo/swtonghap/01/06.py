def countPerms(n):
    MOD = 10 ** 9 + 7

    counts = {
        'a': [0 for _ in range(n)],
        'e': [0 for _ in range(n)],
        'i': [0 for _ in range(n)],
        'o': [0 for _ in range(n)],
        'u': [0 for _ in range(n)]
    }

    for k in counts.keys():
        counts[k][0] = 1

    for i in range(1, n):
        counts['a'][i] = (counts['e'][i - 1] + counts['u'][i - 1] + counts['i'][i - 1]) % MOD
        counts['e'][i] = (counts['a'][i - 1] + counts['i'][i - 1]) % MOD
        counts['i'][i] = (counts['e'][i - 1] + counts['o'][i - 1]) % MOD
        counts['o'][i] = (counts['i'][i - 1]) % MOD
        counts['u'][i] = (counts['i'][i - 1] + counts['o'][i - 1]) % MOD

    total = 0
    for k in counts.keys():
        total = (total + counts[k][n - 1]) % MOD

    return total