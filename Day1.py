string = open('Day1.txt','r').readline()
floor_count = 0
for i in range(0,len(string)):
    if string[i] == '(':
        floor_count += 1
    if string[i] == ')':
        floor_count -= 1
    if floor_count == -1:
        print("step count is {}".format(i+1))
print(floor_count)
