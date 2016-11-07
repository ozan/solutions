class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        i = 0
        len_haystack = len(haystack)
        len_needle = len(needle)
        while True:
            for j in xrange(len_needle):
                if i + j >= len_haystack:
                    return -1
                if haystack[i + j] != needle[j]:
                    i += 1
                    break
            else:
                return i
    
            if i >= len_haystack:
                return -1