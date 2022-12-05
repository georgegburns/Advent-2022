#importing the day's data
with open('Day5Data.txt') as i:
    task = i.readlines()
    
#obtaining the crates part of the txt file
letters = task[0:8]

#cleaning the crates into a usable list of lists to make a dict
crates = []
num = 1
while num < 37:    
    for letter in letters:
        letter.replace('',',')
        crates.append(letter[0 + num])
    crates.append(' ')
    num += 4
crates_cleaned = [[]]
for i in crates:
    if i == ' ':
        crates_cleaned.append([])
    else:
        crates_cleaned[-1].append(i)
crates = [x for x in crates_cleaned if x != []]

#obtaining the locations of the crates from the txt file
numbers = task[8]
stacks = []
for num in numbers:
    stacks.append(num)
stacks = [x for x in stacks if x != ' ' and x != '\n']

#creating a dict of the areas + the crates located there
start = dict(zip(stacks, crates))
print(start)

#obtaining the instructions from the txt file
instructions = task[10:]
#print(len(instructions))

#part 1
#defining a function that takes the dict and the instructions and moves values according to the instructions
def crate_move(start, instructions):
    move = []
    start_stack = []
    end_stack = []
    for line in instructions:
        temp = line.split()
        if temp != []:
            move.append(temp[1])
            start_stack.append(temp[3])
            end_stack.append(temp[5])
    for i in range(len(move)):
        updated_lst = []
        for x in range(0,int(move[i])):
            item = start[start_stack[i]][x]
            updated_lst.append(item)
        for y in updated_lst:
            start[start_stack[i]].remove(y)
        updated_lst.reverse()
        new_value = updated_lst + start[end_stack[i]]
        start.update({end_stack[i] : new_value})
        print(f'Instruction {i+1}: move {move[i]} from {start_stack[i]} to {end_stack[i]}')
        if i < 10: 
            print(start)
    end_position = ''
    for k,v in start.items():
        end_position += v[0]
    return f'The crates at the end of the instructions are {end_position}'

#print(crate_move(start, instructions))

#part 2
def crate_move_v2(start, instructions):
    move = []
    start_stack = []
    end_stack = []
    for line in instructions:
        temp = line.split()
        if temp != []:
            move.append(temp[1])
            start_stack.append(temp[3])
            end_stack.append(temp[5])
    for i in range(len(move)):
        updated_lst = []
        for x in range(0,int(move[i])):
            item = start[start_stack[i]][x]
            updated_lst.append(item)
        for y in updated_lst:
            start[start_stack[i]].remove(y)
        #removed the reverse
        new_value = updated_lst + start[end_stack[i]]
        start.update({end_stack[i] : new_value})
        print(f'Instruction {i+1}: move {move[i]} from {start_stack[i]} to {end_stack[i]}')
        if i < 10: 
            print(start)
    end_position = ''
    for k,v in start.items():
        end_position += v[0]
    return f'The crates at the end of the instructions are {end_position}'

print(crate_move_v2(start, instructions))