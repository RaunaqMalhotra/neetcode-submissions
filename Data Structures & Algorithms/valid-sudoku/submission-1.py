"""
Understand:
- Input is a sudoku board
- List of lists
    - board[row][column]
- Max rows = max column = 9
- Length of list = 9
- Length of sublist = 9

No row should have duplicate numbers
No column should have duplicate numbers
No 3x3 box should have duplicate numbers

Board does not need to be complete
Empty spaces will be denoted by a .

For a 3x3 box
    - 00, 01, 02
    - 10, 11, 12
    - 20, 21, 22

So row 0 to 2, column 0 to 2

Match:
- Lists/Arrays
- Hashmap or Set to check duplicate elements for each row and column

Plan:
- Can make 3 subfunctions
    - check row
    - check column
    - check box

for row, just send in each sublist at a time
for column, we'll send in the index of each column and parse through every row
for box, indeces will be at an interval of 3
    - so 0-2, 3-5, 6-8 (for both row and column)

Implement:
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #Check for rows
        for row_index in range(0, 9): # 0 (Time O(n))

            row_set = set() # (1, 2, 3)
            column_set = set()
            for element in board[row_index]: # .
                if element != ".": # true
                    if element in row_set: # false
                        return False

                    row_set.add(element) # added
            
            # Check for columns
            for column_index in range(0, 9): # 8 (Time O(n))
                # We are checking every element in the same column so row changes, but column doesn't change
                # We do that for every row after checking the row
                current_element = board[column_index][row_index] #80
                if current_element != ".":
                    if current_element in column_set:
                        return False

                    column_set.add(current_element)

        # Check for boxes
        # 00 01 02  # 03 04 05  # 06 07 08
        # 10 11 12  # 13 14 15  # 16 17 18
        # 20 21 22  # 23 24 25  # 26 27 28

        # 30 31 32  # 33 34 35  # 36 37 38
        # 40 41 42  # 43 44 45  # 46 47 48
        # 50 51 52  # 53 54 55  # 56 57 58

        # 60 61 62  # 63 64 65  # 66 67 68
        # 70 71 72  # 73 74 75  # 76 77 78
        # 80 81 82  # 83 84 85  # 86 87 88

        for row in range(0, 9, 3): # Time O(n/3)
            for column in range(0, 9, 3): # Time O(n/3)
                box_indeces = [ 
                    (row, column), (row, column+1), (row, column+2),
                    (row+1, column), (row+1, column+1), (row+1, column+2),
                    (row+2, column), (row+2, column+1), (row+2, column+2)
                ]
                box_set = set() # (1, 2, 4, 9)
                for row_index, column_index in box_indeces: # 22
                    current_element = board[row_index][column_index] # board[2][1] = 1
                    if current_element != ".": # false
                        if current_element in box_set: # true
                            return False # returns False
                        box_set.add(current_element) # added

        
        return True


"""
Review:
- Done in comments

Evaluate:
Time:
- O(n)*O(n) = O(n^2) in the first nested loop
- O(n/3)*O(n/3) = O((n^2)/9) in the second nested loop for box checks

Space:
- O(n) for rowSet
- O(n) for columnSet
- O(n) for boxSet

O(3n) = O(n)
"""        