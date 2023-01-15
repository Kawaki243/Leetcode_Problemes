from collections import defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # this section is to check whether or not the board has all the characters used for the word. This will handle odd large edge cases
        charFreq = defaultdict(int)
        for char in word:
            charFreq[char] += 1

        for row in range(len(board)):
            for col in range(len(board[row])):
                charFreq[board[row][col]] -= 1

        for freq in charFreq.values():
            if freq > 0:
                return False



        # backtrack part of the solution
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def withinBounds(row, col):
            if 0 <= row and row < len(board) and 0 <= col and col < len(board[0]):
                return True
            return False

        def dfs(row, col, visiting, i):
            if (row, col) in visiting:
                return False

            if board[row][col] != word[i]:
                return False

            if i == len(word) - 1:
                return True
            
            found = False
            visiting.add((row, col))

            for directionRow, directionCol in directions:
                nextRow, nextCol = row + directionRow, col + directionCol
                if withinBounds(nextRow, nextCol):
                    found = found or dfs(nextRow, nextCol, visiting, i + 1)

            visiting.remove((row, col))
            return found

        for row in range(len(board)):
            for col in range(len(board[row])):
                if dfs(row, col, set(), 0):
                    return True

        return False
