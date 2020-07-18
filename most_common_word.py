"""Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned
words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not
case sensitive.  The answer is in lowercase.

Example:

Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
"""

import re
import collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


# def mostCommonWord(paragraph, banned):
#     ban = set(banned)
#     words = re.findall(r'\w+', paragraph.lower())
#     return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]


def mostCommonWord(paragraph, ban):
    dic = {}
    banned = set(ban)
    words = re.findall(r'\w+', paragraph.lower())
    for word in words:
        if word not in banned:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
    return max(dic, key=dic.get)


print(mostCommonWord(paragraph, banned))
