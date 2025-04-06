#create a function which takes input of sudoku and row_no. create a empty list. run a for loop across that
#row and check whether that element >0 and that element is not present is the list then append the element
#and if present in list then return False

def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    new_list =[]
    for element in row: 
        if element >0:
            if element not in new_list:
                new_list.append(element)
            else:
                return False
    return True

if __name__ == "__main__":
    sudoku = [[9, 0, 0, 0, 8, 0, 3, 0, 0], [2, 0, 0, 2, 5, 0, 7, 0, 0]]
    print(row_correct(sudoku, 1))