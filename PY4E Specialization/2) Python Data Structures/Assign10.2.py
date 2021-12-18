"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution 
by hour of the day for each of the messages. You can pull the hour out from the 'From ' 
line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour 
as shown below.
"""

"""
Starter Code:

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

di = dict()

for line in handle:
    #line = line.rstrip()
    words = line.split()
    if not line.startswith('From '): continue
    words = words[5]
    hours = words.split(':')
    hours = hours[:1]
    for h in hours:
        di[h] = di.get(h,0) + 1

lst = list()

for v,k in di.items():
    lst.append((v,k))

#lst = sorted(lst,reverse=True)
lst.sort()

for v,k in lst:
    #lst.sort(key=lambda x:x[1])
    print(v,k)

