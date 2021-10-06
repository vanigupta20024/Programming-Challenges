class Solution:
    # @param A : integer
    # @return a string
    def solve(self, A):
        def count_zeros(s):
            i = len(s) - 1
            t = 0
            while i >= 0 and s[i] == "0":
                t += 1
                i -= 1
            return t
        zeros = 0
        sol = 1
        ans = ""
        for i in range(1, A + 1):
            sol *= i
            z = count_zeros(str(sol))
            zeros += z
            sol = int(str(sol)[:len(str(sol)) - z])
        return str(sol) + "0" * zeros
