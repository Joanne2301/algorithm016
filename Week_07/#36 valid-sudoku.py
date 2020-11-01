class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        r = [{} for i in range(9)]
        c = [{} for i in range(9)]
        squares = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    square_index = (i // 3 ) * 3 + j // 3

                    r[i][num] = r[i].get(num, 0) + 1
                    c[j][num] = c[j].get(num, 0) + 1
                    squares[square_index][num] = squares[square_index].get(num, 0) + 1

                    if r[i][num] > 1 or c[j][num] > 1 or squares[square_index][num] > 1:
                        return False         
        return True