def lastLetters(word):
    s1, s2 = word[len(word)-1], word[len(word)-2]
    return s2 + ' ' + s1