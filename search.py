import time, os, random
clear = lambda: os.system('cls')

def print_frame(arr, g):
    clear()
    output = ''
    for i in range(len(arr)):
        output += '--|'
    output += '   Search: {}'.format(g)
    print(output)
    output = ''
    for i in range(len(arr)):
        output += '{:3d}'.format(arr[i])
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
array = []
seeds = [2, 3, 0, 1, 3, 2, 4, 2, 3, 1]

print("Generating a random sorted array of {} integers".format(length))
for i in range(length):
    temp += random.choice(seeds)
    array.append(temp)
    
time.sleep(2)
clear()
print(array)

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
        guess = random.choice(array)
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
print("Searching for the number {}...".format(guess))
time.sleep(2)
print_frame(array, guess)

input("Press any key to terminate the program")

