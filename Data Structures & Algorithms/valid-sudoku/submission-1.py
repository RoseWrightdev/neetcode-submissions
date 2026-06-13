class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s = set()
            for num in row:
                if num in s and num != ".":
                    return False
                else:
                    s.add(num)
        for c in range(9):
            s = set()
            for r in range(9):
                num = board[r][c]
                if num in s and num != ".":
                    return False
                else:
                    s.add(num)
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                s = set()
                for r in range(start_row, start_row + 3):
                    for c in range(start_col, start_col + 3):
                        num = board[r][c]
                        if num in s and num != ".":
                            return False
                        else:
                            s.add(num)
        return True

