def spiralOrder(matrix):
    if len(matrix) == 0:
        return []
    right = (1, 0) 
    down = (0, 1)
    left = (-1, 0)
    up = (0, -1)
    directions = [right, down, left, up]
        
    n = 0
    curr_dirr = directions[n]
        
    def change_dir():
        nonlocal n
        nonlocal curr_dirr
        n += 1
        if n > 3:
            n = 0
        curr_dirr = directions[n]
        return
        
    traversal = []
    explored = []
    counter = 0
        
    pos_x = 0
    pos_y = 0
    while counter < len(matrix)*len(matrix[0]):
        traversal.append(matrix[pos_y][pos_x])
        explored.append((pos_x, pos_y))
        if not 0 <= pos_x + curr_dirr[0] < len(matrix[0]) or not 0 <= pos_y + curr_dirr[1] < len(matrix) or (pos_x + curr_dirr[0], pos_y + curr_dirr[1]) in explored:
            change_dir()
        pos_x += curr_dirr[0]
        pos_y += curr_dirr[1]
        counter += 1
    return traversal
    
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    