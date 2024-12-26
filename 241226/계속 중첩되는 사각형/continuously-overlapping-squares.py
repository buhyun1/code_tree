def calculate_blue_area(n, rectangles):
    OFFSET = 100 
    grid = [[0] * 201 for _ in range(201)] 
    
    for i in range(n):
        x1, y1, x2, y2 = rectangles[i]
        x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
        
        color = 1 if i % 2 == 0 else 2
        for x in range(x1, x2):
            for y in range(y1, y2):
                grid[x][y] = color
    
    blue_area = sum(1 for x in range(201) for y in range(201) if grid[x][y] == 2)
    return blue_area

n = int(input())
rectangles = [tuple(map(int, input().split())) for _ in range(n)]

result = calculate_blue_area(n, rectangles)
print(result)
