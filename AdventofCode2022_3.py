# import the day's data
with open('Day3Data.txt') as i:
    task = i.read()
    task = task.splitlines()
#print(task)

#part 1
#creating a dictionary of letters to their numerical value using their ord
letters = {}

#lowercase
for i in range (ord('a'), ord('z') + 1):
    letters[chr(i)] = ord(chr(i)) - 96

#uppercase
for i in range (ord('A'), ord('Z') + 1):
    letters[chr(i)] = ord(chr(i)) - 38
#print(letters)

#splitting each string into two and comparing for the duplicate letter, adding that letter to a list
duplicate_letters = []
for string in range(len(task)):
    first_half = task[string][:len(task[string]) // 2]
    second_half = task[string][len(first_half):]
    duplicate_letters.append(''.join(set(first_half).intersection(second_half)))

#summing the value of the letters
total = 0
for letter in duplicate_letters:
    total += letters.get(letter)
#print(total)

#part 2
#sublisting every three elves and then finding the duplicate letter
badges = []
for string in range(0,len(task), 3):
    elves = task[string:string + 3]
    for elf in elves:
        first = elves[0]
        second = elves[1]
        third = elves[2]
        match1 = ''.join(set(first).intersection(second))
        match2 = ''.join(set(match1).intersection(third))
        badges.append(match2)
        
#removing the duplicates from each three-group              
non_dup_badges = []
for i in range(0,len(badges), 3):
    non_dup_badges.append(badges[i])

#summing the value of the letters
total2 = 0
for badge in non_dup_badges:
    total2 += letters.get(badge)
#print(total2)