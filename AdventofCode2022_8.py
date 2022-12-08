# import the day's data
with open('Day8Data.txt') as i:
    task = i.read()
    task = task.splitlines()
#print(task)

#part 1

#building a set to remove duplicate coordinates and a list to iterate through 
visible = set()
trees = []
for line in task:
    temp = []
    for i in line:
        temp.append(i)
    trees.append(temp)

#for convenience, assigning the length and width of the area of trees to iterate through
length = range(len(trees))
width = range(len(trees[0]))

#going from top to bottom to establish if tree is visible
for y in width:
    #to start need to assign a height below the lowest
    highest = -1
    for x in length:
        #assigning the current tree
        current = int(trees[x][y])
        if current > highest:
            #if the tree is greater than the previous highest in this direction add to the set of visible trees and reassign highest
            tree = (x, y)
            highest = current
            visible.add(tree)
            
#going from bottom to top
for y in width:
    highest = -1
    for x in length:
        current = int(trees[len(trees) - 1 - x][y])
        if current > highest:
            tree = (len(trees) - 1 - x, y)
            highest = current
            visible.add(tree)  

#going from left to right
for x in length:
    highest = -1
    for y in width:
        current = int(trees[x][y])
        if current > highest:
            tree = (x, y)
            highest = current
            visible.add(tree)

#going from right to left
for x in length:
    highest = -1
    for y in width:
        current = int(trees[x][len(trees) - 1 - y])
        if current > highest:
            tree = (x, len(trees) - 1 - y)
            highest = current
            visible.add(tree)

#the set removes duplicates and the length is the number of visible trees
print(len(visible))

#building a dictionary of tree coordinates
viewing_dist = {}
for y in width:
    for x in length:
        tree = (y, x)
        viewing_dist[tree] = int(trees[y][x])

#reassigning length and width to be lists so I can later remove the edges which will have 0 viewing distance
length = len(trees)
width = len(trees[0])

#creating a list of possible movements 1 up, 1 down, 1 right, 1 left and no change
movement = [(0,1), (0,-1), (1,0), (-1,0)]
longest_view = 0

#the ranges are now only the interior trees, 1 tree deep
for x in range(1, width-1):
    for y in range(1, length-1):
        #assigning the current tree and building a list for the four possible view lengths
        current = viewing_dist[(x,y)]
        views = []
        #iterating through the movements
        for movex, movey in movement:
            view = 0
            X,Y = x,y
            while True:
                X,Y = X+movex, Y+movey
                if X < 0 or Y < 0 or X >= width or Y >= length:
                    break
                view += 1
                if viewing_dist[(X,Y)] >= current:
                    break
            #appending each view to the list of views
            views.append(view)
        i = 0
        #iterating through the lists to find the longest possible viewing distance
        while i != 1:
            n = views[0] * views[1] * views[2] * views[3]
            if n > longest_view:
                longest_view = n
            i += 1

print(longest_view)
        
