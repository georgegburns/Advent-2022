# import the day's data
with open('Day4Data.txt') as i:
    task = i.read()
    task = task.splitlines()
#print(task)

#defining a function to convert the list of strings into comparable lists
def redundancy_check(lst):
    total_overlap_count = 0
    overlap_count = 0
    comp_lsts = []
    #iterating through the list, creting new lists using the delimiter ,
    for item in lst:
        new_lst = item.split(',')
        for item in new_lst:
            #cleaning the strings to be ints
            start = item[0:2].replace('-','')
            end = item[2:].replace('-', '')
            temp = list(range(int(start), int(end)+1))
            comp_lsts.append(temp)
    #print(comp_lsts)
    #iterating through the pairs of lists and comparing if either set is contained in the other
    for lst in range(0, len(comp_lsts), 2):
        if set(comp_lsts[lst]).issubset(comp_lsts[lst+1]) or set(comp_lsts[lst+1]).issubset(comp_lsts[lst]):
            total_overlap_count += 1
    #iterating through the pairs of lists and comparing if there are shared elements between them
    for lst in range(0, len(comp_lsts), 2):
        for item in comp_lsts[lst]:
            if item in comp_lsts[lst+1]:
                overlap_count += 1
                break
    #returning the count of the overlap for each part 1 and 2
    return total_overlap_count, overlap_count
        
print(redundancy_check(task))