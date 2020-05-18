class Solution:
    def countAndSay(self, n: int) -> str:
        # The first sequence always be '1'
        seq = "1"
        for i in range(n-1):
            seq = self.getNext(seq)
        return seq

    def getNext(slef, seq):
        # always reset i and next_seq to 0 and empty
        i, next_seq = 0, ""
        while i < len(seq):
            count = 1
            while i < len(seq) - 1 and seq[i] == seq[i+1]:
                count += 1
                i += 1
            # add the counter and the number to the end of the next_seq
            next_seq += str(count) + seq[i]
            i += 1
        return next_seq