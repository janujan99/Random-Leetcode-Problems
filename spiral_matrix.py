def spiral(matrix):
    directions = [(1, 0), (0,1), (-1,0), (0,-1)]
        
    dir_change = 0
        
    

    x = 0
    y = 0
    length = len(matrix[0])
    width = len(matrix)
    num_matrix_entries = length*width
    spiral_matrix = []
    visited_coordinates = set()

    while len(visited_coordinates) < num_matrix_entries:
        spiral_matrix.append(matrix[y][x])
        visited_coordinates.add((x,y))
        if not (0 <= x + directions[dir_change][0] < length and 0 <= y + directions[dir_change][1] < width) or (x+ directions[dir_change][0],y+ directions[dir_change][1]) in visited_coordinates:
            dir_change += 1
            if dir_change == 4:
                dir_change = 0
        x += directions[dir_change][0]
        y += directions[dir_change][1]
    
    return spiral_matrix



print(spiral([[1,2,3],[4,5,6],[7,8,9]]))