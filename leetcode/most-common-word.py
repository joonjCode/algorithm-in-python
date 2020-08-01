def mostCommonWord(p:str, banned:list)-> str:
    from collections import Counter
    import re
    p = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
    c = Counter(p)

    return c.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(mostCommonWord(paragraph, banned))