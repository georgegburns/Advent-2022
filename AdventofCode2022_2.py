# import the day's data
with open('Day2Data.txt') as i:
    task = i.read()
    task = task.splitlines()
#print(task)

#part1
# replace letter values with corresponding point values
task_cleaned = [i.replace('Z', '3') for i in task]
task_cleaned = [i.replace('Y', '2') for i in task_cleaned]
task_cleaned = [i.replace('X', '1') for i in task_cleaned]
task_cleaned = [i.replace('A', '1') for i in task_cleaned]
task_cleaned = [i.replace('B', '2') for i in task_cleaned]
task_cleaned = [i.replace('C', '3') for i in task_cleaned]

#print(task_cleaned)

#create a total score
score = 0

#iterate through each list item and give the appropriate number of points for each occurence
for i in task_cleaned:
    if i[0] == i[2]:
        score += 3 + int(i[2])  
    elif (i[0] == "1" and i[2] == "2") or (i[0] == "2" and i[2] == "3") or (i[0] == "3" and i[2] == "1"): 
        score += 6 + int(i[2])
    else:
        score += int(i[2])
        
#print(score)

#part2
#replace only the opponents values with the points
task_cleaned2 = [i.replace('A', '1') for i in task]
task_cleaned2 = [i.replace('B', '2') for i in task_cleaned2]
task_cleaned2 = [i.replace('C', '3') for i in task_cleaned2]

#new total score
score2 = 0

# iterating through the possible scenarios of Draw, Win and Lose and then adding the appropriate points
for i in task_cleaned2:
    if i[2] == "Y":
        if i[0] == "1":
            score2 += 4
        elif i[0] == "2":
            score2 += 5
        else:
            score2 += 6
    elif i[2] == "Z":
        if i[0] == "1":
            score2 += 8
        elif i[0] == "2":
            score2 += 9
        else:
            score2 += 7
    else:
        if i[0] == "1":
            score2 += 3
        elif i[0] == "2":
            score2 += 1
        else:
            score2 += 2

print(score2)
    
