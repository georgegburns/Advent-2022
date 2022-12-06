#importing the day's data
with open('Day6Data.txt') as i:
    task = i.read()
    task = task.splitlines()
#print(task)

#part 1
def find_signal(lst):
    temp = []
    signal = ''
    for elem in lst:
        for i in elem:
            if len(temp) == 4 and len(temp) == len(set(temp)):
                break
            elif len(temp) == 4:
                temp.remove(temp[0])
                temp.append(i)
            else: 
                temp.append(i)
            signal += i
    print(temp)
    print(len(signal))
    
find_signal(task)

#part 2
def find_message(lst):
    temp = []
    signal = ''
    for elem in lst:
        for i in elem:
            #changed len to 14
            if len(temp) == 14 and len(temp) == len(set(temp)):
                break
            elif len(temp) == 14:
                temp.remove(temp[0])
                temp.append(i)
            else: 
                temp.append(i)
            signal += i
    print(temp)
    print(len(signal))

find_message(task)