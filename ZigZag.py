class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If only one row or numRows exceeds string length, return as is
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize list of strings for each row
        rows = [''] * numRows

        row = 0
        step = 1

        # Build the zigzag pattern
        for c in s:
            rows[row] += c
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step

        # Concatenate all rows
        return ''.join(rows)
