# import the day's data
with open('Day7Data.txt') as i:
    task = i.read()
    task = task.splitlines()
#print(task)

#part 1
#defining a Node class to contain each of the nodes in the tree (I had no idea how to do this, thank you StackOverflow)
class Node:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        self. children = []

#defining a start point (this is the base directory) as well as a list of directories and a list of the whole tree
start = Node("/", 0, None)
current = start 
directories = []
tree = []
tree.append(start)

#a function to iterate through each line of the task and establish whether it is a dir within a dir or a movement to a new directory
def tree_build(lst):
    for i in task:
        i = i.split()
        #$ means action either move to cd or ls
        if i[0] == '$':
            if i[1] == 'cd':
                #.. moves the directory one level above as such we set current to the parent
                if i[2] == '..':
                    current = start.parent
                #this is for the first iteration
                elif i[2] == '/':
                    directories.append(i[2])
                    current = start
                #this sets each new directory location, adds the current node to the tree and sets the parent as the second to last directory
                else:
                    directories.append(i[2])
                    current = Node(i[2], 0, directories[:-2])
                    tree.append(current)
        else:
            #if it isn't a $ action, it is either a directory within a directory (a child) or a file (size)
            if i[0] == 'dir':
                current.children.append(i[1])
            else:
                current.size += int(i[0])

tree_build(task)
#reverse the tree to iterate through
tree.reverse()

#these are for part2
MAX = 70000000
NEED = 30000000

#a function to build the sizes of all the directories (children included) and return the minimum amount needed to delete for the update
def size_comp(lst):
    temp = {}
    #this took an awfully long time, but this *mostly* correctly adds child sizes to parent sizes 
    #(due to the copies in directory names there are errors, but produces the right answer for part1)
    for i in range(len(tree)):
        for x in tree[i].children:
            #print(temp[x])
            tree[i].size += temp[x]
            temp[x] = tree[i].size
            #print(tree[i].name, tree[i].size, tree[i].children)
        temp[tree[i].name] = tree[i].size
        #print(tree[i].parent, tree[i].name, tree[i].size, tree[i].children)
    total_size = 0
    #iterating through to find all the directories with <= 100000 file size, summing them
    for i in range(len(tree)):
        if tree[i].size > 100000:
            pass
        else:
            total_size += tree[i].size
    return total_size
print(size_comp(tree))