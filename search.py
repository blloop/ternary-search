import time, os, random
clear = lambda: os.system('cls')

def print_frame(nums, start, end, points):
    clear()
    output = ''
    if (points):
        for i in range(0, start):
            output += "   "
        output += "  V"
        for i in range(start, end - 1):
            output += "   "
        if (end - start > 0):
            output += "  V"
        print(output)
    else:
        for i in range(0, start):
            output += "   "
        output += "  >"
        for i in range(start, end - 1):
            output += "---"
        output += "--<"
        print(output)  
    output = ''
    for i in range(len(nums)):
        output += '--|'
    output += '   Search: {}'.format(guess)
    print(output)
    output = ''
    for i in range(len(nums)):
        output += '{:3d}'.format(nums[i])
    print(output)

# Input an integer value between 10-30
length = 0
temp = 0

while (length < 1):
    print("Please enter an array size to search (10-30):")
    temp = input()
    try:
        temp = int(temp)
    except:
        pass
    if (isinstance(temp, int)):
        if (int(temp) > 30 or int(temp) < 10):
            print("Please enter a valid number")
        else:
            length = int(temp)
    else:
        print("Please enter an integer value")

# Create sorted array to search through
clear()
temp = 0
nums = []
seeds = [2, 3, 0, 1, 3, 2, 4, 2, 3, 1]

print("Generating a random sorted array of {} integers".format(length))
for i in range(length):
    temp += random.choice(seeds)
    nums.append(temp)
    
time.sleep(1)
clear()
print(nums)

# Input a number to search for
guess = -1
temp = 0

print("Please enter a number to search for (0-{}):".format((length*4)))
print("Press [ENTER] for a random array value")
while (guess < 0):    
    temp = input()
    try:
        temp = int(temp)
    except:
        pass
    if (not temp and not temp == 0):
        guess = random.choice(nums)
        break
    if (isinstance(temp, int)):
        check = int(temp)
        if (check > ((length*4)) or check < 0):
            print("Please enter a valid number")
        else:
            guess = check
    else:
        print("Please enter an integer value")

# Begin ternary search algorithm
clear()
start = 0
end = length - 1
found = False
print("Searching for the number {}...".format(guess))

while (end - start > 2):
    
    if (guess == nums[start]):
        # Found at start
        found = True
        print_frame(nums, start, end, True)
        time.sleep(1)
        print("Found " + str(guess) + " at index " + str(start))
        break
    if (guess == nums[end]):
        found = True
        print_frame(nums, start, end, True)
        time.sleep(1)
        # Found at end
        print("Found " + str(guess) + " at index " + str(end))
        break

    diff = end  - start
    print("Diff: " + str(diff) + ", Start: " + str(start) + ", End: " + str(end))
    print_frame(nums, start, end, False)
    r_mark = int(start + ((diff * 2) / 3))
    l_mark = int(start + (diff / 3))
    if (diff % 3 > 1):
        r_mark += 1
    print("Diff: " + str(diff) + ", Start: " + str(start) + ", End: " + str(end))
    print_frame(nums, l_mark, r_mark, True)
    if (guess < nums[l_mark]):
        # Found before left marker
        start = start + 1
        end = l_mark - 1
    elif (guess > nums[r_mark]):
        # Found after right marker
        start = r_mark + 1
        end = end - 1
    else:
        # Found between two markers, inclusive
        start = l_mark
        end = r_mark
        
if (not found):
    print("failed!!")
    print("Diff: " + str(diff) + ", Start: " + str(start) + ", End: " + str(end))
    
    print_frame(nums, start, end, True)
    for i in range(start, end + 1):
        if (nums[i] == guess):
            print_frame(nums, i, i, True)
            found = True
            break

if (not found):
    print("Diff: " + str(diff) + ", Start: " + str(start) + ", End: " + str(end))
    print_frame(nums, start - 1, end + 1, False)
    print("Value not found!!!")
            
time.sleep(1)
input("Press any key to terminate the program")
