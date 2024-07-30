class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def check(i,j,board,num):
            if(num in board[i]):return False
            if(num in [board[row][j] for row in range(9)]):return False
            for r in range((i//3)*3,((i//3)*3)+3):
                for c in range((j//3)*3,((j//3)*3)+3):
                    if(board[r][c]==num):return False
            return True

        def rec(board,i,j):
            if(j==9):
                i+=1;j=0
            if(i==9):
                return True
            if(board[i][j]=="."):
                for num in range(1,10):
                    if(check(i,j,board,str(num))):
                        board[i][j]=str(num)
                        if(rec(board,i,j+1)):return True
                        board[i][j]="."
                return False
            else:
                return rec(board,i,j+1)
        rec(board,0,0)
        return board
                    

            