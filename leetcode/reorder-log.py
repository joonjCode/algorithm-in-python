
def reorderLog(logs:list)-> list:
    letters, digits = [],[]
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    # 문자 순으로정렬 뒤, 요소의 번호로 정렬
    letters.sort(key = lambda x:(x.split()[1:], x.split()[0]))
    return letters+digits




logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]



print(reorderLog(logs))

print(logs[0].split())