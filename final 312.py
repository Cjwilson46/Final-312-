#importing module
import hashlib
import logging

# Reading And Writing Files
# create a new.txt file and set the mode to a+ for append/add a new text to the already existing file or a new file.
# similarly, we can use 'w' for file creation. The '+' sign indicates new file creation also if not exist.
f = open("new.txt", "a+")

# Initiating a for loop for writing data
for i in range(2):
    # f.write function appends the string after existing or opened file here it is new.txt and writes the line
    f.write("New line %d\r\n" % (i+1))

# Open a file in read mode 'r' describes the read mode
f = open("new.txt", "r")
# Below we check if the file mode is in read state then read the file content and print it
if f.mode == 'r':
    contents = f.read()
    print(contents)

# Hashing

# Closing the opened file
f.close()

# Initiating Objects
intval = 4
strval = 'My Hash Value'
floatval = 24.56

# Printing the hash values.
# Note: When printing, the integer value doesn't change, but float and character values change always.
print("The integer hash value is : " + str(hash(intval)))
print("The hash value is : " + str(hash(strval)))
print("The hash value is : " + str(hash(floatval)))

# Linear Search

# Initiated a list
n1array = list()
# How many numbers to sort? We take the input from the user, converting it to integer.
num = input("Enter how many elements you want:")

# Then take input array elements from user and appended to the list n1array
print('Enter numbers in array: ')
for i in range(int(num)):
    n = input("num :")
    n1array.append(int(n))

# Search function initiated, we defined for loop and scan array and match its search value. If it's matched, then we return index otherwise -1.
def search(arr, x):
    for i in range(len(arr)):
        if int(arr[i]) == int(x):
            return i
    return -1

# Search value input taken from user
search_num = input("Enter Number You Want To search For:")

# Passing the array and value to be searched in a search function then print it
response_val = search(n1array, search_num)
# If response is -1 then not found, otherwise found and show index
if(response_val == -1):
    print('Not Found')
else:
    print('The Value Found And Index Is', response_val)

# Logging

# Create and configure logger with date time and message with filemode 'w' for write
logging.basicConfig(filename="newlogfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating a log object
logger1 = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger1.setLevel(logging.DEBUG)

# Test messages
logger1.debug("Harmless debug Message")
logger1.info("Just an information")
logger1.warning("Its a Warning")
logger1.error("Did you try to divide by zero")
logger1.critical("Internet is down")
