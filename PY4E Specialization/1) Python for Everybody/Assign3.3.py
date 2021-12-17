"""
3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of 
range, print an error. If the score is between 0.0 and 1.0, print a grade using the 
following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. 
For the test, enter a score of 0.85.
"""


score = input("Enter Score:")
g = float(score)

if g > 1.0:
    print("Error")
elif g < 0.0:
    print("Error")
elif 1.0 >= g >= 0.90:
    print("A")
elif 0.89 >= g >= 0.80:
    print("B")
elif 0.79 >= g >= 0.70:
        print("C")
elif 0.69 >= g >= 0.60:
    print("D")
else:
    print("F")
