# Create a function that takes a grid of # and -, 

# created a 2D list with # and - inside 
grid_list = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]]

# def function takes in grid_list as a parameter 
# len function gets the number of characters,if its equal to zero it will return
# nested for loop loops through the trows and coloums  
def hastags (grid_list):
    n = len(grid_list)
    if n == 0:
        return
    index = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    m = len(grid_list[0])
    new_grid = [[ "#" for j in range(m)] for i in range(n)]
    
    for row in range(n):
        for coloum in range(m):
            if(grid_list[row][coloum] == "-"):
                count = 0
                
# for loop loops through the postions, if its = # it will increment by 1          
                for pos in index:
                    pr = row + pos[0]
                    pc = coloum + pos[1]
                    if(pr >= 0 and pr < n and pc >=0 and pc < m and grid_list[pr][pc] == "#"):
                        count = count + 1
                new_grid[row][coloum] = count
    
    return new_grid

new_grid = hastags(grid_list)
print(new_grid)

# https://stackoverflow.com/questions/72898841/python-data-structures-2d-lists
# helped me gain understanding on this topic 