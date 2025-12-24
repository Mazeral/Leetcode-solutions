class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        if a | b == c:
            return 0
        # 1. Get clean strings first
        b_a = bin(a)[2:]
        b_b = bin(b)[2:]
        b_c = bin(c)[2:]
        flips = 0

        # 2. Find the max length among the CLEAN strings
        max_len = max(len(b_a), len(b_b), len(b_c))

        # 3. Pad them so they are all the same length
        b_a = b_a.zfill(max_len)
        b_b = b_b.zfill(max_len)
        b_c = b_c.zfill(max_len)

        for i in range(max_len):
            c_bit = b_c[i]
            if c_bit == '0':
                if b_a[i] == '1':
                    flips += 1
                if b_b[i] == '1':
                    flips += 1
            elif c_bit == '1':
                if b_a[i] == '0' and b_b[i] == '0':
                    flips += 1
            else:
                break
        return flips
