class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        return self.row_ok(board) and self.col_ok(board) and self.box_ok(board)

    
    def no_duplicates(self, row: list[str]) -> bool:

        numbers = set()

        for num in row:
            if num == ".":
                continue
            
            if num in numbers:
                return False
            numbers.add(num)
        
        return True

    def row_ok(self, grid: list[list[str]]) -> bool:

        for i in range(len(grid)):
            if not self.no_duplicates(grid[i]):
                return False
        
        return True
    
    def col_ok(self, grid: list[list[str]]) -> bool:
        frequency = defaultdict(list)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                frequency[j].append(grid[i][j])
        
        for val in frequency.values():
            if not self.no_duplicates(val):
                return False
        
        return True

    def box_ok(self, grid: list[list[str]]) -> bool:
        frequency = defaultdict(list)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                row = i // 3
                column = j // 3
                frequency[f"{row},{column}"].append(grid[i][j])
        
        for val in frequency.values():
            if not self.no_duplicates(val):
                return False
        
        return True
        

        