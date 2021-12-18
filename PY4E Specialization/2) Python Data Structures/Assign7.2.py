"""
7.2 Write a program that prompts for a file name, then opens that file and reads
 through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
    Average spam confidence: 0.750718518519
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name.
"""

"""
Starter Code:
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print(line)
print("Done")
"""

# Use the file name mbox-short.txt as the file name
fname = input('Enter file name: ')
fh = open(fname)
list = []
num = 0

for line in fh:
# Removes extraneous lines from file
    if not line.startswith('X-DSPAM-Confidence:') :
        continue
# Find start of numbers
    #numpos = line.find('0')
# Find end of float numbers
    #endpos = line.find('\n')
# Extract all numbers from string
    numbers = line[20 : 26]
# Converts the string numbers to floats
    x = float(numbers)
# Put all the floats in a list
    list.append(x)

# Create a loop that counts the elements in list
for flts in list:
    num += flts
# Calculate the average and store in variable avrg
avrg = num / len(list)
# Convert to string for final answer
str = str(avrg)
print('Average spam confidence: ' + str)
