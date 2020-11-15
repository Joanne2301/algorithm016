class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters_only_list = [i for i in S if i.isalpha()]
        ans_list = []
        for i in S:
            if i.isalpha():
                ans_list.append(letters_only_list.pop())
            else:
                ans_list.append(i)
        return "".join(ans_list)
