import collections

def groupAnagrams(arr:list)-> list:
    anagrams = collections.defaultdict(list)

    for word in arr:
        anagrams[''.join(sorted(word))].append(word)

    return anagrams.values()



arr =['eat','tea','tan','ate','nat','bat']


print(groupAnagrams(arr))