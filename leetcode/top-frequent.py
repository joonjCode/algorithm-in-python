from collections import Counter
import heapq


# def topKFrequent(nums, k):
#     freqs = Counter(nums)
#     print(f'freqs : {freqs}')
#     freqs_heap = []
#     for f in freqs:
#         heapq.heappush(freqs_heap, (-freqs[f], f))
#         print(freqs_heap)
#
#     topk = []
#     for _ in range(k):
#         topk.append(heapq.heappop(freqs_heap)[1])
#         print(f'topk: {topk}')
#
#     return topk

def topKFrequent(nums, k):
    return list(zip(*Counter(nums).most_common(k)))[0]


nums = [1, 1, 1, 2, 2, 3]
k = 2

print(topKFrequent(nums, k))
