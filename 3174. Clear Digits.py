#https://leetcode.com/problems/clear-digits/description/








class Solution:
    def clearDigits(self, s: str) -> str:
        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        s_dict = {}
        def backtrack(s_d):

            for i in range(len(s_d)-1, -1, -1):

                print(s_dict)
                if s_d[i] == True:

                    for jdx in range(i - 1, -1, -1):


                        if s_d[jdx] == False:
                            s_d[jdx] = "checked"


                            break



            return s_dict
        for idx, char in enumerate(s):
            s_dict[idx] = char in digits
        letters = backtrack(s_dict)
        return "".join(map(lambda x: str(s[x]), [idx for idx, v in letters.items() if v != "checked" and v != True]))


















if __name__ == '__main__':
    sol = Solution()
    an = Solution.clearDigits(1, "a2q2cvbbb1")
    print(an)