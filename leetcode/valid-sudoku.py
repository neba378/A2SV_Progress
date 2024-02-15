
def checkList(each:List[List[str]]) -> bool:
        while("." in each):
            each.remove(".")
        distinctLen = len(set(each))
        eachLen = len(each)
        if distinctLen != eachLen:
            return False
        return True
class Solution:
    
        
        
        
        
        
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col1 = []
        col2 = []
        col3 = []
        col4 = []
        col5 = []
        col6 = []
        col7 = []
        col8 = []
        col9 = []
        sq1 = []
        sq2 = []
        sq3 = []
        sq4 = []
        sq5 = []
        sq6 = []
        sq7 = []
        sq8 = []
        sq9 = []
        for i in board:
            col1.append(i[0])
            col2.append(i[1])
            col3.append(i[2])
            col4.append(i[3])
            col5.append(i[4])
            col6.append(i[5])
            col7.append(i[6])
            col8.append(i[7])
            col9.append(i[8])
        for i in range(3):
            for j in range(3):
                sq1.append(board[i][j])
                sq2.append(board[i][j+3])
                sq3.append(board[i][j+6])
        for i in range(3,6):
            for j in range(3):
                sq4.append(board[i][j])
                sq5.append(board[i][j+3])
                sq6.append(board[i][j+6])
        for i in range(6,9):
            for j in range(3):
                sq7.append(board[i][j])
                sq8.append(board[i][j+3])
                sq9.append(board[i][j+6])
        for i in board:
            if (checkList(i) == False):
                return False
           
        if (checkList(col1) and
           checkList(col2) and
           checkList(col3) and
           checkList(col4) and
           checkList(col5) and
           checkList(col6) and
           checkList(col7) and
           checkList(col8) and
           checkList(col9) and
           checkList(sq1) and
           checkList(sq2) and
           checkList(sq3) and
           checkList(sq4) and
           checkList(sq5) and
           checkList(sq6) and
           checkList(sq7) and
           checkList(sq8) and
           checkList(sq9)):
            return True
        return False
        
                
                    