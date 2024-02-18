from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_flag = True
        col_flag = True

        for row in board:
            num = "".join(char for char in row if char.isdigit())
            if not num:
                row_flag = False
                break
            if row_flag:
                count = set()

                for i in row:
                    if i.isdigit():
                        if int(i) >= 0 and int(i) <= 10:
                            if i in count:
                                row_flag = False
                            else:
                                count.add(i)
                        else:
                            row_flag = False

        if row_flag:
            j_count = set()
            i = 0
            n = 0
            while n < 9 and i < 9:
                for row in board:
                    if row[i].isdigit():
                        if int(row[i]) >= 0 and int(row[i]) <= 10:
                            if row[i] in j_count:
                                col_flag = False
                            else:
                                j_count.add(row[i])
                        else:
                            col_flag = False
                print(j_count, len(j_count))
                # if not len(j_count):
                #     col_flag = False
                #     break
                j_count.clear()
                i += 1
                n += 1

        if row_flag == True and col_flag == True:
            return True
        else:
            return False

    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        """
        Determines whether the given 9x9 Sudoku board is valid or not.

        The function validates the Sudoku board by checking three conditions:

        1. No duplicate digits in each row.
        2. No duplicate digits in each column.
        3. No duplicate digits in each of the nine 3x3 subgrids.

        The solution uses three sets to keep track of seen digits in rows, columns, and subgrids.
        For each cell in the board, it checks whether the current digit violates any of the above conditions.

        The subgrid check is implemented by dividing the row index by 3 and the column index by 3,
        creating a unique identifier for each of the nine 3x3 subgrids.

        If a violation is found in any of the conditions, the function returns False; otherwise, it continues to the next cell.

        """
        row = defaultdict(set)
        cols = defaultdict(set)
        matrix = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in row[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in matrix[(r // 3, c // 3)]
                ):
                    return False
                else:
                    row[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    matrix[(r // 3, c // 3)].add(board[r][c])
        print(row)
        print(cols)
        print(matrix)

        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
board1 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


board3 = [
    [".", ".", "4", ".", ".", ".", "6", "3", "."],
    [".", ".", ".", ".", ".", "1", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "9", "."],
    [".", ".", ".", "5", "6", ".", ".", ".", "."],
    [".", ".", "3", ".", ".", ".", ".", ".", "1"],
    [".", ".", ".", "7", ".", ".", ".", ".", "."],
    [".", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", ".", ".", "2", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "2"],
]

board4 = [
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
]
a = Solution()

print(a.isValidSudoku2(board=board))
