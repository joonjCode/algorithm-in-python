#
# // No.4
# // Given a string of words, your goal is to find the highest scoring word in the string.
# //a is worth 1 point, b is worth 2 points, c is worth 3 points, and so on, all the way up until z, which is worth 26 points.
# //You can assume that strings will consist only of lowercase letters and spaces.
# // In the event that two words have the same score, return the word that appears first in the string.



import string
def highestScoringWord(s):
    values = dict(zip(string.ascii_lowercase, range(1,27)))

    def get_value(w):
        return sum(values[letter] for letter in w)

    return max(s.split(), key=get_value)


print(highestScoringWord("a b c d e f"))
print(highestScoringWord("hello world"))



