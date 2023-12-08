"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longestCommonPrefix(strns):

    # sort list to get the smallest word
    strns.sort()

    # compare each letter of the smallest words to the others
    for i in range(len(strns[0])):
        # if all letters on position i are the same; continue
        if all(strn[i] == strns[0][i] for strn in strns):
                continue
        else:
                return strns[0][:i]

    return strns[0]






strs1 = ["flower", "flow", "flona"]
strs2 = ["dog","racecar","car"]

print(longestCommonPrefix(strs1))
print(longestCommonPrefix(strs2))