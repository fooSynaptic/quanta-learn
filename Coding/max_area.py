#py3

def max_area(area, i, j, cnt):
    if not (i >= 0 and i < len(area)) or not (j >= 0 and j < len(area[0])) or area[i][j] == None:
        return cnt

    if area[i][j] == 0:
        if flip:
            area[i][j] = 1
            flip -= 1
            track = max(max_area(area, i+1, j, cnt+1),
            max_area(area, i-1, j, cnt+1),
            max_area(area, i, j+1, cnt+1),
            max_area(area, i, j-1, cnt+1))
            area[i][j] = 0
            return track
        else:
            return 0

    else:                               
        area[i][j] = None

        track = max(max_area(area, i+1, j, cnt+1),
        max_area(area, i-1, j, cnt+1),
        max_area(area, i, j+1, cnt+1),
        max_area(area, i, j-1, cnt+1))
        area[i][j] = 1

        return track


grid = [[0, 0], [1, 1]]

for i in range(2):
    for j in range(2):
        if grid[i][j] == 1:
            flip = 1
            print(max_area(grid, i, j, 0))