class Solution:
    def containsDuplicate(self, seq):
        len_seq = len(seq)
        return len_seq > 1 and len(set(seq)) != len_seq
