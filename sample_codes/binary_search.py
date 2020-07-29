from bisect import bisect_left, bisect_right


# x 데이터 인덱스 반환

def index_of_x(a,x):
    i = bisect_left(a,x)
    if i != len(a) and a[i] = x:
        return i
    return None

# Return index that is smaller than x
def index_of_less_than_x(a,x):
    i = bisect_left(a,x)
    if i:
        return i-1
    return None

