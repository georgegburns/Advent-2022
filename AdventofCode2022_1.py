
#importing the data from advent of code
with open('Day1Data.txt') as i:
    task = i.read()
    task = task.splitlines()

# part 1: putting the data into a list of lists split by none values (false)
result = [[]]
for i in task:
    if not i:
        result.append([])
    else:
        result[-1].append(i)

# iterating through the list of lists and comparing the sum of each, replacing with a new highest value if found
calories = 0
for li in result:
    temp = 0
    for i in li:
        temp += int(i)
        if temp > calories:
            calories = temp
            
#print(calories)

# part 2: creating a list of summed lists
calories2 = []
for li in result:
    temp = 0
    for i in li:
        temp += int(i)
        calories2.append(temp)
# ordering the list by highest value to lowest and then summing the top 3  
calories2.sort(reverse=True)
top3 = sum(calories2[0:3])

print(top3)
