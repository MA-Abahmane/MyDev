
def longestCommonPrefix(strns):

    # get the smallest word in the list
    strns.sort()
    min = len(strns[0])

    # compare each letter of the smallest words to the others
    for i in range(min):
        # if all letters on position i are the same; continue
        if all(strn[i] == strns[0][i] for strn in strns):
                continue
        else:
                return strns[0][:i]

    return strns[0]






strs1 = ["flower", "flow", "flight"]
strs2 = ["dog","racecar","car"]

print(longestCommonPrefix(strs1))
print(longestCommonPrefix(strs2))