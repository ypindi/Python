class Solution:
    def printZigzag(self, s: str, numRows: int) -> None:
        if numRows == 1:
            print(s)
            return

        rows = [[] for _ in range(numRows)]
        current_row = 0
        going_down = True

        for ch in s:
            # add one column
            for r in range(numRows):
                if r == current_row:
                    rows[r].append(ch)
                else:
                    rows[r].append(' ')

            # change direction at top/bottom
            if current_row == numRows - 1:
                going_down = False
            elif current_row == 0:
                going_down = True

            current_row += 1 if going_down else -1

        for row in rows:
            print(' '.join(row).rstrip())

sol = Solution()
sol.printZigzag("PAYPALISHIRING", 4)


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python> python3 .\LeetCode\10_zigzagPattern.py
# P           I           N
#   A       L   S       I   G
#     Y   A       H   R
#       P           I