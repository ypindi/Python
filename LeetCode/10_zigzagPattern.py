class Solution:
    def printZigzag(self, s: str, numRows: int) -> None:
        if numRows==1:
            print(s)
            return
        
        rows = [[] for _ in range(numRows)]
        goingDown=True
        currentRow = 0
        for myChar in s:
            for i in range(numRows):
                if i==currentRow:
                    rows[i].append(myChar)
                else:
                    rows[i].append(' ')
            if currentRow==0:
                goingDown = True
            elif currentRow==numRows-1:
                goingDown = False
            if goingDown:
                currentRow+=1
            else:
                currentRow-=1
        
        for row in rows:
            print(' '.join(row))

    def printZigzag2(self, s: str, numRows: int) -> None:
        if numRows == 1:
            print(s)
            return

        n = len(s)
        grid = [[' ' for _ in range(n)] for _ in range(numRows)]

        row = 0
        col = 0
        i = 0

        while i < n:
            # go straight down
            while i < n and row < numRows:
                grid[row][col] = s[i]
                i += 1
                row += 1

            row -= 2
            col += 1

            # go diagonally up-right
            while i < n and row > 0:
                grid[row][col] = s[i]
                i += 1
                row -= 1
                col += 1

        for r in range(numRows):
            print(''.join(grid[r]).rstrip())

sol = Solution()
sol.printZigzag("PAYPALISHIRING", 4)
print()
sol.printZigzag2("PAYPALISHIRING", 4)


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python> python3 .\LeetCode\10_zigzagPattern.py
# P           I           N
#   A       L   S       I   G
#     Y   A       H   R
#       P           I
# 
# P  I  N
# A LS IG
# YA HR
# P  I